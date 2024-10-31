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

- **🔐 User Authentication**: Secure signup and login functionality.
- **🔍 AI-Powered Disease Prediction**: Utilizes a state-of-the-art Convolutional Neural Network (CNN) to predict plant diseases from uploaded images.
- **💊 Smart Supplement Recommendations**: Provides tailored information and purchase links for plant care supplements based on identified diseases.
- **👤 Personalized User Profiles**: Manage your profile and maintain a detailed plant care journal.
- **📝 Interactive Contact Form**: Easy-to-use form for submitting queries or feedback.
- **🛒 Integrated Marketplace**: Browse and purchase recommended plant care products seamlessly.

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **Machine Learning**: PyTorch (CNN model)
- **Authentication**: Flask-Login
- **Form Handling**: Flask-WTF
- **ORM**: Flask-SQLAlchemy

## Usage

1. **Home Page**: Visit the landing page to explore main features and navigate the app.
2. **Sign Up/Login**: Create an account or log in to access personalized features.
3. **Disease Prediction**:
   - Navigate to the "Predict" page.
   - Upload a clear image of the affected plant part.
   - Receive an AI-generated diagnosis and care recommendations.
4. **Marketplace**:
   - Browse the "Market" section for recommended supplements.
   - Add items to cart and proceed to checkout.
5. **User Profile**:
   - Update personal information.
   - View and manage your plant care journal.
   - Track order history and saved predictions.
6. **Contact**: Use the contact form for support or feedback.

## File Structure

```
🌱 AgriAid
│
├─📁 app
│ ├─🐍 __init__.py
│ ├─🗄️ models.py
│ │
│ ├─📁 routes
│ │ ├─🐍 __init__.py
│ │ ├─🔐 auth.py
│ │ ├─🌿 main.py
│ │ └─🔌 api.py
│ │
│ ├─📁 static
│ │ ├─🎨 css
│ │ ├─💻 js
│ │ └─🖼️ images
│ │
│ ├─📁 templates
│ │ ├─🏗️ base.html
│ │ ├─🏠 home.html
│ │ ├─🔍 predict.html
│ │ └─ ...
│ │
│ └─📁 utils
│   ├─🐍 __init__.py
│   └─🛠️ helpers.py
│
├─📁 migrations
├─🧪 tests
├─🌐 venv
├─🙈 .gitignore
├─⚙️ config.py
├─📋 requirements.txt
├─🏃 run.py
└─📘 README.md

🔑 Legend:
📁 Folder    🐍 Python     🗄️ Database  🔐 Auth
🌿 Routes    🔌 API        🎨 CSS       💻 JavaScript
🖼️ Images    🏗️ Templates  🧪 Tests     🌐 Virt Env
⚙️ Config    📋 Deps       🏃 Runner    📘 Docs
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
