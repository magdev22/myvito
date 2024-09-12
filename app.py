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
    return render_template('user.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/clouds')
def clouds():
    return render_template('clouds.html')

@app.route('/auto')
def auto():
    return render_template('auto.html')

@app.route('/realty')
def realty():
    return render_template('realty.html')


if __name__ == '__main__':
    app.run(debug=True)