import os


import yaml
config_path = "config.yml"


def load_db_config():
    if not os.path.exists(config_path):
        raise FileNotFoundError("Credentials not found")
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config


config = load_db_config()


class Settings:
    PROJECT_NAME: str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"
    POSTGRES_USER: str = config["database"]["POSTGRES_USER"]
    POSTGRES_PASSWORD = config["database"]["POSTGRES_PASSWORD"]
    POSTGRES_SERVER: str = config["database"]["POSTGRES_HOST"]
    POSTGRES_PORT: str = config["database"]["POSTGRES_PORT"]
    POSTGRES_DB: str = config["database"]["POSTGRES_DB"]
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SECRET_KEY: str = config["database"]["SECRET_KEY"]
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


settings = Settings()
