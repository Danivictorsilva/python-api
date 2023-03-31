class Server:
    def __init__(self, app):
        self.app = app

    def run(self):
        self.app.run(debug=True, port=5000, host='0.0.0.0')
