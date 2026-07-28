import csv
import time
import threading
from datetime import datetime
from pynput import keyboard

count = 0
lock = threading.Lock()

def on_press(key):
    global count
    with lock:
        count += 1

def log_data():
    global count
    while True:
        time.sleep(60)
        with lock:
            current_count = count
            count = 0
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open("keystroke_log.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, current_count])
        
        print(f"[{timestamp}] Recorded {current_count} keystrokes.")

def main():
    with open("keystroke_log.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "count"])

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    logger_thread = threading.Thread(target=log_data, daemon=True)
    logger_thread.start()

    print("KeyPulse is running. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping KeyPulse...")
        listener.stop()

if __name__ == "__main__":
    main()