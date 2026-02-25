# 🚗 AI Driver Safety System
### Real-Time Driver Drowsiness Detection using AI & Computer Vision

An **AI-powered Driver Safety System** that detects driver drowsiness in real time using **Computer Vision and Machine Learning**.  
The system monitors the driver's eyes through a webcam and detects fatigue using **Eye Aspect Ratio (EAR)** and **facial landmark analysis**.

Built with **FastAPI, OpenCV, and MediaPipe**, this project provides a **real-time monitoring dashboard with detection history logging.**

---

## 🌟 Project Highlights

✔ Real-time driver drowsiness detection  
✔ AI-based eye monitoring  
✔ Eye Aspect Ratio (EAR) calculation  
✔ Live webcam detection  
✔ Automatic drowsiness alerts  
✔ Detection history storage  
✔ FastAPI web interface  
✔ One-click automatic installation  
✔ One-click project run  
✔ Clean project architecture

---

## 🧠 Technologies Used

| Technology | Purpose |
|----------|---------|
| Python | Backend Development |
| FastAPI | Web Server |
| OpenCV | Image Processing |
| MediaPipe | Face Landmark Detection |
| SQLite | Database Storage |
| HTML/CSS | User Interface |
| JavaScript | Frontend Logic |

---

## 🏗 System Architecture
```
Web Browser
│
│
FastAPI Server (server.py)
│
│
AI Detection Module (drowsiness.py)
│
│
MediaPipe + OpenCV
│
│
SQLite Database
```
---

## 📂 Project Structure
```
🚗 AI_Driver_Safety_System
│
├── 🤖 ai/
│ └── drowsiness.py
│ AI logic for detecting driver drowsiness
│ using Eye Aspect Ratio (EAR)
│
├── 🗄 database/
│ └── database.py
│ Handles SQLite database creation
│ and history storage
│
├── 🧠 models/
│ └── shape_predictor_68_face_landmarks.dat
│ Pre-trained facial landmark model
│ used for eye detection
│
├── 🌐 templates/
│ ├── index.html
│ │ Main detection interface
│ │
│ └── history.html
│ Detection history dashboard
│
├── ⚙ server.py
│ FastAPI backend server
│ Controls AI detection and routes
│
├── 📦 requirements.txt
│ List of required Python libraries
│
└── ▶ run.bat
One-click project launcher
Automatically installs and runs server
```
---

## ⚙ Installation Guide

### 1️⃣ Clone Repository
```
https://github.com/priya-ak/AI-Driver-Safety-System.git
```
---

### 2️⃣ Open Project Folder
```
cd AI-Driver-Safety-System
```

---

### 3️⃣ Run Project

Double-click:
```
run.bat
```
This will automatically:

✔ Create virtual environment  
✔ Install dependencies  
✔ Start server

---

### 4️⃣ Open Browser
```
http://127.0.0.1:9777
```
## 🚀 How The System Works

1. Webcam captures driver's face
2. MediaPipe detects facial landmarks
3. Eye Aspect Ratio (EAR) is calculated
4. Eye closure duration is monitored
5. If threshold exceeded → Drowsiness Detected
6. Detection stored in database
7. Results displayed on web interface

---

## 📊 Features Overview

| Feature | Status |
|--------|--------|
| Real-time Detection | ✅ |
| AI Face Detection | ✅ |
| Eye Tracking | ✅ |
| EAR Calculation | ✅ |
| History Storage | ✅ |
| Web Interface | ✅ |
| Auto Installation | ✅ |
| Auto Run | ✅ |

---

## 🎯 Example Use Cases

• Driver Monitoring Systems  
• Smart Vehicle Safety  
• Transport Industry Safety  
• AI Surveillance Systems  
• Computer Vision Research

---

## 🔮 Future Improvements

- 🔔 Alarm Sound Alert
- 📱 Mobile Application
- ☁ Cloud Deployment
- 📍 GPS Tracking
- 📊 Driver Analytics Dashboard

---

## 💻 Requirements

- Python 3.9 or higher
- Webcam
- Windows OS

---
## ⭐ GitHub Repository
```
https://github.com/priya-ak/AI-Driver-Safety-System
```

## 🏆 Project Type

✔ Artificial Intelligence Project  
✔ Computer Vision Project  
✔ Real-Time AI System

---

## 🚀 Quick Start

Clone → Run → Detect
git clone https://github.com/priya-ak/AI-Driver-Safety-System.git

cd AI-Driver-Safety-System
run.bat
Open:http://127.0.0.1:9777

---

## 👩‍💻 Author

**Priyadharshini**

AI Developer | ML Engineer
---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
