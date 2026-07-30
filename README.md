# 🐾 AnimalCareAI

AI-powered Veterinary Management System built with Python, Streamlit, SQLAlchemy, SQLite, and Google Gemini.

AnimalCareAI is a modern platform designed to help veterinary clinics, hospitals, and pet owners manage animal medical records while leveraging Artificial Intelligence for image-based veterinary assistance.

---

# ✨ Features

## 👤 Owner Management

- Register pet owners
- Store contact information
- View owner profiles

---

## 🐶 Pet Management

- Register pets
- Species & breed support
- Medical information
- Weight, gender, age
- Owner relationships

---

## 📸 Pet Images

- Upload multiple images
- Store medical images
- Image categorization
- Image management

---

## 🤖 AI Veterinary Analysis

Powered by **Google Gemini**

The AI can:

- Analyze uploaded pet images
- Consider owner-reported symptoms
- Generate veterinary reports
- Estimate confidence level
- Store reports in the database

---

## 📋 AI Reports

Every analysis is saved with:

- Pet
- Image
- Symptoms
- AI model
- Confidence
- Report
- Date & time

---

# 🛠️ Technology Stack

- Python 3.12+
- Streamlit
- SQLAlchemy ORM
- SQLite
- Google Gemini API
- Pillow
- Python Dotenv

---

# 📁 Project Structure

```
AnimalCareAI/
│
├── ai/
│
├── database/
│
├── models/
│
├── pages/
│
├── scripts/
│
├── services/
│
├── uploads/
│
├── utils/
│
├── app.py
│
└── requirements.txt
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Elfadil94/AnimalCareAI.git
```

Enter the project

```bash
cd AnimalCareAI
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install packages

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

---

# 🔑 Environment Variables

Create a `.env` file.

Example

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

# 🗄️ Database

Create the database

```bash
python scripts/create_database.py
```

---

# 📸 AI Workflow

1. Register Owner
2. Register Pet
3. Upload Pet Image
4. Enter Symptoms
5. AI analyzes image
6. Save report
7. View previous reports

---

# 🎯 Future Roadmap

- User Authentication
- Role-based Permissions
- Veterinarian Dashboard
- Hospital Dashboard
- Appointment Scheduling
- Vaccination Tracking
- Medical History
- Prescription Management
- PDF Report Export
- Notifications
- Flutter Mobile App
- REST API (FastAPI)
- PostgreSQL
- Docker Deployment
- Cloud Hosting
- Multi-clinic Support

---

# 📱 Planned Mobile Applications

- Android
- iOS

---

# 🏥 Target Users

- Veterinary Clinics
- Veterinary Hospitals
- Animal Shelters
- Pet Owners

---

# 🤝 Contributing

Contributions are welcome.

Feel free to open Issues or submit Pull Requests.

---

# 📄 License

This project is currently under development.

License will be added before public release.

---

# 👨‍💻 Author

**Elfadil Elfatih**

GitHub:

https://github.com/Elfadil94

---

# ⭐ AnimalCareAI

Building the future of AI-powered veterinary healthcare.
