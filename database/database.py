import sqlite3
from datetime import datetime
import os

DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "driver_data.db"
)


def save_drowsiness():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS drowsiness_log(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        time TEXT,
        status TEXT
    )
    """)

    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "INSERT INTO drowsiness_log(time,status) VALUES (?,?)",
        (time_now,"Drowsiness Detected")
    )

    conn.commit()

    conn.close()