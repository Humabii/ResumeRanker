# 🤖 AI-Based Resume Screening and Candidate Ranking System

An intelligent yet simple **resume screening and candidate ranking system** built by **Huma Bi** using Python. The system automatically reads PDF resumes, checks required skills, compares candidates with a job description using a lightweight AI model, calculates a final suitability score, stores the results in MySQL, and ranks candidates automatically.

The project is designed to demonstrate how **Artificial Intelligence, data processing, and database technology** can be combined to improve the recruitment process.

---

## 📌 Project Overview

Recruiters can receive hundreds of resumes for a single job opening. Manually reviewing every resume is time-consuming and may result in qualified candidates being overlooked.

This project automates the **initial screening stage** of recruitment.

The system:

1. Takes a job description and required skills.
2. Reads multiple PDF resumes.
3. Extracts text from each resume.
4. Checks for required skills.
5. Uses AI to compare the resume with the job description.
6. Calculates a final candidate score.
7. Stores the results in MySQL.
8. Ranks candidates from highest to lowest score.
9. Can export the results to Excel.

> **Important:** The system is designed to assist recruiters, not replace human decision-making.

---

## 🎯 Objectives

* Automate the initial resume screening process.
* Reduce repetitive manual work for recruiters.
* Identify candidates with relevant technical skills.
* Use lightweight AI for semantic resume-job matching.
* Rank candidates based on suitability.
* Store candidate evaluation results in a database.
* Provide an easy-to-understand recruitment workflow.

---

## ⚙️ How It Works

```text
             JOB DESCRIPTION
                    │
                    ▼
             PDF RESUMES
                    │
                    ▼
          ┌──────────────────┐
          │ Extract PDF Text  │
          │    pdfplumber     │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │  Skill Matching   │
          │      70%          │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │   AI Similarity   │
          │       30%         │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │  Final Score      │
          └────────┬─────────┘
                   │
                   ▼
             MySQL Database
                   │
                   ▼
          Candidate Ranking
                   │
                   ▼
             Excel Report
```

---

## 🧠 AI Component

The project uses the pre-trained:

**Sentence Transformer — ****`all-MiniLM-L6-v2`**

The model converts the resume and job description into numerical representations called **embeddings**.

The system then uses **cosine similarity** to estimate how closely the resume matches the job description.

For example:

```text
Job Description:
Python developer with MySQL and data analysis experience

Resume:
Software developer experienced in Python, SQL databases
and Pandas-based data analysis
```

Even when the wording isn't exactly the same, the AI can recognize that the two pieces of text are semantically related.

### Why use only a small amount of AI?

The project intentionally keeps AI usage limited.

Traditional programming handles:

* PDF extraction
* Skill detection
* Score calculation
* Database operations
* Candidate ranking
* Excel export

AI is mainly used for:

**Semantic similarity between the resume and job description.**

This makes the project easier to understand, maintain, and explain during an academic presentation or viva.

---

## 📊 Candidate Scoring

The final candidate score is calculated using two components:

### Skill Score — 70%

Required skills are checked against the resume.

For example, if the required skills are:

```text
Python
MySQL
Pandas
HTML
CSS
JavaScript
```

and a candidate has:

```text
Python
MySQL
Pandas
HTML
```

then:

```text
4 / 6 × 100 = 66.67%
```

### AI Similarity — 30%

The AI model calculates the semantic similarity between the resume and job description.

### Final Score

```text
Final Score =
(0.70 × Skill Score) +
(0.30 × AI Similarity)
```

Example:

```text
Skill Score = 80
AI Score    = 90

Final Score =
(0.70 × 80) + (0.30 × 90)

= 56 + 27

= 83/100
```

---

## ✨ Features

### 📄 Automatic Resume Reading

Reads text from PDF resumes using `pdfplumber`.

### 🔎 Skill Detection

Checks whether required skills appear in candidate resumes.

### 🧠 AI-Based Matching

Uses Sentence Transformers to compare resume and job-description meaning.

### 🏆 Candidate Ranking

Automatically sorts candidates according to their final scores.

### 🗄️ MySQL Database

Stores candidate names and screening scores.

### 📊 Excel Export

Results can be exported for further HR analysis.

### ⚡ Batch Screening

Multiple resumes can be processed instead of screening candidates individually.

### 🎯 Simple Scoring System

The 70/30 scoring model makes the ranking easy to understand.

---

## 🛠️ Technology Stack

| Technology            | Purpose                       |
| --------------------- | ----------------------------- |
| Python                | Main programming language     |
| pdfplumber            | Extract text from PDF resumes |
| Sentence Transformers | AI semantic similarity        |
| Scikit-learn          | Cosine similarity             |
| Pandas                | Data processing and ranking   |
| MySQL                 | Database storage              |
| OpenPyXL              | Excel report generation       |

---

## 📁 Suggested Project Structure

```text
resume-screening-system/
│
├── resumes/
│   ├── candidate1.pdf
│   ├── candidate2.pdf
│   └── ...
│
├── screening.py
├── database.py
├── main.py
├── config.py
├── requirements.txt
├── candidates.sql
├── README.md
└── output/
    └── candidate_ranking.xlsx
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/resume-screening-system.git
```

