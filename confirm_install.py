import tkinter as tk
from tkinter import ttk



class ConfirmUninstallationScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Confirm uninstall")
        self.root.resizable(width=False, height=False)

        # Center the window on the screen
        window_width = 500
        window_height = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create a frame for the application
        app_frame = ttk.Frame(self.root)
        app_frame.pack(expand=True)
        are_you_sure = tk.Label(self.root, text="Are you sure ?", font="Helvetica 15 bold")
        are_you_sure.pack(padx=(5,20))
        v = ["welcome","welcome","welcome","welcome","welcome","welcome"," w"]
        list_of_apps = tk.Listbox(app_frame,listvariable=v)
        list_of_apps.pack(expand=True)

        self.root.mainloop()
