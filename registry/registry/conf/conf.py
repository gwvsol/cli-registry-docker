import os
import click
import socket
from enum import Enum

host: str = os.getenv('REGISTRY_HOST',
                      default=socket.gethostbyname(
                          socket.gethostname()))
click.echo("\n\t\033[96m {}     => {}\033[00m" .format('REGISTRY_HOST', host))
port: int = int(os.getenv('REGISTRY_PORT', default='5000'))
click.echo("\t\033[96m {}     => {}\033[00m" .format('REGISTRY_PORT', port))
user: str = os.getenv('REGISTRY_USER', default='kab')
click.echo("\t\033[96m {}     => {}\033[00m" .format('REGISTRY_USER', user))
password: str = os.getenv('REGISTRY_PASSWORD', default='Let90nc23')
click.echo("\t\033[96m {} => {}\033[00m\n" .format('REGISTRY_PASSWORD',
                                                   '**********'))


class ConfigUrl:
    """ Настройки API REGISTRY """

    host: str = host
    port: int = port
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
