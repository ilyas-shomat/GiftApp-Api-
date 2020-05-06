import os
from src.app import create_app

if __name__ == '__main__':
  env_name = 'development'
  app = create_app(env_name)

  app.run(host='0.0.0.0', port=8080)