@echo off
REM Quick Setup Script for Contract Language Simplifier (Windows)

echo ================================================
echo Contract Language Simplifier - Quick Setup
echo ================================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.10 or higher
    pause
    exit /b 1
)

echo [1/6] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

echo [2/6] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/6] Installing Python dependencies...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [4/6] Downloading spaCy model...
python -m spacy download en_core_web_sm
if errorlevel 1 (
    echo WARNING: Failed to download spaCy model
    echo You may need to run this manually later
)

echo [5/6] Downloading NLTK data...
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"

echo [6/6] Creating environment file...
if not exist .env (
    copy .env.example .env
    echo Created .env file - Please update SECRET_KEY and JWT_SECRET_KEY
) else (
    echo .env file already exists
)

echo.
echo ================================================
echo Setup Complete!
echo ================================================
echo.
echo Next steps:
echo 1. Edit .env file and update SECRET_KEY and JWT_SECRET_KEY
echo 2. Run: python test_installation.py (to verify setup)
echo 3. Run: python app.py (to start the application)
echo.
echo The application will be available at: http://localhost:5000
echo.
pause
