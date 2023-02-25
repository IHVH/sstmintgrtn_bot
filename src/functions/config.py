import os
import pydoc
import yaml
import logging


logger = logging.Logger(__name__)

CONFIG_FOLDER = '../../config'

URL = "url"
TOKEN = "token"

NEGATIVE = "negative"
STEPS = "steps"
WIDTH = "width"
HEIGHT = "height"
SHOW_PROGRESS_PREVIEW = "show_progress_preview"
SHOW_PROGRESS = "show_progress"
UPSCALE = "upscale"
GEN_CMD = "gen_cmd"
SAVE_FOLDER = "save_folder"
IMG2IMG_DENOISING_STRENGTH = "img2img_denoising_strength"
IMG2IMG_DEFAULT_PROMPT = "img2img_default_prompt"


class NotFoundException(Exception):
    pass


class ConfigNeural:
    __slots__ = ("__conf_node", "__file")

    def __init__(self, file: str) -> None:
        logger.info(f"Load neural config, file - {file}")
        self.__file = file
        self.__conf_node = yaml.load(open(self.__file, "r", encoding="utf-8"), Loader=yaml.SafeLoader)

    def get_neural_config(self):
        return self.__conf_node

    def get_neural_setting(self, setting: str):
        items = self.get_neural_config()
        for i in items:
            if i["code"] == setting:
                return i
        raise NotFoundException()

    def get_neural_setting_value(self, setting: str):
        return self.get_neural_setting(setting)["value"]

    def set_neural_setting_value(self, setting_code, value):
        setting = self.get_neural_setting(setting_code)
        logger.info(f"Seting config {setting_code} = '{value}'")
        tp = pydoc.locate(setting["type"])
        if tp == bool:
            if str(value).lower() == 'true' or str(value).lower() == '1':
                setting["value"] = True
            if str(value).lower() == 'false' or str(value).lower() == '0':
                setting["value"] = False
            return

        setting["value"] = tp(value)

    def save(self):
        yaml.dump(self.__conf_node, open(self.__file, "w", encoding="utf-8"))


class Config:
    __slots__ = ("__conf_node", "__file")

    def __init__(self, file: str) -> None:
        logger.info(f"Load config, file - {file}")
        self.__file = file
        self.__conf_node = yaml.load(open(self.__file, "r", encoding="utf-8"), Loader=yaml.SafeLoader)

    def get_value(self, name: str):
        return self.__conf_node[name]

    def __getitem__(self, name):
        return self.__conf_node[name]


def load_telegram_msgs():
    return Config(get_path("telegram_msgs"))


def load_telegram_setting():
    return Config(get_path("telegram_config"))


def load_neural():
    logger.info("loading neural config")
    return ConfigNeural(get_path("telegram_neural"))


def reset_neural():
    path = get_path("telegram_neural")

    if path.endswith(".current.yaml"):
        logger.info(f"Deleting neural config {path}")
        os.remove(path)

    return load_neural()


def get_path(cfgname: str) -> str:
    curr_path = os.path.join(CONFIG_FOLDER, f'{cfgname}.current.yaml')
    def_path = os.path.join(CONFIG_FOLDER, f'{cfgname}.yaml')
    if os.path.exists(curr_path):
        return curr_path
    return def_path
