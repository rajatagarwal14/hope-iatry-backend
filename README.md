# 🌟 Hope-iatry AI Coaching Platform - Complete Setup Guide

## 📋 Overview

This is a complete, production-ready AI coaching platform for Hope-iatry with:
- ✅ Life Wellness Coach chatbot
- ✅ Career Coach chatbot  
- ✅ User registration system
- ✅ Built-in clinical content guardrails
- ✅ Admin dashboard with user management
- ✅ CSV export functionality
- ✅ Your company logo integrated
- ✅ Real Claude AI integration

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Install Python (if not already installed)

**Windows:**
1. Download from: https://www.python.org/downloads/
2. Run installer and CHECK "Add Python to PATH"
3. Open Command Prompt and verify: `python --version`

**Mac/Linux:**
Python usually comes pre-installed. Verify: `python3 --version`

---

### Step 2: Install Dependencies

Open Terminal/Command Prompt in the project folder:

```bash
# Install required packages
pip install -r requirements.txt

# Or use pip3 on Mac/Linux
pip3 install -r requirements.txt
```

---

### Step 3: Get Your Groq API Key (FREE!)

1. Go to: https://console.groq.com/
2. Sign up with Google/GitHub (takes 30 seconds)
3. Go to "API Keys" section
4. Create a new API key
5. Copy the key (it starts with `gsk_...`)

**Why Groq?**
- ✅ **FREE** - No credit card required
- ✅ **FAST** - Up to 10x faster than other APIs
- ✅ **High Quality** - Uses Llama 3.1 70B model
- ✅ **Easy Setup** - Same as OpenAI API format

---

### Step 4: Configure API Key

Create a file named `.env` in the project folder:

```bash
# On Windows
copy .env.example .env

# On Mac/Linux
cp .env.example .env
```

Open `.env` and paste your API key:

```
GROQ_API_KEY=gsk-your-actual-key-here
```

**⚠️ Important:** Never share your `.env` file or commit it to git!

---

### Step 5: Run the Server

```bash
# Start the backend server
python backend.py

# Or on Mac/Linux
python3 backend.py
```

You should see:
```
🌟 Hope-iatry AI Coaching Platform - Backend Server
✅ Groq API Key configured
✅ Model: llama-3.1-70b-versatile
📡 Server Configuration:
   • Local access: http://127.0.0.1:5000
   • Network access: http://YOUR_IP_ADDRESS:5000
🚀 Starting server...
```

---

### Step 6: Open the App

**On your computer:**
Open your browser and go to: `http://localhost:5000`

**On other devices (same network):**
1. Find your computer's IP address
2. Go to: `http://YOUR_IP_ADDRESS:5000`

---

## 🌐 How to Let Others Access Your App

### Find Your IP Address

**Windows:**
```bash
ipconfig
# Look for "IPv4 Address" under your active network
# Example: 192.168.1.100
```

**Mac:**
```bash
ifconfig | grep "inet "
# Look for the 192.168.x.x address
```

**Linux:**
```bash
hostname -I
# Or: ip addr show
```

### Share the URL

Once you have your IP (e.g., `192.168.1.100`), others can access:

```
http://192.168.1.100:5000
```

**Requirements:**
- ✅ Same WiFi network
- ✅ Server running on your computer
- ✅ Firewall allows port 5000 (see troubleshooting below)

---

## 🖥️ Using VSCode (Recommended)

### Step 1: Open in VSCode

```bash
code .
```

Or: File → Open Folder → Select the `hope-iatry-backend` folder

### Step 2: Open Terminal in VSCode

View → Terminal (or Ctrl+` / Cmd+`)

### Step 3: Run Commands

All the commands above work in VSCode's integrated terminal!

---

## 📱 Demo Guide for Client

### User Journey Demo:

1. **Registration**
   - Fill in name, email, phone, address
   - Check consent box
   - Click "Register & Start Coaching"

2. **Choose Coach**
   - Life Wellness Coach: For daily habits, stress, wellness
   - Career Coach: For resumes, interviews, job search

3. **Test Wellness Coaching**
   - "I'm feeling stressed at work"
   - "How can I sleep better?"
   - "I want to build better habits"

4. **Test Career Coaching**
   - "Help me improve my resume"
   - "I have an interview next week"
   - "How do I change careers?"

