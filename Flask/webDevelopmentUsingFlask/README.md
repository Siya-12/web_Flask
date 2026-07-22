# 🚀 NLP APP

<div align="center">

### 🧠 An Interactive NLP Web Application built with Flask & NLP Cloud API

Perform **Named Entity Recognition (NER)**, **Sentiment Analysis**, and **Emotion/Text Analysis** through an intuitive web interface.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.x-black.svg)
![NLP](https://img.shields.io/badge/NLP-NLP%20Cloud-orange)
![License](https://img.shields.io/badge/License-MIT-green.svg)

</div>

---

# 📌 Overview

**NLP APP** is a Flask-based Natural Language Processing application that provides multiple NLP functionalities using the **NLP Cloud API**.

The application features a user authentication system and allows users to analyze text through a clean and user-friendly interface.

Users can:

- 🔍 Perform Named Entity Recognition (NER)
- 😊 Analyze Sentiment
- 📝 Generate Text Summary (Emotion Module)
- 🔐 Register & Login securely
- 🌐 Access all features from a responsive dashboard

---

# ✨ Features

### 👤 Authentication

- User Registration
- User Login
- Session Management

---

### 🔍 Named Entity Recognition (NER)

Extract entities such as:

- Person
- Organization
- Location
- Company
- Date
- Email
- Phone Number

using NLP Cloud's NER model.

---

### 😊 Sentiment Analysis

Analyze text and classify it into sentiment categories such as:

- Positive
- Neutral
- Negative

---

### 📝 Emotion/Text Analysis

Analyze the input text using NLP Cloud.

> **Note:** The current implementation uses the **Summarization API**. You can replace it with an Emotion Detection endpoint if desired.

---

# 🖥️ Tech Stack

## Backend

- Python
- Flask

## Frontend

- HTML
- CSS
- Bootstrap

## NLP

- NLP Cloud API

## Database

- TinyDB (JSON Database)

---

# 📂 Project Structure

```
NLP_APP/
│
├── templates/
│   ├── dashboard.html
│   ├── emotion.html
│   ├── login.html
│   ├── ner.html
│   └── registration.html
│
├── app.py
├── api.py
├── db.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/NLP_APP.git

cd NLP_APP
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Required Libraries

If you don't have a requirements.txt, install these manually.

```bash
pip install flask
pip install tinydb
pip install nlpcloud
pip install python-dotenv
```

---

# 🔑 Configure Environment Variables

Create a `.env` file in the project root.

```env
NLPCLOUD_API_KEY=YOUR_API_KEY
```

Never upload the `.env` file to GitHub.

---

# ▶️ Run the Application

```bash
python app.py
```

The application will run at

```
http://127.0.0.1:5000
```

---

# 📋 Dependencies

- Flask
- TinyDB
- NLP Cloud
- python-dotenv

---

# 🛠️ API Used

This project uses

### NLP Cloud API

https://nlpcloud.com/

Models Used

- lt_core_news_lg (NER)
- gpt-oss-120b (Sentiment)
- gpt-oss-120b (Summarization)

---

# 🖼️ Application Flow

```
User

↓

Login/Register

↓

Dashboard

↓

Choose NLP Task

↓

Enter Text

↓

NLP Cloud API

↓

Display Results
```

---

# 🔒 Security

- API Keys stored using `.env`
- `.env` excluded using `.gitignore`
- User credentials stored locally using TinyDB
- Sensitive files are not pushed to GitHub

---

# 📄 .gitignore

```gitignore
__pycache__/
*.py[cod]

venv/
.venv/

.env

mydb.json

.vscode/
.idea/

.DS_Store
Thumbs.db
```

---

# 🚀 Future Enhancements

- Voice Sentiment Analysis
- Text Translation
- Speech to Text
- Chatbot Integration
- Emotion Detection API
- Dark Mode
- User History
- PDF Text Analysis
- Multi-language Support

---

# 👨‍💻 Developed By

**Siya Agarwal**

MCA '27

National Institute of Technology Jamshedpur

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub!

---

<div align="center">

Made with ❤️ using Flask & NLP Cloud

</div>