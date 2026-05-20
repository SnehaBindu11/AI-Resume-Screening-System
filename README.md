# AI Resume Screening System

An AI-powered Resume Screening System developed using Python, NLP, Machine Learning, and Streamlit. This project automates resume analysis by comparing resumes with job descriptions, calculating similarity scores, identifying missing skills, and generating improvement recommendations.

---

# Live Demo

https://ai-resume-screening-system-dsezuv6htjmcpfncsrsrab.streamlit.app

---

# GitHub Repository

https://github.com/SnehaBindu11/AI-Resume-Screening-System

---

# Project Overview

Recruiters spend significant time manually screening resumes. This system simplifies the recruitment process by automatically analyzing resumes using Natural Language Processing (NLP) techniques and Machine Learning concepts.

The system:
- Extracts text from PDF resumes
- Cleans and preprocesses text
- Matches resumes with job descriptions
- Calculates similarity percentage
- Detects missing skills
- Provides recommendations for improvement
- Generates analysis reports

---

# Features

- Resume Upload in PDF Format
- Job Description Input
- NLP-based Resume Processing
- Resume-Job Matching Score
- Skill Gap Analysis
- Missing Skill Detection
- Recommendation Generation
- Interactive Streamlit User Interface
- PDF Report Generation

---

# Technologies Used

## Programming Language
- Python

## Frontend
- Streamlit

## Libraries
- NumPy
- Pandas
- Scikit-learn
- NLTK
- PDFPlumber
- ReportLab

---

# NLP Concepts Used

- Tokenization
- Stopword Removal
- Lemmatization
- Text Cleaning
- TF-IDF Vectorization
- Cosine Similarity

---

# Machine Learning Concepts Used

- Natural Language Processing (NLP)
- Text Vectorization
- Similarity Analysis
- Information Retrieval
- Feature Extraction

---

# Project Structure

```bash
AI-Resume-Screening-System/
│
├── app.py
├── extractor.py
├── preprocess.py
├── similarity.py
├── skill_matcher.py
├── recommendation.py
├── gap_analysis.py
├── report_generator.py
├── requirements.txt
├── README.md
│
├── resumes/
├── outputs/
└── job_descriptions/
```

---

# Working Process

## Step 1: Resume Upload
The user uploads a resume in PDF format.

## Step 2: Text Extraction
Text is extracted from the uploaded resume using PDFPlumber.

## Step 3: Text Preprocessing
The text is cleaned using NLP preprocessing techniques:
- Lowercasing
- Removing special characters
- Tokenization
- Stopword removal
- Lemmatization

## Step 4: Feature Extraction
TF-IDF Vectorization converts text into numerical vectors.

## Step 5: Similarity Calculation
Cosine Similarity compares the resume with the job description.

## Step 6: Skill Gap Analysis
The system identifies:
- Missing skills
- Required technologies
- Skill gaps

## Step 7: Recommendation Generation
The application provides suggestions for improving the resume and enhancing required skills.

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/SnehaBindu11/AI-Resume-Screening-System.git
```

## Navigate to the Project Folder

```bash
cd AI-Resume-Screening-System
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

---

# Sample Output

## Input
- Resume PDF
- Job Description

## Output
- Resume Match Score
- Missing Skills
- Skill Gap Analysis
- Improvement Recommendations

---

# Future Enhancements

- Deep Learning-based Resume Classification
- AI-powered Career Guidance
- Resume Ranking System
- Recruiter Dashboard
- Database Integration
- Multi-language Resume Support

---

# Learning Outcomes

Through this project, I learned:
- NLP preprocessing techniques
- Streamlit deployment
- Machine Learning workflows
- PDF text extraction
- GitHub project management
- Real-world AI application development

---

# Author

Sneha Bindu  
B.Tech – Artificial Intelligence & Data Science

GitHub:  
https://github.com/SnehaBindu11

---

# License

This project is licensed under the MIT License.
