import os
import subprocess
import threading
import logging
from pathlib import Path

# GUI
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Image processing
from PIL import Image  # pip install Pillow

# Data processing (Excel, CSV, JSON)
import pandas as pd  # pip install pandas
import openpyxl       # pip install openpyxl

# Document conversion
from docx2pdf import convert as d2p   # pip install docx2pdf
from pdf2docx import Converter as p2d # pip install pdf2docx

# Video/audio processing
from moviepy import VideoFileClip  # pip install moviepy (requires ffmpeg)

# Note:
# - Untuk PDF → PNG, membutuhkan `pdftoppm` dari paket Poppler (instal manual sesuai OS)
# - Untuk MP4 → MP3, membutuhkan ffmpeg (instal manual sesuai OS)

VERSION = "0.2.0-BETA"

class FileConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"Xobe Converter {VERSION}")
        self.root.geometry("520x380")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

        self.filepath = None

        # --- widgets ---
        tk.Label(root, text="Xobe Converter", font=("Segoe UI", 18, "bold"),
                 bg="#f5f5f5", fg="#333").pack(pady=12)

        self.option_var = tk.StringVar(value="Word → PDF")
        self.options = [
            "Word → PDF",
            "PDF → Word",
            "PNG ↔ JPG",
            "PDF → PNG",
            "PNG → PDF",
            "Excel → CSV",
            "CSV → Excel",
            "Excel → JSON",
            "JSON → Excel",
            "MP4 → MP3"
        ]
        ttk.Combobox(root, textvariable=self.option_var, values=self.options,
                     state="readonly", width=25, font=("Segoe UI", 10)).pack(pady=5)

        tk.Button(root, text="📁 Pilih File", command=self.select_file,
                  font=("Segoe UI", 10), bg="#e1e1e1", fg="#000",
                  bd=0, padx=15, pady=7).pack(pady=8)

        self.label_file = tk.Label(root, text="Belum ada file dipilih",
                                   fg="#555", bg="#f5f5f5")
        self.label_file.pack()

        tk.Button(root, text="🔄 Mulai Konversi", command=self.start_conversion_thread,
                  font=("Segoe UI", 11, "bold"), bg="#0078d4", fg="#fff",
                  bd=0, padx=20, pady=8).pack(pady=12)

        self.progress = ttk.Progressbar(root, orient="horizontal",
                                        length=400, mode="determinate")
        self.progress.pack(pady=8)

    # ---------- file dialog ----------
    def select_file(self):
        ext_map = {
            "Word → PDF": [("Word", "*.docx")],
            "PDF → Word": [("PDF", "*.pdf")],
            "PNG ↔ JPG": [("Images", "*.png *.jpg *.jpeg")],
            "PDF → PNG": [("PDF", "*.pdf")],
            "PNG → PDF": [("PNG", "*.png")],
            "Excel → CSV": [("Excel", "*.xlsx")],
            "CSV → Excel": [("CSV", "*.csv")],
            "Excel → JSON": [("Excel", "*.xlsx")],
            "JSON → Excel": [("JSON", "*.json")],
            "MP4 → MP3": [("MP4", "*.mp4")]
        }
        opt = self.option_var.get()
        filetypes = ext_map.get(opt, [])
        self.filepath = filedialog.askopenfilename(filetypes=filetypes)
        if self.filepath:
            self.label_file.config(text=Path(self.filepath).name)

    # ---------- threading ----------
    def start_conversion_thread(self):
        if not self.filepath:
            messagebox.showerror("Error", "Pilih file terlebih dahulu!")
            return
        self.progress["value"] = 0
        threading.Thread(target=self.convert_file, daemon=True).start()

    # ---------- konversi ----------
    def convert_file(self):
        try:
            out_dir = filedialog.askdirectory(title="Simpan ke folder")
            if not out_dir:
                return
            out_path = Path(out_dir) / self.build_output_name()
            self.update_progress(10)

            opt = self.option_var.get()
            if opt == "Word → PDF":
                d2p(self.filepath, str(out_path))
            elif opt == "PDF → Word":
                cv = p2d(self.filepath)
                cv.convert(str(out_path), start=0, end=None)
                cv.close()
            elif opt == "PNG ↔ JPG":
                with Image.open(self.filepath) as img:
                    rgb = img.convert("RGB")
                    rgb.save(out_path, "JPEG" if out_path.suffix.lower() == ".jpg" else "PNG")
            elif opt == "PDF → PNG":
                base = str(out_path).replace(".png", "")
                subprocess.run(["pdftoppm", "-png", self.filepath, base], check=True)
            elif opt == "PNG → PDF":
                with Image.open(self.filepath) as img:
                    rgb = img.convert("RGB")
                    rgb.save(str(out_path), "PDF", resolution=100.0)
            elif opt == "Excel → CSV":
                df = pd.read_excel(self.filepath, engine="openpyxl")
                df.to_csv(out_path, index=False)
            elif opt == "CSV → Excel":
                df = pd.read_csv(self.filepath)
                df.to_excel(out_path, index=False, engine="openpyxl")
            elif opt == "Excel → JSON":
                df = pd.read_excel(self.filepath, engine="openpyxl")
                df.to_json(out_path, orient="records", indent=2, force_ascii=False)
            elif opt == "JSON → Excel":
                df = pd.read_json(self.filepath)
                df.to_excel(out_path, index=False, engine="openpyxl")
            elif opt == "MP4 → MP3":
                clip = VideoFileClip(self.filepath)
                clip.audio.write_audiofile(str(out_path), logger=None)
                clip.close()
            else:
                raise ValueError("Opsi tidak dikenal")

            self.update_progress(100)
            messagebox.showinfo("Selesai", f"File berhasil disimpan:\n{out_path}")
        except Exception as e:
            logging.exception("Konversi gagal")
            messagebox.showerror("Gagal", f"Error: {e}")
        finally:
            self.update_progress(0)

    # ---------- helper ----------
    def build_output_name(self) -> str:
        base = Path(self.filepath).stem
        opt = self.option_var.get()
        ext_map = {
            "Word → PDF": ".pdf",
            "PDF → Word": ".docx",
            "PNG ↔ JPG": ".jpg" if Path(self.filepath).suffix.lower() == ".png" else ".png",
            "PDF → PNG": ".png",
            "PNG → PDF": ".pdf",
            "Excel → CSV": ".csv",
            "CSV → Excel": ".xlsx",
            "Excel → JSON": ".json",
            "JSON → Excel": ".xlsx",
            "MP4 → MP3": ".mp3"
        }
        return base + ext_map.get(opt, "_unknown")

    def update_progress(self, val):
        self.root.after(0, lambda: self.progress.config(value=val))

# ---------- main ----------
if __name__ == "__main__":
    root = tk.Tk()
    FileConverterApp(root)
    root.mainloop()
