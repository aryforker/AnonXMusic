from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "8154886"))
        self.API_HASH = getenv("API_HASH", "d2976cd3599122c571f8e5afd54c6d04")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "8039894426:AAFrF0vmmpiqW8YKp99Ix96b52CYopucaqg")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Aryana:1234567890@cluster0.eblez.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1003261133706"))
        self.OWNER_ID = int(getenv("OWNER_ID", "970535949"))

        self.SESSION1 = getenv("SESSION", "BAB8bwYAP6bT5exAX2beZ7MXsWB-4crm7Vrl8hE7SWDHQb75o2QqeDDDmwb3NwunyksjEx7-GltybYHEvuEhz0uty5-cdk-9hrcEiu9WXCr6L0JVAmCuUJnqD89Cy0cFCyGyyVDmfy96m8xi5Uc7iEIGN3NYY9_YaVcjreCwCgzgpqQHvHoFtCBX2YQfMc_WHTS5EvtPgtDivfFsiDglWuQyXTzqZy9IWCClhtK1VgCw5B9EFC5JOTqChJIQ8jI0Wn6p07CzCDJEIifMaIJT17kNE8Dj0WnP6Kjvsxz3PjV8Ef1J4qkDLlqoXfMTM_5szyySHhGrHgt72akUmX5s0wCBhYy7aQAAAAGzkOFJAA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/The_Aryana_PY")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/The_Aryana_PY")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