Move into the project directory:

```bash
cd resume-screening-system
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install the main libraries:

```bash
pip install pdfplumber sentence-transformers scikit-learn pandas mysql-connector-python openpyxl
```

---

## 🗄️ MySQL Setup

Create the database using the provided SQL file:

```bash
mysql -u root -p
```

Then:

```sql
SOURCE candidates.sql;
```

Or open `candidates.sql` in **MySQL Workbench** and execute it.

The database should contain:

```text
resume_db
└── candidates
    ├── id
    ├── name
    ├── skill_score
    ├── ai_score
    └── final_score
```

---

## 🔐 Database Configuration

Update your database configuration:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_PASSWORD",
    "database": "resume_db"
}
```

For a real deployment, database credentials should be stored in environment variables rather than directly inside the source code.

---

## ▶️ Usage

### Step 1

Add candidate PDF resumes to the resume folder.

```text
resumes/
├── Ali_Khan.pdf
├── Sara_Ahmed.pdf
├── Rahul_Verma.pdf
└── ...
```

### Step 2

Provide the job description.

Example:

```text
We are looking for a Python developer with experience
in MySQL, Pandas, HTML, CSS and JavaScript.
```

### Step 3

Run the application:

```bash
python main.py
```

### Step 4

The system processes each resume.

### Step 5

The candidate scores are stored in MySQL and candidates are ranked according to their final score.

Example:

| Rank | Candidate   | Skill Score | AI Score | Final Score |
| ---: | ----------- | ----------: | -------: | ----------: |
|    1 | Ali Khan    |         100 |       91 |        97.3 |
|    2 | David Lee   |          83 |       88 |        84.5 |
|    3 | Rahul Verma |          67 |       90 |        73.9 |
|    4 | Sara Ahmed  |          67 |       78 |        70.3 |

*Example output only.*

---

## 🧪 Testing

The project can be tested using multiple resumes with different skill combinations.

For example:

### Strong Candidate

```text
Python ✓
MySQL ✓
Pandas ✓
HTML ✓
CSS ✓
JavaScript ✓
```

Expected result:

**High ranking**

### Moderate Candidate

```text
Python ✓
MySQL ✓
Pandas ✓
HTML ✗
CSS ✗
JavaScript ✗
```

Expected result:

**Medium ranking**

### Unrelated Candidate

```text
Photoshop
Illustrator
Figma
```

Expected result:

**Low ranking**

This allows the system to demonstrate meaningful differences between candidates.

---

## 🏢 Real-World Applications

The system can be used as a recruitment support tool for:

* Corporate HR departments
* Recruitment agencies
* Campus placement teams
* Internship selection
* Startup hiring
* Small and medium-sized businesses
* High-volume recruitment

---

## ✅ Advantages

### Time Saving

Recruiters don't have to manually read every resume before creating a shortlist.

### Consistent Screening

Every resume is evaluated using the same scoring methodology.

### Scalable

The same workflow can be applied to many resumes.

### Simple

The system uses a straightforward scoring model that is easy for HR users to understand.

### Cost Effective

It can be implemented using open-source Python libraries and a local MySQL database.

---

## ⚠️ Limitations

* The current skill matching relies heavily on predefined skills.
* Text-based PDFs work better than scanned documents.
* OCR would be required for image-based resumes.
* AI similarity does not guarantee that a candidate is actually qualified.
* The quality of the job description affects the AI score.
* The system should not make the final hiring decision independently.

---

## 🔮 Future Scope

The project can be expanded into a complete recruitment platform.

### 🌐 Web Application

A user-friendly interface can be created using **Streamlit**.

### 📷 OCR

OCR can allow the system to read scanned resumes.

### 📧 Email Automation

Candidates could automatically receive interview or rejection emails.

### 📊 HR Dashboard

Recruiters could view:

* Number of applicants
* Average score
* Top candidates
* Skill distribution
* Hiring trends

### 🎤 Interview Recommendation

The system could recommend candidates for interviews based on configurable screening criteria.

### 🧠 Advanced NLP

More sophisticated NLP techniques could improve resume parsing and skill recognition.

---

## 🔒 Responsible Use

This project should be treated as a **decision-support tool**, not an automated hiring authority.

Recruitment decisions can have significant consequences for applicants. Human recruiters should review shortlisted candidates and consider qualifications, experience, context, and other relevant factors before making a final decision.

---

## 📚 Academic Purpose

This project demonstrates the practical use of:

* Artificial Intelligence
* Natural Language Processing
* Python programming
* Database Management
* Data Processing
* Automation
* Recruitment Analytics

It is particularly suitable as an academic project for demonstrating how technology can solve a real-world HR problem.

---

## 👨‍💻 Author

**Huma Bi**

MBA Project

AI-Based Resume Screening and Candidate Ranking System

---

## ⭐ Project Highlights

```text
PDF Resume
     ↓
Text Extraction
     ↓
Skill Matching ──────┐
                     │
                     ▼
                 Final Score
                     ▲
                     │
AI Similarity ───────┘
     │
     ▼
MySQL Database
     │
     ▼
Candidate Ranking
     │
     ▼
Excel Report
```

### Built with Python + MySQL + Pandas + Lightweight AI
