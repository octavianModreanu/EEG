import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from validation import validate
import os

class DatasetValidatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BIDS Dataset Validator")
        self.root.geometry("600x400")
        
        # Configure style
        style = ttk.Style()
        style.configure("Custom.TFrame", background="#f0f0f0")
        
        # Main frame
        self.main_frame = ttk.Frame(self.root, padding="20", style="Custom.TFrame")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Browse button
        self.browse_btn = ttk.Button(
            self.main_frame,
            text="Select Dataset Folder",
            command=self.browse_folder
        )
        self.browse_btn.pack(pady=20)
        
        # Selected path label
        self.path_label = ttk.Label(self.main_frame, text="No folder selected")
        self.path_label.pack(pady=10)
        
        # Status label
        self.status_label = ttk.Label(self.main_frame, text="")
        self.status_label.pack(pady=10)
        
        # Validate button
        self.validate_btn = ttk.Button(
            self.main_frame,
            text="Validate Dataset",
            command=self.validate_dataset,
            state="disabled"
        )
        self.validate_btn.pack(pady=10)
        
        self.dataset_path = None

    def browse_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.dataset_path = path
            self.path_label.configure(text=f"Selected: {os.path.basename(path)}")
            self.validate_btn.configure(state="normal")

    def validate_dataset(self):
        if not self.dataset_path:
            return
            
        self.status_label.configure(text="Validating...")
        self.root.update()
        
        is_valid = validate(self.dataset_path)
        
        if is_valid:
            self.status_label.configure(text="✅ Dataset validation successful!")
        else:
            self.status_label.configure(text="❌ Dataset validation failed")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = DatasetValidatorGUI()
    app.run() 