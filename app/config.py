import toml


class Config:
    def __init__(self, config_file_path="config.toml"):
        self.config_file_path = config_file_path
        self.data = None
        self.load_config()

    def load_config(self):
        try:
            with open(self.config_file_path, "r") as f:
                self.data = toml.load(f)
        except FileNotFoundError:
            print("Config file not found.")

    def get(self, section, key, default=None):
        if self.data and section in self.data and key in self.data[section]:
            return self.data[section][key]
        return default


config = Config()


# Database
db_name = config.get("database", "name", "postgresql")
db_host = config.get("database", "host", "localhost")
db_port = config.get("database", "port", 5432)
db_user = config.get("database", "user", "user")
db_password = config.get("database", "password", "password")
db_database = config.get("database", "database", "database")

# App
host = config.get("app", "host", "localhost")
port = config.get("app", "port", 8080)
debug_mode = config.get("app", "debug_mode", True)

# Keys
api_key = config.get("keys", "api", "key")
secret_key = config.get("keys", "secret", "key")
weather_api_key = config.get("keys", "weather_api", "key")




