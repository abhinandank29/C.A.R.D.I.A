import tkinter as tk
from tkinter import messagebox
import subprocess

def run_client():
    subprocess.run(["python", "client.py"])

# Create main window
client_window = tk.Tk()
client_window.title("Federated Learning Client")

# Create and configure widgets
label = tk.Label(client_window, text="Click below to run the Federated Learning Client:")
label.pack(pady=10)

run_button = tk.Button(client_window, text="Run Client", command=run_client)
run_button.pack(pady=20)

# Start the Tkinter event loop
client_window.mainloop()
