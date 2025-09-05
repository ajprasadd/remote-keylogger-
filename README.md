Remote Keylogger (Educational Project)

⚠️ Disclaimer:
This project is created strictly for educational and research purposes in the field of cybersecurity.
It must not be used on any device or network without explicit permission. Unauthorized use of keyloggers is illegal and violates privacy rights.

📌 Project Overview
This project demonstrates how keystrokes can be captured locally and transmitted to a remote server for monitoring. It combines:
Python Pynput → to log keystrokes on the client system.
Flask (Python web framework) → to host a simple server that receives and displays logs via a specific port.
The goal is to understand how logging tools work, and to practice building secure client-server applications.

⚙️ Features
Keystroke logging using pynput
Transmission of logs to a Flask server over HTTP
Real-time log viewing via web browser
Configurable port for communication

🛠️ Requirements
Install dependencies with:
pip install pynput flask

🚀 Usage
Start the Flask server (on your own machine or VM):
python server.py
By default, it will run on http://127.0.0.1:5000.
Run the keylogger client:
python keylogger.py
The client will capture keystrokes and send them to the Flask server.
View captured logs in your browser at:
http://127.0.0.1:5000/logs

📂 Project Structure
📦 remote-keylogger
 ┣ 📜 keylogger.py     # Client script (captures and sends keystrokes)
 ┣ 📜 server.py        # Flask server (receives and displays logs)
 ┣ 📜 README.md        # Project documentation
 ┗ 📜 requirements.txt # Dependencies

🔒 Security Notes
This project should only be run on your own system or in a controlled lab environment.
If adapted for demonstrations, consider:
Restricting access to localhost
Adding authentication to Flask endpoints
Encrypting communication between client and server

📖 Learning Outcomes
Basics of event listeners (pynput)
Simple client-server communication in Python
Secure coding considerations in monitoring tools
📜 License
This project is licensed under the MIT License.
Use it only for educational purposes.
