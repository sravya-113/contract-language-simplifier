# 🚀 Quick Start Guide - Contract Language Simplifier

## ⚡ Fastest Way to Get Started

### Option 1: Automated Setup (Recommended)

**Windows:**
```bash
cd "Contract Language Simplifier"
setup.bat
```

**Linux/Mac:**
```bash
cd "Contract Language Simplifier"
chmod +x setup.sh
./setup.sh
```

The script will:
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Download AI models (spaCy, NLTK)
- ✅ Create .env file

### Option 2: Docker (One Command)

```bash
cd "Contract Language Simplifier"
docker-compose up -d
```

Access at: http://localhost:5000

---

## 📝 Manual Setup (If Automated Fails)

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # Activate
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Models**
   ```bash
   python -m spacy download en_core_web_sm
   python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
   ```

4. **Configure Environment**
   ```bash
   copy .env.example .env  # Windows
   cp .env.example .env    # Linux/Mac
   ```
   
   Edit `.env` and update:
   - `SECRET_KEY=your-secret-key-here`
   - `JWT_SECRET_KEY=your-jwt-secret-here`

5. **Run Application**
   ```bash
   python app.py
   ```

---

## 🎯 First Time Usage

1. **Open Browser**: http://localhost:5000

2. **Register Account**
   - Click "Register"
   - Fill in username, email, password
   - First user becomes admin automatically

3. **Login**
   - Use your credentials
   - You'll see the dashboard

4. **Test Simplification**
   - Click "Simplify" in navigation
   - Paste this sample text:
   
   ```
   The party of the first part hereby agrees to indemnify and hold 
   harmless the party of the second part from any and all claims, 
   damages, losses, and expenses arising out of or resulting from 
   the performance of this agreement.
   ```
   
   - Select simplification level (try "Basic")
   - Click "Simplify Document"
   - Wait 30-60 seconds (first run downloads models)

5. **View Results**
   - See side-by-side comparison
   - Check readability improvement
   - Read the summary
   - Hover over highlighted legal terms

---

## ⚙️ Verify Installation

Run the test script:
```bash
python test_installation.py
```

This checks:
- ✅ All packages installed
- ✅ spaCy model available
- ✅ NLTK data downloaded
- ✅ Database creation works
- ✅ Services initialize correctly

---

## 🐛 Troubleshooting

### Models Not Loading
**Problem**: "Model not found" error

**Solution**:
```bash
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('punkt')"
```

### Slow First Request
**Problem**: First simplification takes 1-2 minutes

**Reason**: AI models are downloading and loading

**Solution**: Wait for first request to complete. Subsequent requests will be much faster (5-10 seconds).

### Port Already in Use
**Problem**: "Address already in use" error

**Solution**: Change port in `app.py`:
```python
app.run(host='0.0.0.0', port=5001)  # Change 5000 to 5001
```

### Database Locked
**Problem**: Database errors

**Solution**: Delete `database.db` and restart:
```bash
del database.db  # Windows
rm database.db   # Linux/Mac
python app.py
```

---

## 📚 Sample Texts

Use the sample texts in `sample_texts.py` for testing:

```python
python sample_texts.py
```

Or import in Python:
```python
from sample_texts import SAMPLE_CONTRACT, SAMPLE_PRIVACY_POLICY
```

---

## 🎓 Next Steps

1. ✅ **Explore Admin Panel**: Add custom legal terms to glossary
2. ✅ **Try Different Levels**: Test Basic, Intermediate, Advanced
3. ✅ **Upload Files**: Try uploading .txt files
4. ✅ **Download Results**: Save simplified documents
5. ✅ **Check Dashboard**: View your simplification history

---

## 📖 Full Documentation

See [README.md](README.md) for:
- Complete feature list
- API documentation
- Deployment guides
- Architecture details

---

## 🆘 Need Help?

1. Check [README.md](README.md) troubleshooting section
2. Run `python test_installation.py`
3. Check console logs for errors
4. Verify all dependencies installed

---

**Made with ❤️ | Ready to Simplify Legal Language!**
