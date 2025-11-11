# Deployment Guide for AgriAid on Render

This guide will help you deploy AgriAid to Render with Git LFS support for the large model file.

## Prerequisites

- [x] Git LFS installed and configured
- [x] GitHub repository with the code
- [ ] Render account (free tier available at https://render.com)

## Files Added for Deployment

1. **`render.yaml`** - Render configuration file
2. **`.gitattributes`** - Git LFS tracking configuration (already exists)
3. **`Procfile`** - Process file for starting the app
4. **`runtime.txt`** - Python version specification

## Deployment Steps

### Step 1: Push to GitHub with Git LFS

The model file is already tracked with Git LFS. Now push the deployment branch:

```bash
# Stage deployment configuration files
git add render.yaml Procfile runtime.txt DEPLOYMENT.md

# Commit the changes
git commit -m "Add Render deployment configuration"

# Push to GitHub (deployment branch)
git push -u origin deployment
```

**Note**: Your 200MB model file (`plant_disease_model_1_latest.pt`) is already tracked with Git LFS and will be handled properly.

### Step 2: Deploy on Render

#### Option A: Using render.yaml (Recommended)

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Blueprint"**
3. Connect your GitHub repository
4. Select the repository: `sairajB/agriAid`
5. Select branch: `deployment`
6. Render will automatically detect `render.yaml`
7. Click **"Apply"**

#### Option B: Manual Setup

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `agriaid`
   - **Branch**: `deployment`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: `Free` (or choose paid for better performance)
5. Click **"Create Web Service"**

### Step 3: Verify Deployment

1. Wait for the build to complete (may take 5-10 minutes for first deploy)
2. Render will provide a URL like: `https://agriaid.onrender.com`
3. Visit the URL to test your application
4. Upload a test image to verify the ML model works

## Troubleshooting

### Large Model File Issues

Your model file is tracked with Git LFS. Verify with:

```bash
git lfs ls-files
```

You should see `plant_disease_model_1_latest.pt` listed.

### Memory Issues

If the app crashes due to memory on free tier (512MB RAM):

1. **Upgrade to Starter plan** ($7/month) with 512MB-2GB RAM
2. **Optimize model loading** - ensure model is loaded only once at startup
3. **Use external storage** (see alternative below)

### Cold Starts

Free tier spins down after 15 minutes of inactivity:

- First request after idle will take ~30-60 seconds
- Upgrade to paid tier for always-on service

### Alternative: External Model Storage

If Git LFS causes issues, store the model externally:

1. Upload model to Google Drive/AWS S3/Hugging Face
2. Modify `app.py` to download on startup:

```python
import os
import requests
from pathlib import Path

MODEL_URL = "YOUR_DIRECT_DOWNLOAD_LINK"
MODEL_PATH = "plant_disease_model_1_latest.pt"

def download_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading model...")
        response = requests.get(MODEL_URL, stream=True)
        total_size = int(response.headers.get('content-length', 0))

        with open(MODEL_PATH, 'wb') as f:
            downloaded = 0
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                downloaded += len(chunk)
                print(f"Downloaded {downloaded}/{total_size} bytes", end='\r')
        print("\nModel downloaded!")

# Call before loading model
download_model()
```

## Environment Variables (Optional)

Set these in Render dashboard under "Environment":

- `SECRET_KEY` - Generate a secure random key
- `FLASK_ENV` - Set to `production`
- `MAX_CONTENT_LENGTH` - `16777216` (16MB upload limit)

Example for generating SECRET_KEY:

```python
import secrets
print(secrets.token_hex(32))
```

## Post-Deployment Checklist

- [ ] Test image upload functionality
- [ ] Verify disease prediction works
- [ ] Check marketplace page loads
- [ ] Test contact form
- [ ] Monitor logs for errors
- [ ] Set up custom domain (optional)
- [ ] Enable auto-deploy on git push

## Performance Tips

1. **Model Loading**: Ensure the model is loaded once at startup, not per request
2. **Image Processing**: Consider adding image size limits
3. **Caching**: Add caching for frequently accessed data
4. **CDN**: Use Render's CDN for static files

## Cost Estimation

- **Free Tier**:
  - 750 hours/month free
  - Spins down after 15 min inactivity
  - Good for testing/demos
- **Starter ($7/month)**:
  - Always on
  - Better for production
  - Faster performance

## Monitoring

Check application health:

- **Logs**: Available in Render dashboard
- **Metrics**: CPU, Memory usage visible in dashboard
- **Health Checks**: Configured to hit `/` endpoint

## Alternative Deployment Platforms

If Render doesn't work well:

1. **Google Cloud Run** - Better for large models, pay-per-use
2. **Fly.io** - Good free tier, persistent volumes
3. **AWS Elastic Beanstalk** - More control, free tier available
4. **Railway** - Similar to Render, easy deployment

## Support

For issues:

- Check [Render Status](https://status.render.com/)
- Review [Render Docs](https://render.com/docs)
- Check application logs in dashboard
- GitHub Issues for AgriAid-specific problems

---

**Ready to deploy!** 🚀

Push your changes and follow the steps above to get AgriAid live on Render.
