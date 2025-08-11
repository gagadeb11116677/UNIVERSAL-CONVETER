import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
from docx2pdf import convert
from pdf2docx import Converter
import os
import subprocess
import threading

class FileConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Xobe Converter")
        self.root.geometry("550x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#faf8f5")

        self.filepath = None
        self.set_styles()
        self.create_widgets()

    def set_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox",
                        fieldbackground="#fff",
                        background="#e7ddd3",
                        foreground="#333",
                        arrowcolor="#b08968",
                        relief="flat")
        style.configure("Horizontal.TProgressbar",
                        troughcolor="#e7ddd3",
                        background="#b08968")

    def create_widgets(self):
        tk.Label(self.root, text="Xobe Converter", font=("Arial", 20, "bold"),
                 bg="#faf8f5", fg="#4b3f3a").pack(pady=15)

        self.option_var = tk.StringVar(value="Word → PDF")
        options = ["Word → PDF", "PDF → Word", "PNG → JPG", "JPG → PNG", "PDF → PNG", "PNG → PDF"]
        ttk.Combobox(self.root, textvariable=self.option_var, values=options,
                     state="readonly", font=("Arial", 11), width=22).pack(pady=5)

        tk.Button(self.root, text="📂 Pilih File", command=self.select_file,
                  font=("Arial", 11), bg="#eaddcf", fg="#333", bd=0, padx=20, pady=8).pack(pady=8)

        self.label_file = tk.Label(self.root, text="Tidak ada file dipilih", fg="#a68b6b", bg="#faf8f5")
        self.label_file.pack()

        tk.Button(self.root, text="🔄 Mulai Konversi", command=self.start_conversion_thread,
                  font=("Arial", 11, "bold"), bg="#b08968", fg="#fff", bd=0, padx=20, pady=8).pack(pady=15)

        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=350, mode="determinate")
        self.progress.pack(pady=10)

    def select_file(self):
        filetypes = {
            "Word → PDF": [("Word files", "*.docx")],
            "PDF → Word": [("PDF files", "*.pdf")],
            "PNG → JPG": [("PNG files", "*.png")],
            "JPG → PNG": [("JPG files", "*.jpg;*.jpeg")],
            "PDF → PNG": [("PDF files", "*.pdf")],
            "PNG → PDF": [("PNG files", "*.png")]
        }
        selected = self.option_var.get()
        self.filepath = filedialog.askopenfilename(filetypes=filetypes.get(selected))
        if self.filepath:
            self.label_file.config(text=os.path.basename(self.filepath))

    def start_conversion_thread(self):
        if not self.filepath:
            messagebox.showerror("Error", "Pilih file terlebih dahulu!")
            return
        self.progress["value"] = 0
        threading.Thread(target=self.convert_file, daemon=True).start()

    def convert_file(self):
        output_folder = filedialog.askdirectory(title="Pilih Folder Output")
        if not output_folder:
            return

        selected = self.option_var.get()
        output_path = os.path.join(output_folder, self.get_output_filename(selected))

        try:
            self.update_progress(10)
            if selected == "Word → PDF":
                convert(self.filepath, output_path)
            elif selected == "PDF → Word":
                cv = Converter(self.filepath)
                cv.convert(output_path, start=0, end=None)
                cv.close()
            elif selected == "PNG → JPG":
                with Image.open(self.filepath) as img:
                    rgb = img.convert("RGB")
                    rgb.save(output_path, "JPEG")
            elif selected == "JPG → PNG":
                with Image.open(self.filepath) as img:
                    img.save(output_path, "PNG")
            elif selected == "PDF → PNG":
                base = output_path.replace(".png", "")
                subprocess.run(["pdftoppm", "-png", self.filepath, base], check=True)
            elif selected == "PNG → PDF":
                with Image.open(self.filepath) as img:
                    rgb = img.convert("RGB")
                    rgb.save(output_path, "PDF")
            self.update_progress(100)
            messagebox.showinfo("Sukses", f"File disimpan di:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Konversi gagal:\n{str(e)}")
        finally:
            self.progress["value"] = 0

    def update_progress(self, value):
        self.root.after(0, lambda: self.progress.config(value=value))

    def get_output_filename(self, selected):
        base = os.path.splitext(os.path.basename(self.filepath))[0]
        return {
            "Word → PDF": f"{base}.pdf",
            "PDF → Word": f"{base}.docx",
            "PNG → JPG": f"{base}.jpg",
            "JPG → PNG": f"{base}.png",
            "PDF → PNG": f"{base}.png",
            "PNG → PDF": f"{base}.pdf"
        }.get(selected, f"{base}_output")

if __name__ == "__main__":
    root = tk.Tk()
    FileConverterApp(root)
    root.mainloop()