5. **Test Guardrails** (This will flag the user)
   - Type: "I'm feeling depressed"
   - See immediate redirect to licensed services
   - User is automatically flagged in admin dashboard

6. **Admin Dashboard**
   - Click "Admin Login" at bottom
   - Password: `admin123`
   - See all users and flagged users
   - Export to CSV

---

## 🔧 Troubleshooting

### Problem: "Module not found" error

**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

### Problem: "Port 5000 already in use"

**Solution:**
```bash
# Change port in backend.py (last line):
app.run(host='0.0.0.0', port=5001, debug=True)

# Then access at: http://localhost:5001
```

### Problem: Others can't access on network

**Solution 1 - Windows Firewall:**
1. Search "Windows Defender Firewall"
2. Click "Allow an app through firewall"
3. Click "Change settings" → "Allow another app"
4. Browse to Python.exe
5. Check both "Private" and "Public"

**Solution 2 - Mac Firewall:**
1. System Preferences → Security & Privacy → Firewall
2. Click "Firewall Options"
3. Add Python to allowed apps

**Solution 3 - Check if server is accessible:**
```bash
# On your computer, test:
curl http://localhost:5000/health

# From another device, test:
curl http://YOUR_IP_ADDRESS:5000/health
```

### Problem: "API key not configured" error

**Solution:**
1. Make sure `.env` file exists (not `.env.example`)
2. Open `.env` and check API key is correct (starts with `gsk_`)
3. No spaces around the `=` sign
4. Restart the server after changing `.env`

### Problem: Chat gives errors

**Check:**
1. Is backend server running? (Terminal should show activity)
2. Is API key valid? (Check console.groq.com)
3. Open browser console (F12) to see detailed errors

---

## 📊 File Structure

```
hope-iatry-backend/
├── backend.py           # Flask server (backend)
├── requirements.txt     # Python dependencies
├── .env                 # Your API key (DON'T SHARE!)
├── .env.example         # Template for .env
├── README.md           # This file
└── static/
    ├── index.html      # Frontend app
    └── logo.png        # Your Hope-iatry logo
```

---

## 🔒 Security Notes

### For Demo/MVP:
- ✅ Current setup is fine for local demos
- ✅ Data stored in memory (resets when server restarts)
- ✅ Admin password is hardcoded for demo

### For Production (If You Deploy):
You'll need:
- Real database (PostgreSQL, MySQL)
- Proper authentication (JWT, sessions)
- HTTPS/SSL certificate
- Environment variable management
- Rate limiting
- Input validation/sanitization

---

## 💡 Tips for Best Demo

1. **Prepare Test Scenarios:**
   - Have 2-3 wellness questions ready
   - Have 2-3 career questions ready
   - Test the guardrails with clinical keyword

2. **Show the Full Flow:**
   - Registration → Chat → Admin Dashboard → Export

3. **Highlight Key Features:**
   - AI gives specific, actionable advice
   - Automatic clinical detection
   - User flagging for outreach
   - Contact info collection

4. **Have Your Logo Visible:**
   - It's already integrated at the top!

---

## 🆘 Need Help?

### Common Issues:

**"Connection refused" in browser:**
- Make sure backend server is running
- Check URL is correct (http://localhost:5000)

**"API Error 401":**
- API key is invalid or expired
- Get new key from console.groq.com

**Chat not responding:**
- Check backend terminal for errors
- Verify API key in `.env` (should start with `gsk_`)
- Check internet connection

---

## 📝 Admin Credentials

**Password:** `admin123`

**To change:** Edit `backend.py` line where it checks password in the `/api/admin/users` route

---

## 🎯 What's Next?

For production deployment, consider:
1. **Database:** PostgreSQL or MongoDB
2. **Hosting:** AWS, DigitalOcean, Heroku
3. **Domain:** Get a proper domain name
4. **Email:** Integrate email notifications
5. **Analytics:** Add usage tracking

---

## 📞 Support

If you have questions or issues:
1. Check this README carefully
2. Check the Troubleshooting section
3. Look at terminal/console for error messages
4. Verify all steps were followed exactly

---

## ✅ Success Checklist

- [ ] Python installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created with API key
- [ ] Server starts without errors
- [ ] Can access http://localhost:5000
- [ ] Can register a user
- [ ] Chat works and responds
- [ ] Guardrails redirect clinical topics
- [ ] Admin dashboard shows users
- [ ] Can export to CSV

**All checked? You're ready to demo! 🎉**
