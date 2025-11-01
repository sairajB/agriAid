# AgriAid - AI Plant Disease Detection

Deploy this Flask app to Render.com with these steps:

## Deployment Instructions

### 1. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/sairajB/agriAid.git
git push -u origin master
```

### 2. Deploy on Render

1. Go to [render.com](https://render.com) and sign up/login
2. Click **New +** → **Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `agriaid`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Free (or paid for better performance)

### 3. Environment Variables (Optional)

If needed, add in Render dashboard:

- `PYTHON_VERSION`: `3.11.0`
- `PORT`: `10000` (auto-set by Render)

### 4. Wait for Deployment

- First deployment takes 5-10 minutes (large PyTorch model)
- Render will automatically build and deploy
- You'll get a URL like: `https://agriaid.onrender.com`

## Notes

- Model file (200MB) is included in repo
- Free tier may have cold starts (30s delay after inactivity)
- Upgrade to paid plan for better performance and no cold starts

## Local Testing

```bash
pip install -r requirements.txt
python app.py
```

Visit: http://localhost:5000
