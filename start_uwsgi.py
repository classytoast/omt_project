import os
from dotenv import load_dotenv
import subprocess

# Путь к .env файлу
dotenv_path = os.path.join(os.path.dirname(__file__), 'config/.env')
load_dotenv(dotenv_path)

# Запуск uWSGI с использованием загруженных переменных окружения
subprocess.run(["uwsgi", "--ini", "uwsgi.ini"])

