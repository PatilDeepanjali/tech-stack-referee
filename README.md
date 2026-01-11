# Tech Stack Referee ⚖️

A decision-support web tool that compares **MERN Stack** and **Django + PostgreSQL** based on user constraints and explains trade-offs instead of giving a single answer.

Built for **Kiro Heroes Challenge – Week 6 ("The Referee")**  
Part of **AI for Bharat (Powered by AWS)** organized by **Team Hack2skill**

---

##  Problem

Students and developers often ask:

> *"Which tech stack is best?"*

But the right choice depends on:
- Programming background
- Time constraints
- Budget
- Career goals

There is **no single best answer**.

---

##  Solution

**Tech Stack Referee** acts like a mentor:

- Collects user constraints
- Scores both stacks
- Explains pros & cons
- Shows confidence level
- Provides *what-if* scenarios
- Gives a **balanced verdict**

>  No absolute recommendations. Only context-aware guidance.

---

##  Tech Stack

- Python (Flask backend)
- HTML / CSS / JavaScript (frontend)
- Kiro (agent steering workflow)

---

##  Project Structure

tech-stack-referee/
.kiro/ workflow.yaml
referee/
 compare.py
 explain.py
web/
 index.html
 script.js
 styles.css
app.py
README.md
docs/
 blog_draft.md


---

##  How to Run Locally

### 1. Install dependencies
### 2. Run the app

pip install flask

### 2. Run the app
python app.py

### 3. Open browser
http://127.0.0.1:5000

### Features

- Rule-based scoring system

- Confidence meter

- Trade-off comparison table

- "What-if" scenario analysis

- Agent steering via Kiro

### Author

### Deepanjali Patil
Participant – Kiro Heroes Challenge (Week 6)

Links

Blog: (Add after publishing)

GitHub: (This repository)


### Acknowledgements

### Thanks to: 
- AI for Bharat
- AWS
- Team Hack2skill
- Kiro
