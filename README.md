# Contract Language Simplifier

🤖 AI-powered web application that simplifies complex legal contracts into easy-to-understand language.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)

## ✨ Features

- **Multi-Level Simplification**: Basic, Intermediate, and Advanced modes
- **AI-Powered**: Uses Hugging Face FLAN-T5 and BART models
- **Readability Analysis**: 6 different metrics (Flesch-Kincaid, Gunning Fog, etc.)
- **Legal Term Highlighting**: 40+ default legal terms with explanations
- **Summarization**: Automatic document summarization
- **User Authentication**: Secure JWT-based authentication
- **Admin Dashboard**: Manage users and glossary terms
- **Responsive UI**: Beautiful Bootstrap 5 interface

## 🚀 Quick Start

### Option 1: Docker (Recommended)

```bash
docker-compose up
```

Access at: http://localhost:5000

### Option 2: Local Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download models
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('punkt')"

# Create .env file
cp .env.example .env

# Run application
python app.py
```

## 🌐 Deploy to Hugging Face Spaces

[![Deploy to Spaces](https://huggingface.co/datasets/huggingface/badges/raw/main/deploy-to-spaces-lg.svg)](https://huggingface.co/spaces)

1. Create a new Space on Hugging Face
2. Select **Docker** as SDK
3. Connect this GitHub repository
4. Add environment variables in Space settings:
   - `SECRET_KEY`
   - `JWT_SECRET_KEY`
5. Your app will be live in 10-15 minutes!

## 📚 Tech Stack

- **Backend**: Flask, SQLAlchemy, JWT
- **Frontend**: Jinja2, Bootstrap 5
- **AI/NLP**: Hugging Face Transformers, spaCy, NLTK
- **Database**: SQLite (default), PostgreSQL (production)
- **Deployment**: Docker, Gunicorn

## 📖 Documentation

- [Quick Start Guide](QUICKSTART.md)
- [Deployment Guide](DEPLOY_GUIDE.md)
- [Installation Help](INSTALL_HELP.md)

## 🎯 Usage

1. **Register**: Create an account (first user becomes admin)
2. **Login**: Use your credentials
3. **Simplify**: Paste legal text or upload a .txt file
4. **Select Level**: Choose Basic, Intermediate, or Advanced
5. **Review**: See side-by-side comparison with readability scores
6. **Download**: Save your simplified document

## 🔧 Configuration

Edit `.env` file:

```env
FLASK_ENV=production
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret
DATABASE_URL=sqlite:///database.db
```

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## 🙏 Acknowledgments

- Hugging Face for transformer models
- spaCy for NLP processing
- Bootstrap for UI components

---

**Made with ❤️ for simplifying legal language**
