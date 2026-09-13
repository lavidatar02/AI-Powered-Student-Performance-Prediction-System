# 🎓 AI-Powered Student Performance Prediction System

### Developed by Lavi Datar

An AI-powered web application designed to analyze student academic data, predict performance, identify academic risk, and provide meaningful insights through an interactive dashboard.

---

## 🚀 Live Demo

🌐 **Live Application:**
https://v0-ai-powered-student-performance-prediction.vercel.app/

---

## 📌 About the Project

The **AI-Powered Student Performance Prediction System** is a modern web-based application that combines **Machine Learning, academic analytics, student management, and automated reporting** into one platform.

The system allows users to manage student academic information and analyze factors such as GPA, attendance, assignments, study hours, and previous scores. The prediction pipeline processes the available academic data and provides performance-related insights, risk levels, trends, and recommendations.

---

## 🎯 Objectives

* Predict student academic performance using Machine Learning
* Identify students who may be at academic risk
* Analyze important academic factors
* Identify performance trends
* Provide meaningful academic insights
* Generate data-driven recommendations
* Maintain student and prediction history
* Provide reports for academic analysis
* Present information through an interactive dashboard

---

## ✨ Key Features

### 🤖 AI-Powered Prediction

* Machine Learning-based student performance prediction
* Performance score prediction
* Risk-level identification
* Performance trend analysis
* Prediction confidence where supported
* Data-driven recommendations

### 👨‍🎓 Student Management

* Add new students
* View student records
* Search students
* Filter student records
* View individual student details
* Update student information
* Delete student records
* Persistent student data

### 📊 Interactive Dashboard

* Total students analyzed
* Average predicted performance
* Students at risk
* Performance overview
* Academic performance trends
* Interactive charts and visualizations
* Key academic insights

### 📈 Analytics

* Student performance analysis
* Risk distribution
* Performance trends
* Academic factor analysis
* Interactive data visualization
* Student-level insights

### 🔮 Prediction System

The prediction system can use academic information such as:

* Student Name
* Student ID
* Program
* Current GPA
* Attendance Rate
* Assignments Completed
* Study Hours per Week
* Previous Score

The submitted information is processed through the prediction pipeline to generate performance-related results and insights.

### 📑 Reports

The application provides report-generation functionality for academic analysis, including:

* Cohort Performance Report
* Intervention Impact Report
* Academic Advisor Brief
* Student prediction information
* Performance analysis
* Academic recommendations

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
Academic Insights
        ↓
Recommendations
        ↓
Dashboard & Reports
```

---

## 📊 Academic Input Features

| Feature               | Description                     |
| --------------------- | ------------------------------- |
| Student ID            | Unique student identifier       |
| Program               | Student's academic program      |
| Current GPA           | Current academic GPA            |
| Attendance Rate       | Student attendance percentage   |
| Assignments Completed | Number of completed assignments |
| Study Hours           | Weekly study hours              |
| Previous Score        | Previous academic score         |

---

## 🛠️ Technology Stack

### Frontend

* React
* Next.js
* TypeScript
* Tailwind CSS
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

> **Note:** Update the structure above if the final repository organization is different.

---

## 🗄️ Data Persistence

The application uses **SQLite with SQLAlchemy** for persistent data storage.

Stored information can include:

* Student details
* Academic information
* Prediction results
* Risk levels
* Performance trends
* Prediction history
* Creation and update timestamps

Student and prediction records remain available until they are explicitly deleted.

---

## 🧪 Machine Learning Pipeline

The Machine Learning workflow includes:

1. Dataset collection
2. Data cleaning
3. Missing-value handling
4. Feature preprocessing
5. Feature encoding/scaling where required
6. Train/test split
7. Model training
8. Model evaluation
9. Model selection
10. Model serialization using Joblib
11. Real-time prediction

Possible models evaluated during development may include:

* Logistic Regression
* Random Forest
* Gradient Boosting

> **Note:** Final model metrics should be reported using actual evaluation results rather than hardcoded values.

---

## 🎨 UI & Design

The application follows a modern **AI/SaaS design approach** featuring:

* Premium dark interface
* Professional light mode
* Responsive layout
* Modern typography
* Glass-style cards
* Interactive dashboards
* Data visualization
* Smooth animations
* Mobile-friendly interface
* AI-inspired visual elements

---

## 🔐 Demo Access

For demonstration purposes:

```text
Username: admin
Password: pass1234
```

> ⚠️ These credentials are intended for demonstration only. Do not use public demo credentials for sensitive or production data.

---

## 💻 Installation & Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project

```bash
cd AI-Powered-Student-Performance-Prediction-System
```

### 3. Install Frontend Dependencies

Using pnpm:

```bash
pnpm install
```

Or using npm:

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

Using pnpm:

```bash
pnpm dev
```

Or using npm:

```bash
npm run dev
```

The application will then be available through the local development server.

---

## 📸 Screenshots

### 🏠 Home Page

![Home Page_alt](https://github.com/lavidatar02/AI-Powered-Student-Performance-Prediction-System/blob/main/01_home_page.png?raw=true)

### 📊 Dashboard

![Dashboard_alt](https://github.com/lavidatar02/AI-Powered-Student-Performance-Prediction-System/blob/main/02_dashboard.png?raw=true)

### 🔮 Prediction

![Prediction_alt](https://github.com/lavidatar02/AI-Powered-Student-Performance-Prediction-System/blob/main/03_prediction.png?raw=true)

### 👨‍🎓 Students

![Students](screenshots/students.png)

### 📈 Analytics

![Analytics](screenshots/analytics.png)

### 📑 Reports

![Reports](screenshots/reports.png)


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
* Additional academic features

---

## ⚠️ Disclaimer

This application provides **AI/ML-based estimates** of student performance.

Predictions are not guaranteed outcomes and should not be used as the sole basis for academic decisions. The system is intended for **educational, analytical, and demonstration purposes**.

---

## 👨‍💻 Developer

### Lavi Datar

**B.Sc. Computer Science Graduate | MCA Student | Aspiring Software Developer**

This project was designed and developed as an AI/ML-based academic project to explore **student performance prediction, data analysis, Machine Learning, and modern web application development**.

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is created for **educational, academic, and portfolio purposes**.

© 2026 **Lavi Datar**. All rights reserved.
