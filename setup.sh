#!/bin/bash
# Quick Setup Script for Contract Language Simplifier (Linux/Mac)

echo "================================================"
echo "Contract Language Simplifier - Quick Setup"
echo "================================================"
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.10 or higher"
    exit 1
fi

echo "[1/6] Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    exit 1
fi

echo "[2/6] Activating virtual environment..."
source venv/bin/activate

echo "[3/6] Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo "[4/6] Downloading spaCy model..."
python -m spacy download en_core_web_sm
if [ $? -ne 0 ]; then
    echo "WARNING: Failed to download spaCy model"
    echo "You may need to run this manually later"
fi

echo "[5/6] Downloading NLTK data..."
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"

echo "[6/6] Creating environment file..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Created .env file - Please update SECRET_KEY and JWT_SECRET_KEY"
else
    echo ".env file already exists"
fi

echo ""
echo "================================================"
echo "Setup Complete!"
echo "================================================"
echo ""
echo "Next steps:"
echo "1. Edit .env file and update SECRET_KEY and JWT_SECRET_KEY"
echo "2. Run: python test_installation.py (to verify setup)"
echo "3. Run: python app.py (to start the application)"
echo ""
echo "The application will be available at: http://localhost:5000"
echo ""
