import dotenv
import os


class Config:
    def __init__(self, env_path: str | None = None) -> None:
        dotenv.load_dotenv(env_path) # type: ignore
        self.TOKEN = os.environ['TOKEN']
        self.MESSAGES_STORAGE = os.environ['MESSAGES_STORAGE']
        self.QUEUES_STORAGE = os.environ['QUEUES_STORAGE']
    