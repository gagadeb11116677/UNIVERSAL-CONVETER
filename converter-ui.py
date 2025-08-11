import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
from docx2pdf import convert
from pdf2docx import Converter
import os
import subprocess

class FileConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal File Converter")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="📁 Universal File Converter", font=("Arial", 18, "bold"))
        title.pack(pady=10)

        self.option_var = tk.StringVar(value="Word → PDF")
        options = [
            "Word → PDF",
            "PDF → Word",
            "PNG → JPG",
            "JPG → PNG",
            "PDF → PNG",
            "PNG → PDF"
        ]
        menu = ttk.Combobox(self.root, textvariable=self.option_var, values=options, state="readonly", width=25)
        menu.pack(pady=5)

        self.btn_select = tk.Button(self.root, text="📂 Pilih File", command=self.select_file, width=30, bg="#4CAF50", fg="white")
        self.btn_select.pack(pady=10)

        self.label_file = tk.Label(self.root, text="Belum ada file dipilih", fg="gray")
        self.label_file.pack()

        self.btn_convert = tk.Button(self.root, text="🔄 Konversi", command=self.convert_file, width=30, bg="#2196F3", fg="white")
        self.btn_convert.pack(pady=20)

        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="indeterminate")
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
        filetypes = filetypes.get(selected, [("All files", "*.*")])

        self.filepath = filedialog.askopenfilename(filetypes=filetypes)
        if self.filepath:
            self.label_file.config(text=os.path.basename(self.filepath))

    def convert_file(self):
        if not hasattr(self, 'filepath'):
            messagebox.showerror("Error", "Pilih file terlebih dahulu!")
            return

        output_folder = filedialog.askdirectory(title="Pilih Folder Output")
        if not output_folder:
            return

        self.progress.start()
        try:
            selected = self.option_var.get()
            output_path = os.path.join(output_folder, self.get_output_filename(selected))

            if selected == "Word → PDF":
                convert(self.filepath, output_path)
            elif selected == "PDF → Word":
                cv = Converter(self.filepath)
                cv.convert(output_path, start=0, end=None)
                cv.close()
            elif selected == "PNG → JPG":
                img = Image.open(self.filepath)
                img = img.convert("RGB")
                img.save(output_path, "JPEG")
            elif selected == "JPG → PNG":
                img = Image.open(self.filepath)
                img.save(output_path, "PNG")
            elif selected == "PDF → PNG":
                subprocess.run(["pdftoppm", "-png", self.filepath, output_path.replace(".png", "")])
            elif selected == "PNG → PDF":
                img = Image.open(self.filepath)
                img = img.convert("RGB")
                img.save(output_path, "PDF")

            messagebox.showinfo("Sukses", f"File berhasil disimpan:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mengkonversi:\n{str(e)}")
        finally:
            self.progress.stop()

    def get_output_filename(self, selected):
        base = os.path.splitext(os.path.basename(self.filepath))[0]
        mapping = {
            "Word → PDF": base + ".pdf",
            "PDF → Word": base + ".docx",
            "PNG → JPG": base + ".jpg",
            "JPG → PNG": base + ".png",
            "PDF → PNG": base + ".png",
            "PNG → PDF": base + ".pdf"
        }
        return mapping.get(selected, base + "_output")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileConverterApp(root)
    root.mainloop()
