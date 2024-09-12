from flask import Flask
from flask.cli import AppGroup
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app)

cache_cli = AppGroup('cache')

@app.cli.command('clear')
def clear_cache():
    with app.app_context():
        cache.clear()
        print('Кэш успешно очищен')
