# WhatsApp Groups Verification Checklist

## 🚨 **URGENT: MV Martech Group ID Conflict**

**Two different group IDs found for MV Martech team:**

### Option A: `120363357193603929@g.us`
- **Source:** People profiles (Pavel, Nicole, Alvin, Marisha, Monique)
- **Members:** 5 confirmed team members
- **Usage:** Listed in individual team member profiles

### Option B: `120363423218272168@g.us`  
- **Source:** Teams mapping + recent appreciation messages
- **Members:** Same team + Eliza
- **Usage:** Used for Pavel appreciation message (Feb 6, 2026)

## ✅ **Verification Process:**

**Step 1: Test Both Groups**
```bash
# Test Group A
message action=send channel=whatsapp target=120363357193603929@g.us message="Group verification test A"

# Test Group B  
message action=send channel=whatsapp target=120363423218272168@g.us message="Group verification test B"
```

**Step 2: Check Response**
- Which group receives the message successfully?
- Which group has active team members responding?

**Step 3: Update Master Registry**
- Mark correct group as `"status": "active"`
- Mark incorrect group as `"status": "inactive_duplicate"`
- Update all people profiles with correct group ID

## 🔍 **Other Groups to Verify:**

### Vibrantly Build Group: `120363421111503792@g.us`
- **Test:** Send message to confirm it's Vibrantly (not Longevity/Health)
- **Expected Response:** Euson Chew or Vibrantly team members

### Executive Group: `120363406637186264@g.us` 
- **Test:** Confirm Norman Noble is in this group
- **Expected Response:** Executive team members

## 📋 **Post-Verification Actions:**

1. **Update Master Registry** with verified group IDs
2. **Fix People Profiles** to use correct group IDs
3. **Update Appreciation System** to use verified groups
4. **Clean Up Old References** in memory files

## ⏰ **Timeline:**
- **Verification:** Immediate (next message opportunity)
- **Cleanup:** Within 24 hours of verification
- **Documentation:** Update master registry same day

---
*Created: 2026-02-06*  
*Priority: HIGH - Affects daily appreciation messages*