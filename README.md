# Redaction Project (Test)
To automate PII masking. 


# Quick Setup Reference

## First Time Setup

```bash
# 1. Check Python version (need 3.11-3.13, NOT 3.14)
py --list

# 2. Install Tesseract OCR
# Download: https://github.com/UB-Mannheim/tesseract/wiki
# Install and add to PATH

# 3. Create virtual environment
py -3.13 -m venv venv

# 4. Activate venv
venv\Scripts\activate              # Windows
source venv/bin/activate           # Mac/Linux

# 5. Install dependencies
pip install -r requirements.txt

# 6. Download spaCy model
python -m spacy download en_core_web_lg

# 7. Test setup
python test_setup.py
```

## VS Code Setup

1. Open Command Palette: `Ctrl+Shift+P`
2. Type: `Python: Select Interpreter`
3. Choose: `.\venv\Scripts\python.exe`
4. Restart VS Code

## Workflow

```bash
# Activate venv
venv\Scripts\activate

# Verify correct Python
python --version

# Work on project
cd redaction-system
python src/main.py
```