import os
from flask import Flask, render_template, request, redirect, url_for,flash,session
from PIL import Image
import torchvision.transforms.functional as TF
import CNN
import numpy as np
import torch
import pandas as pd
import bcrypt
from flask_mysqldb import MySQL, MySQLdb



disease_info = pd.read_csv('disease_info.csv' , encoding='cp1252')
supplement_info = pd.read_csv('supplement_info.csv',encoding='cp1252')

model = CNN.CNN(39)    
model.load_state_dict(torch.load("plant_disease_model_1_latest.pt"))
model.eval()

def prediction(image_path):
    image = Image.open(image_path)
    image = image.resize((224, 224))
    input_data = TF.to_tensor(image)
    input_data = input_data.view((-1, 3, 224, 224))
    output = model(input_data)
    output = output.detach().numpy()
    index = np.argmax(output)
    return index


app = Flask(__name__)

app.secret_key = os.urandom(24)
mysql = MySQL()

app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'agriaid'
app.config['MYSQL_HOST'] = 'localhost'


mysql.init_app(app)



@app.route('/') 
def home_page():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')
        password_repeat = request.form.get('repeat_password')

        errors = []

        if not all([firstname, lastname, email, password, password_repeat]):
            errors.append("All fields are required")
        if '@' not in email or '.' not in email:
            errors.append("Email is not valid")
        if len(password) < 8:
            errors.append("Password must be at least 8 characters long")
        if password != password_repeat:
            errors.append("Password does not match")

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users_signup WHERE email = %s", (email,))
        result = cur.fetchone()
        
        if result:
            errors.append("Email already exists!")

        if errors:
            return render_template('signup.html', errors=errors)
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            cur.execute("INSERT INTO users_signup (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)",
                        (firstname, lastname, email, hashed_password))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('login'))

    return render_template('signup.html')

    



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        errors = []

        if not all([email, password]):
            errors.append("All fields are required")
        if '@' not in email or '.' not in email:
            errors.append("Email is not valid")

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM users_signup WHERE email = %s", (email,))
        result = cur.fetchone()
        cur.close()
        if not result:
            errors.append("Email does not exist!")
        elif not bcrypt.checkpw(password.encode('utf-8'), result['password'].encode('utf-8')):
            errors.append("Invalid email or password!")

        if errors:
            return render_template('login.html', errors=errors)
        else:
            session['user_id'] = result['user_id']
            flash('Login successful!', 'success')
            return redirect(url_for('main'))

    return render_template('login.html')


@app.route('/main')
def main():
    return render_template('main.html')



    
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        image = request.files.get('image')
        if image is None:
            # User did not upload an image, display an error message
            flash('Please upload an image before pressing Detect Disease.')
            return redirect(request.url)
        image = request.files['image']
        filename = image.filename
        file_path = os.path.join('static/uploads', filename)
        image.save(file_path)
        print(file_path)
        pred = prediction(file_path)
        title = disease_info['disease_name'][pred]
        description =disease_info['description'][pred]
        prevent = disease_info['Possible Steps'][pred]
        image_url = disease_info['image_url'][pred]
        supplement_name = supplement_info['supplement name'][pred]
        supplement_image_url = supplement_info['supplement image'][pred]
        supplement_buy_link = supplement_info['buy link'][pred]
        return render_template('submit.html' , title = title , desc = description , prevent = prevent , 
                               image_url = image_url , pred = pred ,sname = supplement_name , simage = supplement_image_url , buy_link = supplement_buy_link)
    


@app.route('/market', methods=['GET', 'POST'])
def market():
    return render_template('market.html', supplement_image = list(supplement_info['supplement image']),
                           supplement_name = list(supplement_info['supplement name']), disease = list(disease_info['disease_name']), buy = list(supplement_info['buy link']))
        
        
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out!', 'success')
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form.get('email')
        message = request.form.get('message')

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT user_id FROM users_signup WHERE email = %s", (email,))
        result = cur.fetchone()

        if result:
            id = result['user_id']
        else:
            cur.execute("INSERT INTO ContactFormSubmissions (UserID, Email, Message) VALUES (%s, %s, %s)", (id, email, message))
            mysql.connection.commit()
            cur.close()
        return redirect(url_for('contact'))

    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)
