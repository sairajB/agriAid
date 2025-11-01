# AgriAid

![AgriAid Logo](static/images/logo.svg)

AgriAid is a cutting-edge web application designed to revolutionize plant care by leveraging artificial intelligence for disease identification and providing tailored supplement recommendations.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)
- [Contact](#contact)

## Features

- ** AI-Powered Disease Prediction**: Utilizes a state-of-the-art Convolutional Neural Network (CNN) to predict plant diseases from uploaded images with 95%+ accuracy.
- **💊 Smart Supplement Recommendations**: Provides tailored information and direct purchase links for plant care supplements based on identified diseases.
- **🎨 Modern, Responsive Design**: Beautiful, consistent UI with smooth animations and glassmorphism effects across all pages.
- **📝 Interactive Contact Form**: Easy-to-use form for submitting queries or feedback.
- **🛒 Integrated Marketplace**: Browse and purchase recommended fertilizers and treatment supplements seamlessly.
- **⚡ Fast & Lightweight**: Optimized performance with minimal dependencies for quick load times.

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3 (Tailwind CSS), JavaScript (GSAP Animations)
- **Machine Learning**: PyTorch (CNN model for disease classification)
- **Image Processing**: PIL (Pillow), torchvision
- **Data Processing**: Pandas, NumPy
- **Deployment**: Gunicorn

## Usage

1. **Home Page**: Visit the landing page to explore features and learn about AgriAid's capabilities.
2. **Disease Detection**:
   - Click "Get Started" to navigate to the detection page.
   - Upload a clear image of the affected plant (supports drag & drop).
   - Receive instant AI-generated diagnosis with treatment recommendations.
3. **View Results**:
   - See detailed disease information and prevention tips.
   - Get personalized supplement recommendations.
   - Click "Buy Product" to purchase recommended treatments.
4. **Marketplace**:
   - Browse fertilizers for healthy plants and supplements for disease treatment.
   - Filter by plant disease type.
   - Direct purchase links to verified suppliers.
5. **Contact**: Use the modern contact form for support, questions, or feedback.

## File Structure

```
🌱 AgriAid
│
├─� app.py                    # Main Flask application
├─🤖 CNN.py                    # CNN model architecture
├─🎯 plant_disease_model_1_latest.pt  # Trained model weights
├─� disease_info.csv          # Disease descriptions & prevention
├─� supplement_info.csv       # Product recommendations
├─� requirements.txt          # Python dependencies
├─📘 README.md                 # Documentation
│
├─📁 static
│ ├─🎨 styles
│ │ ├─ style_home.css         # Home page styles
│ │ ├─ sidebar.css            # Sidebar component styles
│ │ ├─ modern.css             # Modern UI utilities
│ │ └─ login_signup.css       # Form styles
│ ├─� js
│ │ └─ script.js              # Frontend interactions
│ ├─🖼️ images
│ │ └─ logo.svg               # AgriAid branding
│ └─� uploads                # User-uploaded images
│
└─📁 templates                 # HTML templates
  ├─� home.html              # Landing page
  ├─� main.html              # Disease detection page
  ├─📊 submit.html            # Results display
  ├─� market.html            # Product marketplace
  └─� contact.html           # Contact form

🔑 Legend:
📁 Folder    � Python File   🤖 ML Model   🎯 Weights
� Data      � Products      📋 Config     📘 Docs
🎨 CSS       💻 JavaScript    🖼️ Images     📤 Uploads
🏠 Pages     🔍 Detection     � Results    � Shop
```

## Contributing

We welcome contributions to AgriAid! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more information on how to get started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For support, feedback, or inquiries, please contact us:

- **Email**: sairaj.sab@gmail.com

---

Made with 💚 by the AgriAid Team
