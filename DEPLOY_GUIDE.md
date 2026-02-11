# 🚀 Deploy to Hugging Face Spaces - Quick Guide

## What is Hugging Face Spaces?

Hugging Face Spaces provides **FREE hosting** for AI applications. Your app will be available at:
`https://huggingface.co/spaces/YOUR-USERNAME/contract-simplifier`

## Step-by-Step Deployment

### 1. Create Hugging Face Account (Free)

1. Go to: https://huggingface.co/join
2. Sign up with email or GitHub
3. Verify your email

### 2. Create a New Space

1. Go to: https://huggingface.co/new-space
2. Fill in:
   - **Space name**: `contract-simplifier`
   - **License**: MIT
   - **SDK**: Docker
   - **Visibility**: Public (free) or Private (paid)
3. Click "Create Space"

### 3. Upload Your Files

You have two options:

#### Option A: Git Upload (Recommended)

1. Install Git: https://git-scm.com/downloads
2. Open terminal in your project folder
3. Run these commands:

```bash
# Login to Hugging Face
git lfs install
huggingface-cli login

# Initialize and push
git init
git add .
git commit -m "Initial commit"
git remote add origin https://huggingface.co/spaces/YOUR-USERNAME/contract-simplifier
git push -u origin main
```

#### Option B: Web Upload (Easier)

1. Go to your Space: `https://huggingface.co/spaces/YOUR-USERNAME/contract-simplifier`
2. Click "Files" tab
3. Click "Add file" → "Upload files"
4. Upload ALL files from your project folder:
   - `app.py`
   - `config.py`
   - `models.py`
   - `requirements.txt`
   - `Dockerfile`
   - `docker-compose.yml`
   - `.env.example`
   - All folders: `templates/`, `services/`, `static/`
5. Rename `README_HF.md` to `README.md` and upload it
6. Click "Commit changes to main"

### 4. Configure Environment Variables

1. In your Space, click "Settings"
2. Scroll to "Repository secrets"
3. Add these secrets:
   - `SECRET_KEY`: `your-secret-key-12345`
   - `JWT_SECRET_KEY`: `your-jwt-secret-67890`
4. Save

### 5. Wait for Build

- Hugging Face will automatically build your Docker container
- This takes 10-15 minutes (first time)
- Watch the "Logs" tab for progress
- When you see "Running on http://0.0.0.0:7860", it's ready!

### 6. Access Your App

Your app will be live at:
```
https://huggingface.co/spaces/YOUR-USERNAME/contract-simplifier
```

## 🎉 That's It!

Your Contract Language Simplifier is now hosted for FREE!

## Alternative: Streamlit Cloud

If Hugging Face doesn't work, try Streamlit Cloud:

1. Go to: https://streamlit.io/cloud
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Set main file: `app.py`
6. Deploy!

## Need Help?

- Hugging Face Docs: https://huggingface.co/docs/hub/spaces
- Streamlit Docs: https://docs.streamlit.io/streamlit-community-cloud

---

**Estimated Time**: 15-20 minutes
**Cost**: FREE
**Your app will be online 24/7!**
