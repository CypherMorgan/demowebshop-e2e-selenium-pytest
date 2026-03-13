import yaml
import os


class ConfigReader:

    _config = None

    @classmethod
    def load_config(cls):

        if cls._config is None:
            path = os.path.join(os.path.dirname(__file__), "config.yaml")

            with open(path, "r") as file:
                cls._config = yaml.safe_load(file)

        return cls._config

    @classmethod
    def get_env_config(cls):

        config = cls.load_config()
        env = config["environment"]
        return config["environments"][env]

    @classmethod
    def get_base_url(cls):
        return cls.get_env_config()["base_url"]

    @classmethod
    def get_username(cls):
        return cls.get_env_config()["username"]

    @classmethod
    def get_password(cls):
        return cls.get_env_config()["password"]

    @classmethod
    def get_browser(cls):
        return cls.load_config()["browser"]["name"]

    @classmethod
    def is_headless(cls):
        return cls.load_config()["browser"]["headless"]

    @classmethod
    def get_implicit_wait(cls):
        return cls.load_config()["settings"]["implicit_wait"]

    @classmethod
    def get_explicit_wait(cls):
        return cls.load_config()["settings"]["explicit_wait"]
