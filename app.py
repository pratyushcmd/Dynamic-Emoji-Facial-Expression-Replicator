import streamlit as st
import cv2
import numpy as np
from deepface import DeepFace
from PIL import Image

EMOJI_MAP = {
    "happy": "happy.png",
    "sad": "sad.png",
    "angry": "angry.png",
    "surprise": "surprised.png",
    "neutral": "neutral.png",
    "fear": "fear.png",
    "disgust": "disgust.png"
}

def load_emojis():
    emojis = {}
    for emotion, filename in EMOJI_MAP.items():
        try:
            emojis[emotion] = Image.open(filename).convert("RGBA")
        except Exception:
            emojis[emotion] = None
    return emojis

emojis = load_emojis()
st.title("Dynamic Emoji Facial Expression Replicator")
run = st.checkbox("Start Camera")
FRAME_WINDOW = st.image([])

def overlay_emoji(frame, emoji_img, face_coords, size=100):
    if emoji_img is None or face_coords is None:
        return frame
    x, y, w, h = face_coords
    emoji = emoji_img.resize((size, size))
    x_offset = x + w // 2 - size // 2
    y_offset = max(0, y - size - 10)
    pil_frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    pil_frame.paste(emoji, (x_offset, y_offset), emoji)
    return cv2.cvtColor(np.array(pil_frame), cv2.COLOR_RGB2BGR)

def get_face_box(face):
    region = face.get('region', None)
    if region is None:
        return None
    x, y, w, h = region.get('x', 0), region.get('y', 0), region.get('w', 0), region.get('h', 0)
    return int(x), int(y), int(w), int(h)

if run:
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Could not access webcam.")
            break
        frame = cv2.flip(frame, 1)
        try:
            # DeepFace returns a list if detect_multiple_faces is True or in recent versions
            result = DeepFace.analyze(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), actions=['emotion'], enforce_detection=False)
            if isinstance(result, list):
                face_result = result[0] if result else {}
            else:
                face_result = result
            dominant_emotion = face_result.get('dominant_emotion', 'neutral')
            face_box = get_face_box(face_result)
        except Exception as e:
            print("DeepFace error:", e)
            dominant_emotion = "neutral"
            face_box = None

        emoji_img = emojis.get(dominant_emotion, emojis["neutral"])
        frame = overlay_emoji(frame, emoji_img, face_box)
        FRAME_WINDOW.image(frame, channels="BGR")
        if not st.session_state.get("Start Camera", True):
            break
    cap.release()
else:
    st.write("Camera stopped.")
