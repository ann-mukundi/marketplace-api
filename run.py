import os
from app import create_app

config_env = os.getenv('APP_SETTINGS')
app = create_app(config_env)

if __name__ == '__main__':
    app.run()
