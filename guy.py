# gui.py

import tkinter as tk

def start_gui(config):
    """Start the GUI interface."""
    root = tk.Tk()
    root.title("CC-Link RS485 Simulator")

    # Create a label for the GUI
    label = tk.Label(root, text="CC-Link RS485 Simulator GUI", font=("Arial", 16))
    label.pack(pady=20)

    # Add a button to start the simulation
    start_button = tk.Button(root, text="Start Simulation", command=lambda: print("Simulation started"))
    start_button.pack(pady=10)

    # Add a button to stop the simulation
    stop_button = tk.Button(root, text="Stop Simulation", command=lambda: print("Simulation stopped"))
    stop_button.pack(pady=10)

    # Add a text area to display RS485 traffic
    text_area = tk.Text(root, height=10, width=50)
    text_area.pack(pady=10)
    text_area.insert(tk.END, "RS485 Traffic Log\n")

    # Run the GUI main loop
    root.mainloop()