---
description: Execute a sub-milestone following the strict 6-phase protocol with approval gates
---

# Milestone Execution Workflow

**IMPORTANT:** This workflow MUST be followed for every sub-milestone (e.g., 1.1, 1.2, 2.1). Each sub-milestone is its own session - do NOT proceed to the next sub-milestone until this one is complete and summarized.

---

## Pre-Flight Checklist

Before starting ANY milestone work:

```
[ ] Identify the current sub-milestone from TASKS.md
[ ] Confirm with user: "We are starting sub-milestone X.X - [name]. Correct?"
[ ] Create/update task.md artifact in brain/ directory
```

---

## Phase 1: MILESTONE SELECTION

1. **Read TASKS.md** to find the current sub-milestone
2. **Extract ALL tasks** for that sub-milestone (copy the full checklist)
3. **Note any dependencies** on previous milestones
4. **Confirm with user** that this is the correct milestone to work on

**Output:** List of tasks for this sub-milestone

---

## Phase 2: CONTEXT GATHERING

Read these documents IN ORDER to understand the full context:

### Step 2.1: Read PRD.md
- Find sections relevant to the tasks
- Note acceptance criteria
- Note any UI/UX specifications
- Note priority levels (P0/P1/P2)

### Step 2.2: Read GEMINI.md
- Note technology constraints
- Note coding standards
- Note Islamic content handling rules
- Note security requirements

### Step 2.3: Read PLANNING.md
- Note architecture decisions
- Note package/dependency choices
- Note folder structure requirements
- Note testing strategy

### Step 2.4: Read brand-identity skill
- Check design-tokens.json for colors, fonts, spacing
- Check visual-guidelines.md for component specs
- Check tech-stack.md for library choices

**Output:** Compiled context notes in task.md artifact

---

## Phase 3: IMPLEMENTATION PLAN (🛑 APPROVAL GATE 1)

Create `implementation_plan.md` artifact with:

### 3.1 Goal Statement
- What this sub-milestone achieves
- Link to PRD sections

### 3.2 Task Breakdown
- Break each TASKS.md item into smaller, atomic steps
- Estimate complexity (S/M/L)
- Order by dependencies

### 3.3 Files to Create/Modify
List exact file paths:
```
[NEW] path/to/new/file.ts
[MODIFY] path/to/existing/file.ts  
[DELETE] path/to/remove/file.ts
```

### 3.4 External Dependencies
List EVERYTHING needed from user:
- [ ] API keys or credentials
- [ ] Design assets not in mockups
- [ ] Clarification on requirements
- [ ] Access to services
- [ ] Hardware/device for testing

### 3.5 Verification Plan
- What tests to run
- What to manually verify
- Acceptance criteria from PRD

### 3.6 Risks & Uncertainties
- Anything unclear
- Potential blockers
- Alternative approaches if blocked

---

**🛑 STOP: Request user approval of implementation plan before proceeding**

Use notify_user with:
- PathsToReview: [implementation_plan.md path]
- BlockedOnUser: true
- Message: Summary + specific questions

---

## Phase 4: EXECUTION

Only after plan approval:

1. **Follow the plan step-by-step**
2. **Update task.md** with progress:
   - `[ ]` = Not started
   - `[/]` = In progress
   - `[x]` = Complete
3. **When blocked:**
   - STOP immediately
   - Document what's blocking
   - Ask user for help
   - Do NOT guess or improvise
4. **Confirm external dependencies** as you need them (even if listed upfront)

### During Execution:
- Run linting/type-checks frequently
- Test incrementally
- Commit logical chunks (if git is set up)

---

## Phase 5: VERIFICATION (🛑 APPROVAL GATE 2)

### 5.1 Run Automated Checks
```bash
# For React Native
npm run lint
npm run typecheck
npm test

# For Python backend
flake8 app/
mypy app/
pytest tests/
```

### 5.2 Manual Verification
- Check against PRD acceptance criteria (list each one)
- Test on device/emulator if UI work
- Verify edge cases mentioned in PRD

### 5.3 Update TASKS.md
- Mark completed items with [x]
- Add any notes about partial completion
- Document any scope changes

---

**🛑 STOP: Request user verification before marking complete**

Use notify_user with:
- PathsToReview: [modified files, TASKS.md]
- BlockedOnUser: true
- Message: "Sub-milestone X.X verification - please review"

---

## Phase 6: SESSION SUMMARY

After user approval of verification:

### 6.1 Create/Update walkthrough.md
In brain/ artifacts directory:

```markdown
# Session Summary: Sub-Milestone X.X - [Name]

## What Was Done
- [List all completed tasks]

## How It Was Done
- [Key implementation decisions]
- [Libraries/patterns used]

## Why (Traceability)
- [Link to PRD sections]
- [Link to GEMINI.md rules followed]
- [Link to PLANNING.md decisions]

## Files Changed
- [List with brief description]

## Blockers for Next Milestone
- [Any issues to address]
- [Dependencies not yet available]

## Next Steps
- [What sub-milestone comes next]
- [Any prep needed]
```

### 6.2 Update SESSION_LOG.md
Append to project root `SESSION_LOG.md`:

```markdown
---
## [Date] - Sub-Milestone X.X: [Name]
**Status:** ✅ Complete | ⚠️ Partial | ❌ Blocked
**Tasks Completed:** X/Y
**Key Changes:** [1-2 sentence summary]
**Next:** Sub-Milestone X.Y
---
```

### 6.3 Final Confirmation
Notify user:
- "Sub-milestone X.X complete. Ready to start X.Y?"
- Do NOT auto-proceed to next milestone

---

## Quick Reference Card

```
┌────────────────────────────────────────┐
│  MILESTONE EXECUTION PROTOCOL          │
├────────────────────────────────────────┤
│  1. SELECT    → Read TASKS.md          │
│  2. GATHER    → Read PRD/GEMINI/PLAN   │
│  3. PLAN      → Create impl plan       │
│     🛑 APPROVAL GATE 1                 │
│  4. EXECUTE   → Follow plan exactly    │
│  5. VERIFY    → Test & check criteria  │
│     🛑 APPROVAL GATE 2                 │
│  6. SUMMARIZE → Write session log      │
│     ✅ ONLY THEN → Next milestone      │
└────────────────────────────────────────┘
```

---

## Anti-Patterns to Avoid

❌ Starting execution without reading all 4 docs  
❌ Skipping the implementation plan  
❌ Proceeding without user approval at gates  
❌ Guessing when blocked instead of asking  
❌ Moving to next milestone without summary  
❌ Modifying TASKS.md items without completing them  
❌ Drifting from the approved plan  

---

## Invoking This Workflow

User can trigger this workflow with:
- `/milestone` - Start the next pending sub-milestone
- `/milestone 1.3` - Start a specific sub-milestone
- `/milestone status` - Show current progress

Agent should auto-invoke this when:
- User says "let's start building"
- User says "continue with the next milestone"
- User references a specific TASKS.md item
