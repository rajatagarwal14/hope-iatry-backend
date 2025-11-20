# 🚀 Deployment Guide - Hope-iatry Backend

Your team can access this from anywhere! Here are the easiest options:

---

## ⚡ Option 1: Render.com (RECOMMENDED - FREE & EASIEST)

**Why Render?**
- ✅ **100% FREE** for small apps
- ✅ Auto-deploys from GitHub
- ✅ HTTPS automatically
- ✅ Global access
- ✅ Zero configuration needed

### Steps:

1. **Push to GitHub:**
   ```bash
   cd /Users/rajat/Downloads/MPVHOPE/hope-iatry-backend
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Deploy on Render:**
   - Go to: https://render.com
   - Sign up (free)
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Use these settings:
     - **Name**: `hope-iatry-backend`
     - **Environment**: `Python`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn backend:app`
     - **Add Environment Variable**: 
       - Key: `GROQ_API_KEY`
       - Value: `YOUR_GROQ_API_KEY` (from your .env file)
   
3. **Done!** You'll get a URL like: `https://hope-iatry-backend.onrender.com`

---

## 🌐 Option 2: ngrok (INSTANT - For Testing)

**Perfect for quick testing!**

### Steps:

1. **Install ngrok:**
   ```bash
   brew install ngrok
   ```

2. **Sign up for free:**
   - Go to: https://ngrok.com/
   - Copy your auth token

3. **Run ngrok:**
   ```bash
   ngrok config add-authtoken YOUR_TOKEN
   ngrok http 5001
   ```

4. **Share the URL!** 
   - You'll get: `https://abc123.ngrok.io`
   - Share this with your team
   - ⚠️ URL changes when you restart

---

## ☁️ Option 3: Railway.app (FREE & FAST)

1. Go to: https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub"
4. Select your repo
5. Add environment variable: `GROQ_API_KEY`
6. Deploy! Get URL like: `https://your-app.railway.app`

---

## 🐳 Option 4: Heroku (Classic Choice)

1. Install Heroku CLI: `brew install heroku`
2. Login: `heroku login`
3. Create app: `heroku create hope-iatry-backend`
4. Set env: `heroku config:set GROQ_API_KEY=your_key`
5. Deploy: `git push heroku main`

---

## 📦 What You Need to Add First

Create `gunicorn` requirement (for production):

```bash
echo "gunicorn==21.2.0" >> requirements.txt
```

Also create a `Procfile` for some platforms:

```bash
echo "web: gunicorn backend:app" > Procfile
```

---

## 🎯 Quick Start Recommendation

**For immediate testing:** Use **ngrok** (takes 2 minutes)
**For permanent hosting:** Use **Render.com** (takes 5 minutes, free forever)

---

## 🔒 Security Notes

- ✅ Your Groq API key is already configured
- ✅ CORS is enabled (cross-origin requests work)
- ⚠️ For production, consider:
  - Adding rate limiting
  - Using a proper database (not in-memory)
  - Adding authentication for admin endpoints

---

## 🆘 Need Help?

Run this command for instant ngrok deployment:
```bash
./deploy_ngrok.sh
```

(I'll create this script for you!)
