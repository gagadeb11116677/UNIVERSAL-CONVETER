# 📁 Universal File Converter – Beta v0.9.0
**A simple, open-source desktop GUI for converting documents & images.**  
Maintained by **Xobe Development** in collaboration with **Creammm**.

---

## ✅ Features
| From → To            | Status |
|----------------------|--------|
| Word (.docx) → PDF   | ✅     |
| PDF → Word (.docx)   | ✅     |
| PNG → JPG            | ✅     |
| JPG → PNG            | ✅     |
| PDF → PNG (per page) | ✅     |
| PNG → PDF            | ✅     |

---

## 🖼️ Logo / Badge
![Beta](https://img.shields.io/badge/status-beta-orange)
![MIT](https://img.shields.io/badge/license-MIT-green)



---

## 🚀 Getting Started

### 1. Download
Clone or download ZIP:
```bash
git clone https://github.com/xobedevelopment/universal-file-converter.git
cd universal-file-converter

### Create a virtual-env (recommended):
python -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows

###Install dependencies:
pip install -r requirements.txt

###RUN:
python converter_ui.py


##🛠️ Requirements (System-Wide)
Tool	Windows	macOS	Linux (Debian/Ubuntu)
Poppler	poppler-windows	brew install poppler	sudo apt install poppler-utils
Needed only for PDF → PNG conversion.

📋 Usage Guide (Step-by-Step)
Launch
Double-click converter_ui.py or run via terminal.
Choose Conversion
Use the dropdown to select the direction (e.g. Word → PDF).
Select Source File
Click 📂 Pilih File → browse your file.
Pick Output Folder
A dialog will ask where to save the converted file.
Convert
Press 🔄 Konversi – progress bar spins until done.
Result
A success popup shows the exact output path.

🧪 Beta Notes
This is a beta release.
Known limitations:
Password-protected PDFs are not supported.
Very large PDFs (>100 MB) may freeze the UI (fix in v1.0).
Drag-and-drop not yet implemented.

🤝 Contributing
Fork the repo.
Create a feature branch (git checkout -b feature/amazing-idea).
Commit (git commit -m 'Add amazing idea').
Push (git push origin feature/amazing-idea).
Open a Pull Request.

📄 License
MIT © 2025 Xobe Development & Creammm
You are free to use, modify and distribute under the terms of the MIT License.
📬 Credits
Xobe Development – Core logic & GUI design
Creammm – Icon, UX flow & beta testing
Pillow, docx2pdf, pdf2docx – underlying libraries


## 🔄 Update – Beta v0.1.0 (UI/UX Redesign)

**Release Date:** 2025-08-11

### ✨ Changes
- **Complete UI Redesign**
  - Cleaner and more modern flat style.
  - Improved button and dropdown sizes for better usability.
  - Smoother progress bar animation.
  - Updated icons for a more consistent look.

- **UX Enhancements**
  - More readable layout and spacing.
  - Clearer status messages during conversion.
  - Dark/Light mode toggle for better accessibility.




