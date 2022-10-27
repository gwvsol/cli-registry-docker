import os
import sys
import socket
import json

from .stdout import _stdout

registry_host = socket.gethostbyname(socket.gethostname())

registry_port = os.getenv('ASTERISK_PORT',
                          default=None)
if registry_port.isdigit():
    registry_port = int(registry_port)
else:
    raise SystemError('ASTERISK_PORT ERROR in env')


def _first() -> str or dict:
    """ Получение из командной строки первого параметра """
    try:
        return sys.argv[1]
    except IndexError:
        _error = 'parameter error in sys.argv[1]'
        _error = dict(error=_error)
        return _stdout(json.dumps(_error))


def _second() -> str or None:
    """ Получение из командной строки второго параметра """
    try:
        return sys.argv[2]
    except IndexError:
        return


class Config:
    """ Настройки API REGISTRY """
    base_url: str = "/v2/"
    host: str = registry_host
    port: str = registry_port
    first: str = _first()
    second: str = _second()
    timeout: int = 3


conf = Config()
