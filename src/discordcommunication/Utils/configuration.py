import os
from dotenv import load_dotenv

load_dotenv()

class Configuration:
    def __init__(self):
        self.webhook_url = os.environ.get("webhook_url")
        self.port = os.environ.get("port")
        self.host = os.environ.get("host")
        self.debug = os.environ.get("debug")
        