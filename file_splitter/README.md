# 📄 FastAPI File Splitter

A simple and mobile-friendly web application that allows users to upload a file and split it into smaller parts based on a specified **keyword**. After processing, the user is redirected to a clean results page where all split files are available for download.

---

## ✨ Features

- ✅ Upload any text-based file (e.g., `.txt`, `.log`)
- 🔍 Split by keyword (e.g., "ERROR", "===")
- 📦 Automatically saves result files in `/static/results/`
- 🌐 Redirects to a result page listing all split parts
- 📱 Mobile-friendly UI
- 🧾 Clean, styled HTML templates using Jinja2

---

## 📦 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) - Backend framework
- Jinja2 - Template rendering
- HTML + CSS (No frontend frameworks)
- Python Standard Libraries (`shutil`, `uuid`, `zipfile`, etc.)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- fastapi
- uvicorn
### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/huanghaiyss/fastapi/file_splitter.git
   cd fastapi/file_splitter
   fastapi dev main.py
   # or
   # uvicorn main:app --reload
