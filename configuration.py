import yaml
import os

class Config:
    def read_yaml():
        with open(f"{os.getcwd()}/config.yml", "r") as f:
            return yaml.safe_load(f)

config = Config.read_yaml()