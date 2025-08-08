# GitHub Repository Setup Instructions

## 🚀 Quick Setup Guide

### Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `tiktok-sentiment-analyzer`
3. Description: `Real-time TikTok sentiment analysis with Python, Streamlit, and NLP`
4. Make it **Public** (for Vercel deployment)
5. **Don't** initialize with README (we already have one)
6. Click "Create repository"

### Step 2: Link Local Repository to GitHub
Copy and paste these commands in your terminal:

```bash
cd "d:\Alter PC - D\stuff\coding\tiktok-sentiment-analyzer"
git remote add origin https://github.com/YOUR_USERNAME/tiktok-sentiment-analyzer.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### Step 3: Deploy to Vercel
1. Go to https://vercel.com/
2. Sign in with GitHub
3. Click "New Project"
4. Import your `tiktok-sentiment-analyzer` repository
5. Set Framework Preset to "Other"
6. Configure build settings:
   - Build Command: `pip install -r requirements.txt`
   - Output Directory: Leave empty
   - Install Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

### Step 4: Environment Variables in Vercel
Add these environment variables in Vercel dashboard:
- `STREAMLIT_BROWSER_GATHER_USAGE_STATS` = `false`
- `STREAMLIT_SERVER_ENABLE_CORS` = `false`
- `STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION` = `false`

## 🎯 Alternative: Streamlit Cloud (Recommended)
1. Go to https://share.streamlit.io/
2. Connect your GitHub account
3. Deploy your `tiktok-sentiment-analyzer` repository
4. The app will be live at: `https://your-username-tiktok-sentiment-analyzer-app-123456.streamlit.app/`

## 📝 Repository Details
- **Name**: `tiktok-sentiment-analyzer`
- **Description**: `Real-time TikTok sentiment analysis with Python, Streamlit, and NLP`
- **Topics**: `python`, `streamlit`, `nlp`, `sentiment-analysis`, `tiktok`, `data-science`, `machine-learning`
- **License**: MIT

## ✅ Your Repository is Ready!
All files have been cleaned of personal/UK job market references and are ready for public deployment.

## 🚀 Live Demo Features
- Real-time API simulation
- Interactive sentiment analysis
- Professional data visualizations  
- Docker deployment ready
- Production-quality code

Perfect for showcasing your technical skills! 🎉
