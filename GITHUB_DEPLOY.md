# 🚀 GitHub Deployment - Step by Step

## Prerequisites

✅ Git installed (check with `git --version`)
✅ GitHub account (create at https://github.com/join)

## Step 1: Create GitHub Repository

1. Go to: https://github.com/new
2. Fill in:
   - **Repository name**: `contract-language-simplifier`
   - **Description**: `AI-powered web app that simplifies legal contracts`
   - **Visibility**: Public (for free Hugging Face deployment)
   - **DO NOT** initialize with README (we already have one)
3. Click "Create repository"
4. **Copy the repository URL** (looks like: `https://github.com/YOUR-USERNAME/contract-language-simplifier.git`)

## Step 2: Push Your Code to GitHub

Open terminal in your project folder and run these commands:

```bash
# Configure Git (first time only)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Add all files
git add .

# Commit
git commit -m "Initial commit: Contract Language Simplifier"

# Add remote (replace YOUR-USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR-USERNAME/contract-language-simplifier.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Enter your GitHub credentials when prompted.**

## Step 3: Deploy to Hugging Face Spaces

### Option A: Connect GitHub Repository (Recommended)

1. Go to: https://huggingface.co/new-space
2. Fill in:
   - **Owner**: Your username
   - **Space name**: `contract-simplifier`
   - **License**: MIT
   - **Select SDK**: Docker
   - **Space hardware**: CPU basic (free)
3. Click "Create Space"
4. In your new Space, click "Settings" → "Repository"
5. Click "Link to a GitHub repository"
6. Select your repository: `YOUR-USERNAME/contract-language-simplifier`
7. Click "Link repository"

### Option B: Manual Upload

1. Go to: https://huggingface.co/new-space
2. Create Space (same as above)
3. Click "Files" → "Add file" → "Upload files"
4. Drag and drop ALL files from your project
5. Click "Commit changes to main"

## Step 4: Configure Environment Variables

1. In your Hugging Face Space, go to "Settings"
2. Scroll to "Repository secrets"
3. Add these secrets:
   ```
   SECRET_KEY = your-secret-key-12345
   JWT_SECRET_KEY = your-jwt-secret-67890
   ```
4. Click "Save"

## Step 5: Wait for Build

- Hugging Face will automatically build your Docker container
- Watch the "Logs" tab
- Build takes 10-15 minutes
- When complete, you'll see: "Running on http://0.0.0.0:7860"

## Step 6: Access Your Live Website! 🎉

Your app will be live at:
```
https://huggingface.co/spaces/YOUR-USERNAME/contract-simplifier
```

## 🔄 Updating Your App

Whenever you make changes:

```bash
git add .
git commit -m "Description of changes"
git push
```

Hugging Face will automatically rebuild and redeploy!

## ✅ Verification

After deployment, test these features:
- [ ] Registration works
- [ ] Login works
- [ ] Text simplification works
- [ ] File upload works
- [ ] Admin dashboard accessible

## 🆘 Troubleshooting

**Build fails?**
- Check "Logs" tab in Hugging Face Space
- Ensure Dockerfile is present
- Verify requirements.txt is correct

**App doesn't start?**
- Check environment variables are set
- Look for errors in logs
- Ensure port 7860 is exposed in Dockerfile

**Models not loading?**
- First request takes 1-2 minutes (downloading models)
- Subsequent requests will be faster

## 📞 Need Help?

- GitHub Docs: https://docs.github.com
- Hugging Face Docs: https://huggingface.co/docs/hub/spaces

---

**Estimated Total Time**: 20-30 minutes
**Result**: Live website accessible 24/7 for FREE!
