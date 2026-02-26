# 11_Development-of-AI-Driven-Code-Reviewer
# Deployment Link : 
# Project Demo Video :

**Overview**
Reviewing code manually for correctness, coding style, and optimization is time-consuming, especially in academic or training environments where students submit large volumes of assignments. This project aims to build an AI-powered tool that automatically reviews student code submissions. The system will check for syntax errors, logical issues, coding style adherence, and suggest optimizations.
By combining AI models (GPT API) with Abstract Syntax Tree (AST) parsing, the solution will provide detailed feedback to help students improve their coding practices.

**Outcomes**
●  	Error Detection: Identify syntax and logical errors in code.
●  	Coding Style Review: Highlight deviations from coding standards (e.g., PEP8 for Python).
●  	Optimization Suggestions: Recommend improvements in performance and readability.
●  	Automated Feedback: Reduce manual evaluation effort for instructors.
●  	Student-Friendly Tool: Allow students to paste or upload code and instantly get actionable insights.

**Modules **
Module 1: Code Parsing & Preprocessing
●  	Accept student code in supported languages (start with Python).
●  	Parse code using AST (Abstract Syntax Tree).
●  	Preprocess code for formatting and readability.
Module 2: Error & Bug Detection
●  	Identify syntax errors and undefined variables.
●  	Detect logical issues (unused imports, unreachable code, infinite loops).
●  	Provide explanations for detected errors.
Module 3: Coding Style Analysis
●  	Check adherence to standard coding guidelines (PEP8).
●  	Highlight issues like improper indentation, naming conventions, or long functions.
●  	Score submissions based on style compliance.
Module 4: Optimization & Best Practice Suggestions
●  	Use GPT API to analyze code for efficiency and readability improvements.
●  	Suggest alternative data structures, algorithmic optimizations, and cleaner patterns.
●  	Provide before-and-after code snippets for learning.
Module 5: Web Application & Feedback Delivery
●  	Build a UI for students to upload/paste code.
●  	Display results as categorized feedback (errors, style, optimizations).
●  	Allow instructors to track submissions and feedback history.
