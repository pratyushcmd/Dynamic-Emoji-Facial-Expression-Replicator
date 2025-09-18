# Dynamic Emoji Facial Expression Replicator

This project is a real-time facial expression recognition application that overlays emojis corresponding to detected emotions on a live webcam feed. It combines **computer vision**, **deep learning**, and a simple **web interface** to demonstrate the practical use of AI in an interactive and engaging way.

---

## 📖 Overview
- Detects facial expressions using **DeepFace** and **OpenCV**.
- Maps detected emotions to corresponding emoji icons (e.g., happy → 😀).
- Renders output in a **Streamlit** web app for easy interaction.
- Designed for both **educational demonstrations** and **hands-on AI learning**.

---

## 🚀 Features
- Real-time emotion detection through webcam feed.
- Supports seven emotions: `happy`, `sad`, `angry`, `surprise`, `neutral`, `fear`, and `disgust`.
- Emoji overlay dynamically aligned with detected face position.
- Lightweight, easy-to-run Python app with minimal setup.
- Deployable on **Streamlit Cloud** for instant access.

---

## 🛠️ Tech Stack
- **Python 3.8+**
- [Streamlit](https://streamlit.io/)
- [OpenCV](https://opencv.org/)
- [DeepFace](https://github.com/serengil/deepface)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [NumPy](https://numpy.org/)

---
## 📂 Project Structure
## 📂 Project Structure.
├── app.py # Main application script
├── happy.png # Emoji images
├── sad.png
├── angry.png
├── surprised.png
├── neutral.png
├── fear.png
├── disgust.png
├── requirements.txt # Dependencies file
└── README.md # Project documentation


## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/emoji-facial-expression.git
   cd emoji-facial-expression
2.   Create and activate a virtual environment:
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

3. Run locally
 streamlit run app.py

