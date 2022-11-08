from enum import Enum


class ConfigUrl:
    """ Настройки API REGISTRY """
    base_url: str = "v2"
    catalog_url: str = "_catalog"
    list_url: str = "tags/list"
    manifests_url: str = "manifests"
    headers: dict = {
        'Accept': 'application/vnd.docker.distribution.manifest.v2+json'
        }
    timeout: int = 3


conf = ConfigUrl()


class ClickHelp:
    help: str = "Справка по работе с приложением"
    repo: str = "Информация о репозиториях Registry"
    info: str = "Информация об образах Docker в Registry"
    delete: str = "Удаление образа Docker в Registry"
    ssl: str = "Поддержка шифрования"
    host: str = "IP адрес Registry"
    port: str = "Порт Registry"


_help = ClickHelp()


class Color(Enum):
    """ 256 Colors Cheat Sheet
        https://www.ditig.com/256-colors-cheat-sheet """
    Maroon = 1
    Green = 2
    Olive = 3
    Navy = 4
    Purple = 5
    Teal = 6
    Silver = 7
    Grey = 8
    Red = 9
    Yellow = 11
    Blue = 12
    Fuchsia = 13
    Aqua = 14
    White = 15
    Turquoise4 = 30
    DodgerBlue1 = 33
    SpringGreen3 = 41
    RoyalBlue1 = 63
    Salmon1 = 209
