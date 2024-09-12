from flask import Flask, render_template

from models import db, User, Auto, Chat, Clouds, Realty

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)