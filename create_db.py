from flask import Flask

from models import db, User, Auto, Chat, Clouds, Realty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        user1 = User(username='name1', password='111')
        user2 = User(username='name2', password='222')
        db.session.add_all([user1, user2])
        db.session.commit()

        auto1 = Auto(mark='mark1', model='model1', year=1, price=1, user=user1)
        auto2 = Auto(mark='mark2', model='model2', year=2, price=2, user=user2)
        db.session.add_all([auto1, auto2])
        db.session.commit()

        chat1 = Chat(message='message1', time='time1', user=user1)
        chat2 = Chat(message='message2', time='time2', user=user2)
        db.session.add_all([chat1, chat2])
        db.session.commit()

        cloud1 = Clouds(title='title1', price=1, user=user1)
        cloud2 = Clouds(title='title2', price=2, user=user2)
        db.session.add_all([cloud1, cloud2])
        db.session.commit()

        realty1 = Realty(title='недвига1', room=1, price=1, user=user1)
        realty2 = Realty(title='недвига2', room=2, price=2, user=user2)
        db.session.add_all([realty1, realty2])
        db.session.commit()