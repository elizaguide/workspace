#!/usr/bin/env python3
"""
Nano Banana Pro Image Generator

Generates images using Google's Gemini API.
Reads API key from .env file.

Usage:
    python generate_image.py "prompt" [options]

Options:
    --output, -o      Output file path (default: generated_image.png)
    --size, -s        Image size: square, landscape, portrait (default: square)
    --style           Style hint: photo, illustration, 3d, icon (optional)
    --count, -n       Number of images to generate (default: 1, max: 4)
    --env-file        Path to .env file (default: .env in current or parent dirs)

Examples:
    python generate_image.py "A serene mountain landscape at sunset"
    python generate_image.py "Modern minimalist logo" --style icon --output logo.png
    python generate_image.py "Hero background for wellness website" --size landscape -n 2
"""

import argparse
import base64
import json
import os
import sys
from pathlib import Path
from typing import Optional


def find_env_file(start_path: Optional[str] = None) -> Optional[Path]:
    """Find .env file in current directory or parent directories."""
    if start_path:
        env_path = Path(start_path)
        if env_path.exists():
            return env_path

    current = Path.cwd()
    for _ in range(10):  # Check up to 10 parent directories
        env_file = current / ".env"
        if env_file.exists():
            return env_file
        if current.parent == current:
            break
        current = current.parent
    return None


def load_api_key(env_file: Optional[Path] = None) -> str:
    """Load Google Gemini API key from .env file or environment."""
    # First check environment variable
    api_key = os.environ.get("GOOGLE_GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if api_key:
        return api_key

    # Find and parse .env file
    env_path = find_env_file(env_file)
    if not env_path:
        raise ValueError(
            "No .env file found. Create a .env file with GOOGLE_GEMINI_API_KEY=your_key\n"
            "or set the GOOGLE_GEMINI_API_KEY environment variable."
        )

    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            if "=" in line:
                key, _, value = line.partition("=")
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key in ("GOOGLE_GEMINI_API_KEY", "GEMINI_API_KEY"):
                    return value

    raise ValueError(
        f"GOOGLE_GEMINI_API_KEY not found in {env_path}\n"
        "Add this line to your .env file: GOOGLE_GEMINI_API_KEY=your_api_key"
    )


def get_aspect_ratio(size: str) -> str:
    """Convert size name to aspect ratio."""
    sizes = {
        "square": "1:1",
        "landscape": "16:9",
        "portrait": "9:16",
        "wide": "3:2",
        "tall": "2:3",
    }
    return sizes.get(size.lower(), "1:1")


def enhance_prompt(prompt: str, style: Optional[str] = None, context: Optional[str] = None) -> str:
    """Enhance prompt with style hints and context for better results."""
    enhanced = prompt

    # Add style-specific enhancements
    style_hints = {
        "photo": "photorealistic, high quality photograph, professional photography",
        "illustration": "digital illustration, clean vector art style, modern design",
        "3d": "3D rendered, soft lighting, clean modern aesthetic",
        "icon": "minimal icon design, flat design, simple geometric shapes, clean lines",
        "hero": "website hero image, professional, high resolution, modern aesthetic",
        "feature": "clean product feature image, professional, well-lit",
        "avatar": "profile picture style, centered subject, clean background",
        "abstract": "abstract art, modern design, artistic composition",
    }

    if style and style.lower() in style_hints:
        enhanced = f"{enhanced}, {style_hints[style.lower()]}"

    # Add context-specific enhancements for web design
    if context:
        context_lower = context.lower()
        if "hero" in context_lower or "background" in context_lower:
            enhanced = f"{enhanced}, suitable for website hero section, high resolution"
        elif "icon" in context_lower:
            enhanced = f"{enhanced}, clean icon design, transparent background friendly"
        elif "avatar" in context_lower or "profile" in context_lower:
            enhanced = f"{enhanced}, portrait style, centered composition"

    return enhanced


def generate_image(
    prompt: str,
    api_key: str,
    output_path: str = "generated_image.png",
    size: str = "square",
    style: Optional[str] = None,
    count: int = 1,
    context: Optional[str] = None,
) -> list[str]:
    """
    Generate image(s) using Google Gemini API.

    Args:
        prompt: Text description of the image to generate
        api_key: Google Gemini API key
        output_path: Base path for output file(s)
        size: Image size (square, landscape, portrait)
        style: Optional style hint
        count: Number of images to generate (1-4)
        context: Optional context for prompt enhancement

    Returns:
        List of paths to generated images
    """
    from google import genai
    from google.genai import types

    # Create client
    client = genai.Client(api_key=api_key)

    # Enhance the prompt
    enhanced_prompt = enhance_prompt(prompt, style, context)

    # Generate images
    print(f"Generating {count} image(s)...")
    print(f"Prompt: {enhanced_prompt}")
    print(f"Size: {size}")

    output_paths = []
    base_path = Path(output_path)

    # Ensure output directory exists
    base_path.parent.mkdir(parents=True, exist_ok=True)

    for i in range(count):
        # Use Gemini 2.0 Flash with image generation
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=f"Generate an image: {enhanced_prompt}",
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"]
            )
        )

        # Extract image from response
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None and part.inline_data.mime_type.startswith('image/'):
                if count == 1:
                    file_path = base_path
                else:
                    file_path = base_path.parent / f"{base_path.stem}_{i+1}{base_path.suffix}"

                with open(file_path, "wb") as f:
                    f.write(part.inline_data.data)
                output_paths.append(str(file_path))
                print(f"Saved: {file_path}")
                break

    return output_paths


def main():
    parser = argparse.ArgumentParser(
        description="Generate images using Google Gemini API (Nano Banana Pro)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "A serene mountain landscape at sunset"
  %(prog)s "Modern minimalist logo" --style icon -o logo.png
  %(prog)s "Hero background for wellness app" --size landscape
  %(prog)s "Professional headshot placeholder" --style avatar -n 2

Size options: square (1:1), landscape (16:9), portrait (9:16), wide (3:2), tall (2:3)
Style options: photo, illustration, 3d, icon, hero, feature, avatar, abstract
        """
    )

    parser.add_argument("prompt", help="Text description of the image to generate")
    parser.add_argument("-o", "--output", default="generated_image.png",
                       help="Output file path (default: generated_image.png)")
    parser.add_argument("-s", "--size", default="square",
                       choices=["square", "landscape", "portrait", "wide", "tall"],
                       help="Image aspect ratio (default: square)")
    parser.add_argument("--style",
                       choices=["photo", "illustration", "3d", "icon", "hero", "feature", "avatar", "abstract"],
                       help="Style hint for generation")
    parser.add_argument("-n", "--count", type=int, default=1,
                       help="Number of images to generate (1-4, default: 1)")
    parser.add_argument("--env-file", help="Path to .env file")
    parser.add_argument("--context", help="Additional context (e.g., 'hero section', 'feature card')")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()

    # Validate count
    if args.count < 1 or args.count > 4:
        print("Error: Count must be between 1 and 4")
        sys.exit(1)

    try:
        # Load API key
        api_key = load_api_key(args.env_file)
        if args.verbose:
            print(f"API key loaded successfully")

        # Generate image(s)
        output_paths = generate_image(
            prompt=args.prompt,
            api_key=api_key,
            output_path=args.output,
            size=args.size,
            style=args.style,
            count=args.count,
            context=args.context,
        )

        print(f"\nGenerated {len(output_paths)} image(s):")
        for path in output_paths:
            print(f"  - {path}")

    except ValueError as e:
        print(f"Configuration Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error generating image: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
