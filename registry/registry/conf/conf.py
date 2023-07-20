import os
import socket
from enum import Enum

user = os.getenv('REGISTRY_USER', default='kab')
password = os.getenv('REGISTRY_PASSWORD', default='Let90nc23')


class ConfigUrl:
    """ Настройки API REGISTRY """

    host: str = socket.gethostbyname(socket.gethostname())
    port: int = 5000
    user: str = user
    passwd: str = password

    base_url: str = "v2"
    catalog_url: str = "_catalog"
    list_url: str = "tags/list"
    manifests_url: str = "manifests"
    headers: dict = {
        'Accept': 'application/vnd.docker.distribution.manifest.v2+json'
        }
    timeout: int = 3


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
