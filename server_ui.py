import tkinter as tk
from tkinter import messagebox
import subprocess

def run_server():
    subprocess.run(["python", "server.py"])

# Create main window
server_window = tk.Tk()
server_window.title("Federated Learning Server")

# Create and configure widgets
label = tk.Label(server_window, text="Click below to run the Federated Learning Server:")
label.pack(pady=10)

run_button = tk.Button(server_window, text="Run Server", command=run_server)
run_button.pack(pady=20)

# Start the Tkinter event loop
server_window.mainloop()
