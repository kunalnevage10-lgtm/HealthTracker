# 🏥 HealthSync Pro: Personal Health & Activity Tracker

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Framework-Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/Database-SQLite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Architecture-MVC%20%2F%20OOP-FF6F00?style=for-the-badge" alt="Architecture" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</p>

**HealthSync Pro** is a modular, full-stack health intelligence web application designed for comprehensive daily metric tracking, biometric assessment, and lifestyle optimization. Built following the **Model-View-Controller (MVC)** architectural pattern and strict **Object-Oriented Programming (OOP)** database abstraction, it provides automated BMI categorization, intelligent hydration reminders, step goal tracking, and formatted clinical health summary reports.

---

## 🎯 Objective

Modern wellness applications often suffer from cluttered interfaces, bloated dependencies, and fragmented health logging.

**HealthSync Pro** solves this by delivering:
- **Unified Biometric Dashboard**: Real-time aggregation of daily steps, water intake, weight, height, and target goals.
- **Rule-Based Health Intelligence**: Automated calculation of Body Mass Index (BMI) and proactive contextual reminders (e.g., dehydration warnings when water intake falls below healthy thresholds).
- **OOP & Clean Code Principles**: Complete decoupling of SQL database queries from route handlers via an abstracted `DBManager` class.
- **Printable Clinical Summary**: Clean, formatted receipt-style health reports for personal record-keeping.

---

## ✨ Key Features

- **📊 Intelligent Biometric Computation**:
  - Automatically calculates **BMI** using $\text{BMI} = \frac{\text{Weight (kg)}}{\text{Height (m)}^2}$.
  - Dynamically categorizes health status: *Underweight*, *Normal Weight*, *Overweight*, or *Obese*.
- **💧 Smart Hydration & Step Alerts**:
  - Monitors real-time daily water consumption and triggers hydration reminder banners when intake drops below baseline.
  - Compares active step counts against customizable daily step targets.
- **🏗️ OOP Database Abstraction (`DBManager`)**:
  - Encapsulates all CRUD transactions within a dedicated `DBManager` class.
  - Automatically provisions multi-table relational schemas (`USER`, `LOGS`, `HEALTH_REPORT`) upon first startup.
- **📄 Printable Clinical Summary Report**:
  - Generates a monochromatic, receipt-style health summary sheet displaying current biometrics, milestones, and medical classifications.

---

## 🛠️ Tech Stack Used

| Layer | Technology | Function |
|---|---|---|
| **Backend Framework** | [Flask](https://palletsprojects.com/p/flask/) | Application routing, controller logic, and session handling |
| **Database Engine** | [SQLite3](https://www.sqlite.org/) | Embedded relational storage for user profiles and daily telemetry |
| **Architecture** | MVC & OOP | Separation of business logic, database manager, and UI presentation |
| **Frontend Templates** | HTML5, CSS3, Jinja2 | Responsive dashboard, setup cards, and health reports |

---

## 📁 Repository Structure

```plaintext
HealthTracker/
├── HealthTracker/
│   ├── app.py              # Flask server and controller routes
│   ├── database.py         # DBManager OOP class for SQLite operations
│   └── templates/
│       ├── index.html      # Primary user wellness dashboard
│       ├── login.html      # Biometric profile onboarding modal
│       └── report.html     # Monospaced printable health summary
└── README.md               # Project documentation and guide
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/kunalnevage10-lgtm/HealthTracker.git
cd HealthTracker
```

### 2. Set Up Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install flask
```

---

## 🚀 Usage Instructions

### 1. Run the Flask Web Application
```bash
cd HealthTracker
python app.py
```

### 2. Open the Dashboard
Open your web browser and navigate to:
```text
http://127.0.0.1:5000/
```

### 3. Application Navigation
- **Initial Setup**: If no user profile exists, visit `/login` to set up your profile (Name, Age, Weight in kg, Height in meters, Daily Step Goal).
- **Log Daily Activity**: Submit daily steps and water intake (Liters) directly from the dashboard card.
- **Generate Report**: Navigate to the **View Health Report** button to view and print your clinical summary.

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).
