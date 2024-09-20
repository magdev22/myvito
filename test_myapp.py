import unittest
from app import app, db, User, Auto, Chat, Clouds, Realty

# Импортируем необходимые модули для написания и запуска тестов

class TestApp(unittest.TestCase):

    # Создаем класс тестов, наследуемый от unittest.TestCase

    def setUp(self):
        # Метод setUp выполняется перед запуском каждого теста

        app.config['TESTING'] = True
        # Устанавливаем конфигурацию приложения для режима тестирования

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        # Устанавливаем временную базу данных SQLite в памяти для тестирования

        self.app = app.test_client()
        # Создаем тестового клиента для взаимодействия с приложением

        with app.app_context():
            db.create_all()
        # Создаем все таблицы в базе данных для тестирования

    def tearDown(self):
        # Метод tearDown выполняется после завершения каждого теста

        with app.app_context():
            db.drop_all()
        # Удаляем все таблицы из базы данных после завершения теста

    def test_index_route(self):
        # Тест проверяет корректность ответа при обращении к маршруту '/'

        response = self.app.get('/')
        # Отправляем GET-запрос на маршрут '/'

        self.assertEqual(response.status_code, 200)
        # Проверяем, что код ответа равен 200 (успешный запрос)


def test_login_route(self):
    response = self.app.post('/login', data=dict(username='testuser', password='testpassword'), follow_redirects=True)
    decoded_response = response.data.decode('utf-8')
    self.assertIn('Неверный логин или пароль', decoded_response)  # Проверяем сообщение об ошибке входа
    self.assertNotIn('Успешный вход!', decoded_response)  # Убедимся, что сообщения об успешном входе нет


    def test_register_route(self):
        response = self.app.post('/register', data=dict(username='newuser', password='newpassword'), follow_redirects=True)
        decoded_response = response.data.decode('utf-8')
        self.assertIn('Регистрация прошла успешно', decoded_response)
        # Проверяем, что в ответе содержится сообщение 'Регистрация прошла успешно'

if __name__ == '__main__':
    unittest.main()
# Запускаем тесты, если скрипт запускается напрямую
