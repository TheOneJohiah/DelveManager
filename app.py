import awakened # Pull in awakened, and thus everything else?
import signal
import sys
import os
import pickle
from flask import Flask, render_template
from flask_socketio import SocketIO

"""def exit_handler(signum, frame):
    print("\nCleaning up before exiting...")
    # Add your cleanup tasks here
    print("Exiting program.")
    sys.exit(0)

# Register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, exit_handler)

def handle_command(command):
    if command == "loadFolder":
        print("Loading folder...")
        # Add logic for 'loadFolder' command
    elif command == "bootGUI":
        print("Booting GUI...")
        # Add logic for 'bootGUI' command
    elif command == "quit":
        #print("Quitting program...")
        exit_handler(signal.SIGINT, None)
    elif command == "help":
        print("Displaying help...")
        # Add logic for 'help' command
    else:
        print("Unknown command. Type 'help' for available commands.")
"""

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("example.html")

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=51000, debug=True)

"""# Main control loop
while True:
    user_input = input("Enter a command ('quit' to exit): ")

    handle_command(user_input)"""