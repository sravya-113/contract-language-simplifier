# Installation Guide for Contract Language Simplifier

## ⚠️ Important: Python 3.13 Compatibility Issue

You have Python 3.13.2 installed, which is very new. Some AI libraries (spaCy, PyTorch) don't have pre-built wheels for Python 3.13 yet and require C++ build tools to compile from source.

## ✅ What's Already Installed

The core application is **already set up** with these components:
- ✅ Flask web framework
- ✅ SQLAlchemy database
- ✅ JWT authentication
- ✅ Password hashing (bcrypt)
- ✅ Basic readability metrics (textstat)
- ✅ Environment configuration

## 🚀 Quick Start (Without AI Features)

You can run the application NOW in basic mode:

```bash
venv\Scripts\python.exe app.py
```

**However**, the AI simplification features won't work yet because they need additional libraries.

## 📋 Two Options to Proceed

### Option 1: Use Python 3.10 or 3.11 (Recommended)

1. **Uninstall Python 3.13** and install **Python 3.10** or **3.11** from [python.org](https://www.python.org/downloads/)
2. Delete the `venv` folder
3. Run `setup.bat` again

This will install all AI features smoothly.

### Option 2: Install AI Libraries Manually (Advanced)

If you want to keep Python 3.13, you need to install Microsoft Visual C++ Build Tools first:

1. **Download Visual Studio Build Tools**: https://visualstudio.microsoft.com/downloads/
2. Install "Desktop development with C++"
3. Then run:
   ```bash
   venv\Scripts\pip.exe install spacy nltk
   venv\Scripts\python.exe -m spacy download en_core_web_sm
   venv\Scripts\python.exe -c "import nltk; nltk.download('punkt')"
   ```
4. For PyTorch (large download ~2GB):
   ```bash
   venv\Scripts\pip.exe install torch transformers sentencepiece
   ```

## 🧪 Test What's Working Now

Run this test:

```bash
venv\Scripts\python.exe -c "import flask, flask_sqlalchemy, flask_jwt_extended, bcrypt, textstat; print('Core dependencies OK!')"
```

## 🎯 Recommended Next Steps

**For the best experience:**

1. Install Python 3.10.11 from: https://www.python.org/downloads/release/python-31011/
2. During installation, check "Add Python to PATH"
3. Delete the current `venv` folder in your project
4. Run `setup.bat` again
5. Everything will install smoothly!

## 💡 Alternative: Use Docker

If you have Docker installed, you can skip all Python version issues:

```bash
docker-compose up
```

This will work perfectly regardless of your Python version!

## ❓ Need Help?

The application structure is complete. The only issue is installing the AI libraries with Python 3.13.

**Quick Decision:**
- Want AI features? → Install Python 3.10 or 3.11
- Just want to see the UI? → Run `venv\Scripts\python.exe app.py` now (authentication and database will work)
- Have Docker? → Run `docker-compose up`
