from src.config.server import Server
from src.resources.resources import app

server = Server(app=app)

if __name__ == '__main__':
    server.run()
