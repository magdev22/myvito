# import unittest
# from app import app, db, User, Auto, Chat, Clouds, Realty

# class TestApp(unittest.TestCase):

#     def setUp(self):
#         app.config['TESTING'] = True
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/test_database'
#         app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#         self.client = app.test_client()

#         with app.app_context():
#             db.create_all()

#     def tearDown(self):
#         with app.app_context():
#             db.drop_all()

#     def test_index_page(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)

#     def test_user_page(self):
#         response = self.client.get('/user')
#         self.assertEqual(response.status_code, 200)

#     def test_chat_page(self):
#         response = self.client.get('/chat')
#         self.assertEqual(response.status_code, 200)

#     def test_clouds_page(self):
#         response = self.client.get('/clouds')
#         self.assertEqual(response.status_code, 200)

#     def test_auto_page(self):
#         response = self.client.get('/auto')
#         self.assertEqual(response.status_code, 200)

#     def test_realty_page(self):
#         response = self.client.get('/realty')
#         self.assertEqual(response.status_code, 200)

#     def test_login_route(self):
#         response = self.client.post('/login', data={'username': 'name1', 'password': '111'})
#         decoded_response = response.data.decode('utf-8')
#         self.assertIn('Неверный логин или пароль', decoded_response)  # Проверяем сообщение об ошибке входа
#         self.assertNotIn('Успешный вход!', decoded_response)  # Убедимся, что сообщения об успешном входе нет
#     def test_register_route(self):
#         response = self.client.post('/register', data={'username': 'test_user', 'password': 'test_password'})
#         decoded_response = response.data.decode('utf-8')
#         self.assertIn('Регистрация прошла успешно', decoded_response)

# if __name__ == '__main__':
#     unittest.main()

