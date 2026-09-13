🎓 AI-Powered Student Performance Prediction System

Developed by Lavi Datar

An AI-powered web application designed to analyze student academic data, predict performance, identify academic risk, and provide meaningful insights through an interactive dashboard.

---

🚀 Live Demo

🌐 Live Application:
https://v0-ai-powered-student-performance-prediction.vercel.app/

---

📌 Project Overview

The AI-Powered Student Performance Prediction System is a modern web-based application that combines Artificial Intelligence, Machine Learning, academic analytics, and student management into one platform.

The system allows users to manage student academic information and use machine-learning-based predictions to understand expected performance, identify risk levels, analyze trends, and support better academic decisions.

---

🎯 Objectives

- Predict student academic performance using Machine Learning
- Identify students who may be at academic risk
- Analyze important academic factors
- Provide performance insights and trends
- Generate useful academic recommendations
- Maintain student and prediction history
- Present academic information through an interactive dashboard

---

✨ Key Features

🤖 AI-Powered Prediction

- Machine Learning-based student performance prediction
- Performance score prediction
- Risk-level identification
- Performance trend analysis
- Prediction confidence where supported
- Data-driven academic recommendations

👨‍🎓 Student Management

- Add students
- View student records
- Search students
- Filter student records
- View individual student details
- Update student information
- Delete student records
- Persistent student data

📊 Dashboard

- Total students analyzed
- Average predicted performance
- Students at risk
- Performance overview
- Interactive analytics
- Academic performance trends

📈 Analytics

- Student performance analysis
- Risk distribution
- Performance trends
- Academic factor analysis
- Interactive charts and visualizations

🔮 Prediction System

The prediction form uses academic information such as:

- Student Name
- Student ID
- Program
- Current GPA
- Attendance Rate
- Assignments Completed
- Study Hours per Week
- Previous Score

The system processes these inputs through the prediction pipeline and displays the resulting performance insights.

📑 Reports

The application includes report-generation functionality for:

- Cohort Performance Report
- Intervention Impact Report
- Academic Advisor Brief
- Student performance information
- Prediction results
- Academic analysis
- Recommendations

🌓 Dark & Light Mode

- Premium Dark Mode
- Professional Light Mode
- Instant theme switching
- Theme persistence
- Responsive theme support

---

🧠 Machine Learning Workflow

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

---

🛠️ Technology Stack

Frontend

- React
- Next.js
- TypeScript
- Tailwind CSS
- React Components
- Recharts
- Lucide Icons

Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite

Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

Reporting

- ReportLab

Deployment

- Vercel

---

🏗️ Project Structure

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

«Note: Update the structure above if the final GitHub repository has a different folder organization.»

---

📊 Academic Input Features

Feature| Description
Student ID| Unique student identifier
Program| Student's academic program
Current GPA| Current academic GPA
Attendance Rate| Percentage of attendance
Assignments Completed| Number of completed assignments
Study Hours| Weekly study hours
Previous Score| Previous academic score

---

🗄️ Data Persistence

The application uses a database to maintain student and prediction information.

Stored information can include:

- Student details
- Academic information
- Prediction results
- Risk levels
- Performance trends
- Prediction history
- Creation and update timestamps

Records remain available until they are explicitly deleted by the user.

---

🔐 Demo Access

For demonstration purposes:

Username: admin
Password: pass1234

«⚠️ Note: These credentials are intended for demonstration only. Do not use public demo credentials for sensitive or production data.»

---

💻 Installation

1. Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the Project

cd AI-Powered-Student-Performance-Prediction-System

3. Install Frontend Dependencies

Using pnpm:

pnpm install

Or using npm:

npm install

4. Install Backend Dependencies

pip install -r backend/requirements.txt

5. Start the Backend

uvicorn backend.main:app --reload

6. Start the Frontend

Using pnpm:

pnpm dev

Or using npm:

npm run dev

The application will then be available through the local development server.

---

📊 Machine Learning Model

The project uses a Machine Learning pipeline to analyze student academic information and generate performance predictions.

The ML workflow includes:

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

- Logistic Regression
- Random Forest
- Gradient Boosting

«Important: Final model performance metrics should be reported from actual evaluation results rather than hardcoded values.»

---

🎨 UI / Design

The application follows a modern AI/SaaS design approach featuring:

- Premium dark interface
- Professional light mode
- Responsive layout
- Modern typography
- Glass-style cards
- Interactive dashboards
- Data visualization
- Smooth animations
- Mobile-friendly interface
- AI-inspired visual elements

---

📸 Screenshots

🏠 Home Page

"Home Page" (screenshots/home.png)

📊 Dashboard

"Dashboard" (screenshots/dashboard.png)

🔮 Prediction

"Prediction" (screenshots/prediction.png)

👨‍🎓 Students

"Students" (screenshots/students.png)

📈 Analytics

"Analytics" (screenshots/analytics.png)

📑 Reports

"Reports" (screenshots/reports.png)

«Replace the screenshot paths above with the actual image locations in your repository.»

---

🔮 Future Enhancements

- Advanced Machine Learning models
- Deep Learning integration
- Automated intervention recommendations
- Student performance forecasting
- Email notifications
- Role-based authentication
- Cloud database integration
- Advanced academic analytics
- Automated model retraining
- Additional academic features

---

⚠️ Disclaimer

This application provides AI/ML-based estimates of student performance.

Predictions are not guaranteed outcomes and should not be used as the sole basis for academic decisions. The system is intended for educational, analytical, and demonstration purposes.

---

👨‍💻 Developer

Lavi Datar

B.Sc. Computer Science Graduate | MCA Student | Aspiring Software Developer

This project was designed and developed as an AI/ML-based academic project to explore student performance prediction, data analysis, Machine Learning, and modern web application development.

- 💻 GitHub: https://github.com/lavidatar
- 🔗 LinkedIn: https://linkedin.com/in/lavidatar
- 🌐 Portfolio: https://lavis-portfolio--lavidatar02.replit.app/

---

⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

📄 License

This project is created for educational, academic, and portfolio purposes.

© 2026 Lavi Datar. All rights reserved.
