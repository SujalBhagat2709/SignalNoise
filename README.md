# SignalNoise

SignalNoise is a small Python OOP project that helps separate **useful information from low-value information**.

The project is based on a common real-life problem:

> When too much information arrives at once, important information can get buried inside everything else.

SignalNoise gives each information item a score based on its relevance, urgency, reliability, and impact.

---

## Problem Statement

People and organizations constantly receive information:

* Messages
* Alerts
* Customer feedback
* Reports
* Observations
* Notifications
* System events
* Internal updates

The problem is that not every piece of information deserves the same amount of attention.

For example:

```text
"Five customers reported the same payment failure."
```

is likely more important than:

```text
"One user said the page feels slightly slow."
```

SignalNoise provides a structured way to distinguish between these kinds of information.

---

## Project Structure

```text
SignalNoise/
│
├── signal_noise.py
├── signal_noise_studio.py
├── README.md
└── .gitignore
```

---

## Features

### 1. Create Information Sources

A source represents where information is coming from.

Examples:

```text
Customer Feedback
System Alerts
Team Messages
Website Monitoring
Support Tickets
```

Each source contains:

* Source ID
* Name
* Description
* Information items

---

## 2. Add Information

Each information item contains:

* Content
* Category
* Relevance
* Urgency
* Reliability
* Impact

Example:

```text
Information:
Five customers reported the same payment error.

Category:
Customer Feedback

Relevance:
5/5

Urgency:
4/5

Reliability:
5/5

Impact:
5/5
```

---

## Signal Score

SignalNoise combines four dimensions:

```text
Relevance
Urgency
Reliability
Impact
```

The weighting is:

```text
Relevance   → 30%
Urgency     → 20%
Reliability → 25%
Impact      → 25%
```

The final score is normalized to a value between **0 and 100**.

---

## Classification

Information is classified into three categories:

```text
60–100
→ Signal

40–59
→ Needs Review

0–39
→ Noise
```

### Signal

Information currently appears useful enough to deserve attention.

### Needs Review

The information is borderline and should be examined before being ignored or prioritized.

### Noise

The information currently has relatively low decision value.

---

## Important Distinction

**Noise does not mean false.**

An item can be true but still have low value for the current decision.

Similarly:

**Signal does not automatically mean true.**

That is why reliability is one of the factors used in the score.

The classification represents **current decision value**, not absolute truth.

---

## High-Priority Signals

SignalNoise can identify information that is both:

* Highly relevant
* Highly urgent
* Strong enough to qualify as a signal

For example:

```text
Relevance: 5/5
Urgency: 5/5
Reliability: 4/5
Impact: 5/5
```

Such information deserves immediate attention.

---

## Average Signal Score

The system calculates the average score of all information within a source.

This provides a quick understanding of the overall quality/value of the incoming information.

Example:

```text
Average Score: 68.4
```

This means the source contains information with a relatively strong overall signal level.

---

## Signal Ratio

The system also calculates the percentage of information classified as Signal.

Example:

```text
Total Information: 20

Signals: 12

Signal Ratio:
60%
```

This helps understand how much of the incoming information is currently considered useful.

---

## Category Summary

Information can be grouped by category.

For example:

```text
Customer Feedback
System Alerts
Performance
Security
Operations
```

SignalNoise calculates the average score for each category.

This can reveal which categories tend to contain stronger signals.

---

## Example

Imagine a website monitoring source receives:

```text
1. CPU usage reached 95%
2. One visitor said the page looked slightly slow
3. Payment requests are failing
4. Server restarted successfully
5. Five customers reported checkout failure
```

The system evaluates each item using:

```text
Relevance
Urgency
Reliability
Impact
```

The resulting classifications could look like:

```text
CPU usage reached 95%
→ Signal

One visitor said the page looked slightly slow
→ Needs Review

Payment requests are failing
→ Signal

Server restarted successfully
→ Needs Review

Five customers reported checkout failure
→ High-Priority Signal
```

