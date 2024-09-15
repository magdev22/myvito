from flask import Flask, flash, redirect, render_template, request, url_for

from werkzeug.security import check_password_hash

from models import db, User, Auto, Chat, Clouds, Realty

app = Flask(__name__)

app.secret_key = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# связываем приложение с базой данных

db.init_app(app)

@app.route('/')
def index():
    users = User.query.all()
    autos = Auto.query.all()
    chat = Chat.query.all()
    clouds = Clouds.query.all()
    realty = Realty.query.all()
    return render_template('index.html', users=users, autos=autos, chat=chat, clouds=clouds, realty=realty)

@app.route('/user')
def user():
    users = User.query.all()
    return render_template('user.html', users=users)

@app.route('/chat')
def chat():
    chat = Chat.query.all()
    return render_template('chat.html', chat=chat)

@app.route('/clouds')
def clouds():
    clouds = Clouds.query.all()
    return render_template('clouds.html', clouds=clouds)

@app.route('/auto')
def auto():
    autos = Auto.query.all()
    return render_template('auto.html', autos=autos)

@app.route('/realty')
def realty():
    realty = Realty.query.all()
    return render_template('realty.html', realty=realty)

@app.route('/login', methods=['GET', 'POST'])
def login():
     if request.method == 'GET':
        return render_template('login.html', realty=realty)
     if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            # Здесь вы можете выполнить дополнительные действия при успешной аутентификации
            flash('Успешный вход!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Неверный логин или пароль', 'error')
            return redirect(url_for('login_form'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Пользователь с таким именем уже существует', 'error')
            return redirect(url_for('register'))
        else:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            flash('Регистрация прошла успешно', 'success')
            return redirect(url_for('register'))


if __name__ == '__main__':
    app.run(debug=True)