# 11_Development-of-AI-Driven-Code-Reviewer
# Deployment Link : 
# Project Demo Video :

**Overview**
Reviewing code manually for correctness, coding style, and optimization is time-consuming, especially in academic or training environments where students submit large volumes of assignments. This project aims to build an AI-powered tool that automatically reviews student code submissions. The system will check for syntax errors, logical issues, coding style adherence, and suggest optimizations.
By combining AI models (GPT API) with Abstract Syntax Tree (AST) parsing, the solution will provide detailed feedback to help students improve their coding practices.

📌 Project Overview

The AI-Driven Code Review System is designed to assist developers by automating the code review process.Reviewing code manually for correctness, coding style, and optimization is time-consuming, especially in academic or training environments where students submit large volumes of assignments. Instead of relying solely on manual reviews, this platform provides:

 Instant code analysis

 Intelligent error detection

 Code quality scoring

 Optimization suggestions

 Review history tracking

The system is built using React (Frontend) and Flask (Backend) with AI-powered analysis.

 📌 System Architecture
 
React Frontend  →  Flask REST API  →  AI Analysis Engine  →  Database

🔹 Frontend

React.js

Embedded code editor

Dashboard for review tracking

🔹 Backend

Python

Flask REST API

AST-based static analysis

AI-based semantic evaluation

🔹 Database

PostgreSQL / NeonDB

Stores user data, submissions, scores, and feedback

 📌 Key Features  

 Instant Code Analysis

Users can submit code and receive immediate feedback.

🧠 Intelligent Error Detection

Syntax errors

Logical mistakes

Style violations

Best practice recommendations

📊 Quality Score Generation

Each submission is assigned a structured quality score based on:

Code structure

Complexity

Readability

Optimization level

📁 Review Dashboard

Tracks previous submissions

Displays performance trends

Stores feedback history

📌 Workflow

User submits code via frontend.

Backend API receives the request.

AST parser analyzes code structure.

AI module evaluates semantics and quality.

Issues and score are generated.

Results are stored in the database.

Feedback is displayed on dashboard.

📌 Installation & Setup

🔹 Clone the Repository

git clone https://github.com/your-username/ai-code-reviewer.git
cd ai-code-reviewer

🔹 Backend Setup (Flask)
cd backend
pip install -r requirements.txt
python app.py

Backend runs on:

http://localhost:5000

🔹 Frontend Setup (React)
cd frontend
npm install
npm start

Frontend runs on:

http://localhost:3000

🔐 Security Considerations

Input validation

No execution of user-submitted code (static analysis only)

Environment variable protection for API keys

Secure database connection

📈 Scalability

The system follows a modular architecture and can be scaled by:

Deploying multiple backend instances

Using cloud-based load balancing

Optimizing database indexing

📌 Limitations

Currently optimized for Python code

AI suggestions may require human validation

Does not replace human code reviewers (acts as assistant)

📌 Future Enhancements

Multi-language support

GitHub integration

CI/CD pipeline integration

Deep learning–based semantic analysis

Team collaboration features

👨‍💻 Tech Stack

Frontend: React.js

Backend: Flask (Python)

Database: PostgreSQL / NeonDB

AI Integration: OpenAI API / NLP-based analysis

Static Analysis: Python AST

📌 Learning Outcomes

Through this project, we gained experience in:

REST API development

AI integration in web systems

Database schema design

Frontend-backend integration

System scalability and security practices

📌 Conclusion

This project demonstrates how AI can be integrated into a structured enterprise-ready architecture to automate and enhance the code review process, improving development efficiency and software quality.