The exact classification depends on the ratings entered by the user.

---

## Typical Workflow

```text
Create Information Source
          ↓
Receive Information
          ↓
Rate Each Information Item
          ↓
Calculate Signal Score
          ↓
Classify Information
          ↓
Separate Signal / Noise / Review
          ↓
Prioritize Important Signals
          ↓
Make Better Decisions
```

---

## Real-World Applications

### Customer Support

Large numbers of customer messages can be evaluated based on relevance, urgency, reliability, and impact.

### System Monitoring

Technical events can be prioritized instead of treating every alert equally.

### Business Operations

Managers can separate important operational information from routine updates.

### Project Teams

Team members can identify which updates require immediate attention.

### Feedback Systems

Large amounts of feedback can be organized into stronger and weaker signals.

### Incident Response

During an incident, important observations can be prioritized while lower-value information is reviewed separately.

---

## OOP Concepts Used

### Class

```python
class SignalNoise:
```

The main class contains the application's business logic.

### Constructor

```python
def __init__(self):
```

Initializes the collection of information sources.

### Methods

Separate methods handle:

* Source creation
* Information creation
* Score calculation
* Classification
* Signal filtering
* Noise filtering
* Priority detection
* Category summaries
* Overall analysis
* Recommendations

### Encapsulation

Source and information data is maintained inside the `SignalNoise` object.

### Separation of Responsibilities

```text
signal_noise.py
        ↓
Core business logic

signal_noise_studio.py
        ↓
Interactive interface
```

This keeps the project organized and makes the core logic reusable.

---

## Why This Is More Than a Simple Filter

A simple filter might say:

```text
Important = Yes
Important = No
```

SignalNoise instead considers multiple dimensions:

```text
                Relevance
                    ↓
Urgency → Information ← Reliability
                    ↑
                  Impact
```

This makes the decision more nuanced.

An item may be:

* Highly relevant but unreliable
* Reliable but not urgent
* Urgent but low impact
* Highly impactful but poorly understood

The system makes these dimensions visible rather than treating all information equally.

---

## Limitations

This version is intentionally small.

It does not currently:

* Understand natural language automatically
* Verify whether information is true
* Learn user preferences
* Detect duplicate information
* Understand relationships between information items
* Persist information in a database
* Automatically collect information from external systems

The user supplies the ratings manually.

---

## Future Improvements

Possible future versions could add:

* Persistent database storage
* Duplicate detection
* Source reliability history
* Automatic priority adjustment
* Time-based signal changes
* Information clustering
* Natural-language classification
* Automatic relevance estimation
* Automatic urgency detection
* AI-assisted signal extraction
* AI-assisted summarization
* AI-assisted detection of important patterns

For example, a future version could receive hundreds of customer messages and automatically identify:

```text
Repeated Payment Failure
        ↓
High Frequency
        ↓
High Customer Impact
        ↓
Strong Signal
```

while separating unrelated comments for later review.

---

## Technologies

* Python 3
* Object-Oriented Programming
* Standard Python library only

No external packages are required.

---

## How to Run

Open a terminal inside the project folder and run:

```bash
python signal_noise_studio.py
```

---

## Studio Menu

```text
============================================================
SIGNALNOISE STUDIO
============================================================
1. Create Information Source
2. Add Information
3. View All Sources
4. View Source Details
5. Analyze Source
6. View Signals
7. View Noise
8. View High-Priority Information
9. Exit
============================================================
```

---

## .gitignore

```gitignore
__pycache__/
*.py[cod]
*.pyo
.venv/
venv/
env/
.idea/
.vscode/
.DS_Store
```

---

## Project Goal

SignalNoise demonstrates a practical information-management principle:

> **Not every piece of information deserves equal attention. Evaluate the signal, recognize the noise, review the uncertain items, and focus attention where it matters most.**
