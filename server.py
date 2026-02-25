from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

import sqlite3
import cv2
import time

from ai.drowsiness import detect_drowsiness


app = FastAPI()

templates = Jinja2Templates(directory="templates")


# Camera variables
camera = None
running = False


# ========================
# Home Page
# ========================

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# ========================
# Start Detection
# ========================

@app.get("/start")
def start():

    global running
    global camera

    if not running:

        camera = cv2.VideoCapture(0)
        running = True

    return {"status":"started"}


# ========================
# Stop Detection
# ========================

@app.get("/stop")
def stop_detection():

    global running
    global camera

    running = False

    if camera is not None:
        camera.release()
        camera = None

    return {"status":"stopped"}


# ========================
# Camera Stream
# ========================

def generate_frames():

    global running
    global camera

    while True:

        if running and camera is not None:

            success, frame = camera.read()

            if not success:
                continue

            frame, drowsy = detect_drowsiness(frame)

            ret, buffer = cv2.imencode('.jpg', frame)

            frame = buffer.tobytes()

            yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' +
                frame +
                b'\r\n'
            )

        else:

            # Idle mode (camera OFF)
            time.sleep(0.1)


@app.get("/video")
def video():

    return StreamingResponse(
        generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )


# ========================
# History Page
# ========================

@app.get("/history", response_class=HTMLResponse)
def history(request: Request):

    conn = sqlite3.connect("driver_data.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM drowsiness_log
    ORDER BY id DESC
    LIMIT 20
    """)

    rows = cursor.fetchall()

    conn.close()

    return templates.TemplateResponse(
        "history.html",
        {
            "request":request,
            "rows":rows
        }
    )