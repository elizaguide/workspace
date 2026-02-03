#!/usr/bin/env python3
"""
Spanish Progress Tracker
Monitors learning metrics and generates progress reports
"""

import json
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from pathlib import Path

class SpanishProgressTracker:
    def __init__(self, progress_file="spanish_progress.json"):
        self.progress_file = progress_file
        self.load_progress()
    
    def load_progress(self):
        """Load progress data"""
        try:
            with open(self.progress_file, 'r') as f:
                self.progress = json.load(f)
        except FileNotFoundError:
            self.progress = {
                "start_date": datetime.now().isoformat(),
                "current_lesson": 1,
                "words_learned": [],
                "daily_sessions": [],
                "retention_scores": {},
                "conversation_minutes": 0,
                "milestones_achieved": []
            }
    
    def save_progress(self):
        """Save progress data"""
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)
    
    def log_session(self, words_practiced=0, conversation_minutes=0, confidence_score=0):
        """Log a learning session"""
        session = {
            "date": datetime.now().isoformat(),
            "words_practiced": words_practiced,
            "conversation_minutes": conversation_minutes,
            "confidence_score": confidence_score
        }
        
        self.progress["daily_sessions"].append(session)
        self.progress["conversation_minutes"] += conversation_minutes
        self.save_progress()
    
    def add_vocabulary(self, word, confidence=0.5):
        """Add new vocabulary with confidence score"""
        vocab_entry = {
            "word": word,
            "learned_date": datetime.now().isoformat(),
            "confidence": confidence,
            "review_count": 0,
            "last_reviewed": None
        }
        
        self.progress["words_learned"].append(vocab_entry)
        self.save_progress()
    
    def update_retention(self, word, correct):
        """Update retention score for a word"""
        if word not in self.progress["retention_scores"]:
            self.progress["retention_scores"][word] = {"correct": 0, "attempts": 0}
        
        self.progress["retention_scores"][word]["attempts"] += 1
        if correct:
            self.progress["retention_scores"][word]["correct"] += 1
        
        self.save_progress()
    
    def check_milestones(self):
        """Check and record achieved milestones"""
        milestones = [
            {"name": "First Week", "condition": lambda: self.days_studying() >= 7},
            {"name": "50 Words", "condition": lambda: len(self.progress["words_learned"]) >= 50},
            {"name": "100 Words", "condition": lambda: len(self.progress["words_learned"]) >= 100},
            {"name": "First Conversation", "condition": lambda: self.progress["conversation_minutes"] >= 5},
            {"name": "30 Day Streak", "condition": lambda: self.days_studying() >= 30},
            {"name": "Business Ready", "condition": lambda: self.progress["current_lesson"] >= 21},
        ]
        
        achieved = []
        for milestone in milestones:
            if milestone["condition"]() and milestone["name"] not in self.progress["milestones_achieved"]:
                self.progress["milestones_achieved"].append(milestone["name"])
                achieved.append(milestone["name"])
        
        if achieved:
            self.save_progress()
        
        return achieved
    
    def days_studying(self):
        """Calculate days since starting"""
        start = datetime.fromisoformat(self.progress["start_date"].replace('Z', '+00:00'))
        return (datetime.now() - start.replace(tzinfo=None)).days
    
    def generate_report(self):
        """Generate comprehensive progress report"""
        total_words = len(self.progress["words_learned"])
        days_active = len(self.progress["daily_sessions"])
        avg_retention = self.calculate_average_retention()
        
        report = f"""
🇪🇸 SPANISH LEARNING PROGRESS REPORT
=====================================

📊 OVERVIEW
-----------
• Days studying: {self.days_studying()}
• Active learning days: {days_active}
• Current lesson: {self.progress['current_lesson']}
• Total vocabulary: {total_words} words
• Conversation practice: {self.progress['conversation_minutes']} minutes
• Average retention: {avg_retention:.1%}

🎯 MILESTONES ACHIEVED
----------------------
{chr(10).join(f"✅ {milestone}" for milestone in self.progress['milestones_achieved'])}

📈 RECENT ACTIVITY (Last 7 Days)
---------------------------------
{self.recent_activity_summary()}

🎓 NEXT GOALS
-------------
{self.next_goals()}

💪 RECOMMENDATIONS
------------------
{self.get_recommendations()}
"""
        return report
    
    def calculate_average_retention(self):
        """Calculate average retention rate"""
        if not self.progress["retention_scores"]:
            return 0
        
        total_correct = sum(score["correct"] for score in self.progress["retention_scores"].values())
        total_attempts = sum(score["attempts"] for score in self.progress["retention_scores"].values())
        
        return total_correct / total_attempts if total_attempts > 0 else 0
    
    def recent_activity_summary(self):
        """Summarize recent activity"""
        recent_sessions = [
            session for session in self.progress["daily_sessions"]
            if datetime.fromisoformat(session["date"]) > datetime.now() - timedelta(days=7)
        ]
        
        if not recent_sessions:
            return "No recent activity"
        
        total_words = sum(session["words_practiced"] for session in recent_sessions)
        total_conversation = sum(session["conversation_minutes"] for session in recent_sessions)
        
        return f"• {len(recent_sessions)} sessions\n• {total_words} words practiced\n• {total_conversation} minutes of conversation"
    
    def next_goals(self):
        """Suggest next goals based on progress"""
        goals = []
        
        if self.progress["current_lesson"] < 10:
            goals.append("Complete foundation lessons (1-10)")
        elif self.progress["current_lesson"] < 21:
            goals.append("Master basic conversation skills")
        elif self.progress["current_lesson"] < 40:
            goals.append("Develop business Spanish proficiency")
        else:
            goals.append("Achieve advanced fluency")
        
        if len(self.progress["words_learned"]) < 100:
            goals.append(f"Learn {100 - len(self.progress['words_learned'])} more vocabulary words")
        
        if self.progress["conversation_minutes"] < 60:
            goals.append("Practice 60 minutes of conversation")
        
        return chr(10).join(f"• {goal}" for goal in goals[:3])
    
    def get_recommendations(self):
        """Get personalized recommendations"""
        recommendations = []
        
        # Check consistency
        if len(self.progress["daily_sessions"]) < self.days_studying() * 0.8:
            recommendations.append("Try to practice more consistently - daily practice yields better results")
        
        # Check retention
        retention = self.calculate_average_retention()
        if retention < 0.7:
            recommendations.append("Focus on reviewing previous vocabulary - spaced repetition helps retention")
        
        # Check conversation practice
        if self.progress["conversation_minutes"] < self.days_studying() * 2:
            recommendations.append("Increase conversation practice - speaking builds confidence")
        
        if not recommendations:
            recommendations.append("Great progress! Keep up the consistent practice routine")
        
        return chr(10).join(f"• {rec}" for rec in recommendations[:3])
    
    def export_csv(self, filename="spanish_progress.csv"):
        """Export progress data to CSV"""
        import csv
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Date', 'Words Practiced', 'Conversation Minutes', 'Confidence Score'])
            
            for session in self.progress["daily_sessions"]:
                writer.writerow([
                    session["date"],
                    session["words_practiced"],
                    session["conversation_minutes"],
                    session.get("confidence_score", 0)
                ])
        
        print(f"Progress data exported to {filename}")

def main():
    """Generate and display progress report"""
    tracker = SpanishProgressTracker()
    
    # Check for new milestones
    new_milestones = tracker.check_milestones()
    if new_milestones:
        print("🎉 NEW MILESTONES ACHIEVED!")
        for milestone in new_milestones:
            print(f"✅ {milestone}")
        print()
    
    # Display full report
    report = tracker.generate_report()
    print(report)

if __name__ == "__main__":
    main()