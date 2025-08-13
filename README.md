# 📁 Universal File Converter – Beta v0.2.0

**A simple, open-source desktop GUI for converting documents & images.**
Maintained by **Xobe Development** in collaboration with **Creammm**.

---

## ✅ Features

| From → To            | Status |
| -------------------- | ------ |
| Word (.docx) → PDF   | ✅      |
| PDF → Word (.docx)   | ✅      |
| PNG → JPG            | ✅      |
| JPG → PNG            | ✅      |
| PDF → PNG (per page) | ✅      |
| PNG → PDF 
|excel → json/csv      | ✅      |
|mp4 →  mp3            | yes
---

## 🖼️ Logo / Badge

![Beta](https://img.shields.io/badge/status-beta-orange)
![MIT](https://img.shields.io/badge/license-MIT-green)

---

## 🚀 Getting Started

### 1. Download

```bash
git clone https://github.com/xobedevelopment/universal-file-converter.git
cd universal-file-converter
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run

```bash
python converter_ui.py
```

---

## 🛠️ Requirements (System-Wide)

| Tool    | Windows         | macOS                | Linux (Debian/Ubuntu)          |
| ------- | --------------- | -------------------- | ------------------------------ |
| Poppler | poppler-windows | brew install poppler | sudo apt install poppler-utils |

> Required only for **PDF → PNG** conversion.

---

## 📋 Usage Guide (Step-by-Step)

1. **Launch** – Double-click `converter_ui.py` or run via terminal.
2. **Choose Conversion** – Use the dropdown to select the direction (e.g. *Word → PDF*).
3. **Select Source File** – Click 📂 *Pilih File* to browse your file.
4. **Pick Output Folder** – Choose where to save the converted file.
5. **Convert** – Press 🔄 *Konversi* – progress bar spins until done.
6. **Result** – A success popup shows the exact output path.

---

## 🧪 Beta Notes

* This is a beta release.
* Known limitations:

  * Password-protected PDFs are not supported.
  * Very large PDFs (>100 MB) may freeze the UI (planned fix in v1.0).
  * Drag-and-drop not yet implemented.

---

## 🤝 Contributing

1. Fork the repo.
2. Create a feature branch:

   ```bash
   git checkout -b feature/amazing-idea
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add amazing idea"
   ```
4. Push to the branch:

   ```bash
   git push origin feature/amazing-idea
   ```
5. Open a Pull Request.

---

## 📄 License

MIT © 2025 **Xobe Development** & **Creammm**
You are free to use, modify, and distribute under the terms of the MIT License.

---

## 📬 Credits

* **Xobe Development** – Core logic & GUI design
* **Creammm** – Icon, UX flow & beta testing
* **Pillow**, **docx2pdf**, **pdf2docx** – underlying libraries

---

---

# 📦 Changelog — v0.2.0

## ✨ New Features
- Cleaner and more compact UI for better usability.
- Added file conversion tools:
  - **Excel ↔ CSV / JSON** conversion.
  - **MP4 → MP3** audio extraction.
- Real-time progress bar based on file size during processing.

## 🛠 Improvements
- Fixed minor bugs from the `0.1.x` series.
- Optimized performance for large file conversions.

## 🚫 Removed
- No additional logos or icons included in this release.

---

**Credits:** Developed by **XOBE DEVELOPMENT** & **creammm**  
**License:** MIT
