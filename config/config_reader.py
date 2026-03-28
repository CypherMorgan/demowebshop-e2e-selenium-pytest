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
        env = os.getenv("TEST_ENV", config["environment"])
        return config["environments"][env]

    @classmethod
    def get_base_url(cls):
        return os.getenv("BASE_URL", cls.get_env_config()["base_url"])

    @classmethod
    def get_username(cls):
        return os.getenv("TEST_USERNAME", cls.get_env_config()["username"])

    @classmethod
    def get_password(cls):
        return os.getenv("TEST_PASSWORD", cls.get_env_config()["password"])

    @classmethod
    def get_browser(cls):
        return os.getenv("BROWSER", cls.load_config()["browser"]["name"]).lower()

    @classmethod
    def is_headless(cls):
        headless_env = os.getenv("HEADLESS")

        if headless_env is not None:
            return headless_env.lower() == "true"

        return cls.load_config()["browser"]["headless"]

    @classmethod
    def get_implicit_wait(cls):
        return int(os.getenv("IMPLICIT_WAIT", cls.load_config()["settings"]["implicit_wait"]))

    @classmethod
    def get_explicit_wait(cls):
        return int(os.getenv("EXPLICIT_WAIT", cls.load_config()["settings"]["explicit_wait"]))