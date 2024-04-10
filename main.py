import tkinter as tk
from tkinter import ttk
from monitor import Monitor

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("System Monitor")

        self.monitor = Monitor()

        self.create_widgets()

    def create_widgets(self):
        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.pack(expand=1, fill="both")

        # Create tabs
        tabs = ['Download', 'Disk', 'CPU', 'Memory', 'Network']
        for tab_name in tabs:
            tab = ttk.Frame(self.tab_control)
            self.tab_control.add(tab, text=tab_name)

        # Create labels for each tab
        self.labels = {}
        for tab_name in tabs:
            label = ttk.Label(self.tab_control.tab(tab_name), text="Loading...")
            label.pack(padx=10, pady=10)
            self.labels[tab_name] = label

        # Start monitoring
        self.start_monitoring()

    def start_monitoring(self):
        self.monitor.start_monitoring(self.update_ui)

    def update_ui(self, data):
        for tab_name, values in data.items():
            self.labels[tab_name].config(text=values)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
