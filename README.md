# 🎓 AI-Powered Student Performance Prediction System

### Developed by Lavi Datar

An AI-powered student performance prediction system designed to analyze academic data, predict student performance, identify academic risk, and provide meaningful insights through an interactive dashboard.

## 🚀 Project Overview

**AI-Powered Student Performance Prediction System** is a modern web-based application that combines **Artificial Intelligence, Machine Learning, academic analytics, and student management** into one platform.

The system allows users to manage student academic information and use machine-learning-based predictions to understand expected performance, identify risk levels, analyze trends, and support better academic decisions.

### 🎯 Objectives

* Predict student academic performance using Machine Learning
* Identify students who may be at academic risk
* Analyze important academic factors
* Provide performance insights and trends
* Generate useful academic recommendations
* Maintain student and prediction history
* Present information through an interactive dashboard

---

## ✨ Key Features

### 🤖 AI-Powered Prediction

* Machine Learning-based student performance prediction
* Performance score prediction
* Risk-level identification
* Performance trend analysis
* Prediction confidence where supported
* Data-driven academic recommendations

### 👨‍🎓 Student Management

* Add students
* View student records
* Search students
* Filter student records
* View student details
* Update student information
* Delete student records
* Persistent student data

### 📊 Dashboard

* Total students analyzed
* Average predicted performance
* Students at risk
* Performance overview
* Interactive analytics
* Academic performance trends

### 📈 Analytics

* Student performance analysis
* Risk distribution
* Performance trends
* Academic factor analysis
* Interactive charts and visualizations

### 🔮 Prediction System

The prediction form uses academic information such as:

* Student Name
* Student ID
* Program
* Current GPA
* Attendance Rate
* Assignments Completed
* Study Hours per Week
* Previous Score

The system processes these inputs through the prediction pipeline and displays the resulting performance insights.

### 📑 Reports

The application includes report-generation functionality for:

* Cohort Performance Report
* Intervention Impact Report
* Academic Advisor Brief
* Student performance information
* Prediction results
* Academic analysis
* Recommendations

### 🌓 Dark & Light Mode

* Premium Dark Mode
* Professional Light Mode
* Instant theme switching
* Theme persistence
* Responsive theme support

---

## 🧠 Machine Learning Workflow

```text
Student Academic Data
        ↓
Data Validation
        ↓
Data Preprocessing
        ↓
Feature Processing
        ↓
Machine Learning Model
        ↓
Performance Prediction
        ↓
Risk / Performance Analysis
        ↓
Recommendations
        ↓
Dashboard & Reports
```

---

## 🛠️ Technology Stack

### Frontend

* React
* Next.js
* TypeScript
* Tailwind CSS
* React Components
* Recharts
* Lucide Icons

### Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib

### Reporting

* ReportLab

### Deployment

* Vercel

---

## 🏗️ Project Structure

```text
AI-Powered-Student-Performance-Prediction-System/
│
├── app/
│   ├── ...
│
├── backend/
│   ├── api/
│   ├── database/
│   ├── ml/
│   ├── main.py
│   ├── schemas.py
│   └── requirements.txt
│
├── components/
│   ├── ...
│
├── lib/
│   ├── ...
│
├── public/
│   ├── ...
│
├── ui/
│   ├── ...
│
├── package.json
├── pnpm-lock.yaml
├── pnpm-workspace.yaml
├── tsconfig.json
├── postcss.config.*
├── next.config.*
├── .gitignore
└── README.md
```

> The structure above should be adjusted if your final repository has a different folder organization.

---

## 📊 Academic Input Features

| Feature               | Description                     |
| --------------------- | ------------------------------- |
| Student ID            | Unique student identifier       |
| Program               | Student's academic program      |
| Current GPA           | Current academic GPA            |
| Attendance Rate       | Percentage of attendance        |
| Assignments Completed | Number of completed assignments |
| Study Hours           | Weekly study hours              |
| Previous Score        | Previous academic score         |

---

## 🗄️ Data Persistence

The application is designed to maintain student and prediction information using a database.

Stored information can include:

* Student details
* Academic information
* Prediction results
* Risk levels
* Performance trends
* Prediction history
* Creation/update timestamps

Records remain available until they are explicitly deleted by the user.

---

## 🔐 Demo Access

For demonstration purposes:

```text
Username: admin
Password: pass1234
```

> ⚠️ These credentials are intended for demonstration only. Do not use public demo credentials for sensitive or production data.

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project

```bash
cd AI-Powered-Student-Performance-Prediction-System
```

### 3. Install Frontend Dependencies

```bash
pnpm install
```

Or:

```bash
npm install
```

### 4. Install Backend Dependencies

```bash
pip install -r backend/requirements.txt
```

### 5. Start the Backend

```bash
uvicorn backend.main:app --reload
```

### 6. Start the Frontend

```bash
pnpm dev
```

Or:

```bash
npm run dev
```

---

## 📸 Screenshots

### 🏠 Home Page

Add your homepage screenshot:

```text
screenshots/home.png
```

### 📊 Dashboard

```text
screenshots/dashboard.png
```

### 🔮 Prediction

```text
screenshots/prediction.png
```

### 👨‍🎓 Students

```text
screenshots/students.png
```

### 📈 Analytics

```text
screenshots/analytics.png
```

### 📑 Reports

```text
screenshots/reports.png
```

---

## 🔮 Future Enhancements

* Advanced Machine Learning models
* Deep Learning integration
* Automated intervention recommendations
* Student performance forecasting
* Email notifications
* Role-based authentication
* Cloud database integration
* Advanced academic analytics
* Automated model retraining
* More student academic features

---

## ⚠️ Disclaimer

This application provides **AI/ML-based estimates** of student performance.

Predictions are not guaranteed outcomes and should not be used as the sole basis for academic decisions. The system is intended for educational, analytical, and demonstration purposes.

---

## 👨‍💻 Developer

### Lavi Datar

**B.Sc. Computer Science Graduate | MCA Student | Aspiring Software Developer**

This project was designed and developed as an AI/ML-based academic project to explore student performance prediction, data analysis, and modern web application development.

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is created for **educational, academic, and portfolio purposes**.

© 2026 **Lavi Datar**. All rights reserved.
