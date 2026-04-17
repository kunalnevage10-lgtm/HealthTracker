HealthSync Pro: AI-Driven Personal Health Tracker
HealthSync Pro is a modular web application designed to track personal health metrics such as daily steps, water intake, and BMI. Built using a professional MVC (Model-View-Controller) architecture, the project emphasizes Object-Oriented Programming (OOP) principles and robust Database Management (DBMS).

🚀 Features
AI BMI Calculator: Automatically calculates Body Mass Index and provides health status categorization.

Smart Reminders: Logic-driven notifications that nudge users based on their remaining daily goals.

Automated Calorie Tracking: Integrated DBMS logic that converts step counts into calories burned using programmed algorithms.

Medical Report Generator: A dedicated module to generate and print comprehensive health summaries.

Virtual Group Sessions: Integrated Video Calling and Chat feature for group fitness discussions.

🛠️ Technical Stack
Backend: Python (Flask Framework)

Database: SQLite3

Frontend: HTML5, CSS3, JavaScript

Architecture: Object-Oriented Programming (OOP) & MVC

🏗️ System Architecture & OOP Implementation
This project is built with a strong focus on Object-Oriented Programming:

Encapsulation: All database operations are bundled within the DBManager class in database.py. This hides complex SQL queries from the application logic.

Abstraction: The app.py controller interacts with the database via method calls (e.g., db.get_today_stats()), abstracting away the underlying database schema.

Modularity: Separation of concerns between the Data Model (database.py), the User Interface (templates/), and the Logic Controller (app.py).
