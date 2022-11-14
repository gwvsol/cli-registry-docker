import click
import socket
from requests.auth import HTTPBasicAuth

from .conf import _help, conf
from .registry import _repo, _info_repos, _deleting_image


_host = socket.gethostbyname(socket.gethostname())


@click.group(help=_help.help)
def registry() -> None:
    return


@registry.command(help=_help.repo)
@click.option('-h', '--host', default=_host, show_default=True,
              required=False, type=str, help=_help.host)
@click.option('-p', '--port', default=5000, show_default=True,
              required=False, type=int, help=_help.port)
@click.option('-s', '--ssl', default=False, show_default=True,
              required=False, type=bool, help=_help.ssl)
@click.option('-u', '--user', default=conf.user, show_default=False,
              required=False, type=str, help=_help.user)
@click.option('-pwd', '--passwd', default=conf.passwd, show_default=False,
              required=False, type=str, help=_help.passwd)
def repo(ssl, host, port, user, passwd) -> None:
    click.echo("\t\033[96m {} => {}:{}\033[00m" .format(_help.repo,
                                                        host, port))
    auth = HTTPBasicAuth(user, passwd)
    _repo(ssl, host, port, auth)


@registry.command(help=_help.info)
@click.option('-h', '--host', default=_host, show_default=True,
              required=False, type=str, help=_help.host)
@click.option('-p', '--port', default=5000, show_default=True,
              required=False, type=int, help=_help.port)
@click.option('-s', '--ssl', default=False, show_default=True,
              required=False, type=bool, help=_help.ssl)
@click.option('-r', '--repo', default='', required=False, type=str)
@click.option('-u', '--user', default=conf.user, show_default=False,
              required=False, type=str, help=_help.user)
@click.option('-pwd', '--passwd', default=conf.passwd, show_default=False,
              required=False, type=str, help=_help.passwd)
def info(ssl, host, port, repo, user, passwd) -> None:
    name_repo = repo if repo else 'all'
    click.echo("\t\033[96m {} => {}:{} | Репозиторий => {}\033[00m" .format(
        _help.info, host, port, name_repo))
    auth = HTTPBasicAuth(user, passwd)
    _info_repos(ssl, host, port, repo, auth)


@registry.command(help=_help.delete)
@click.option('-h', '--host', default=_host, show_default=True,
              required=False, type=str, help=_help.host)
@click.option('-p', '--port', default=5000, show_default=True,
              required=False, type=int, help=_help.port)
@click.option('-s', '--ssl', default=False, show_default=True,
              required=False, type=bool, help=_help.ssl)
@click.option('-r', '--repo', required=True, type=str)
@click.option('-t', '--tag', required=True, type=str)
@click.option('-u', '--user', default=conf.user, show_default=False,
              required=False, type=str, help=_help.user)
@click.option('-pwd', '--passwd', default=conf.passwd, show_default=False,
              required=False, type=str, help=_help.passwd)
def delete(ssl, host, port, repo, tag, user, passwd) -> None:
    click.echo("\t\033[96m {} => {}:{} => {}:{}\033[00m" .format(
        _help.delete, host, port, repo, tag))
    auth = HTTPBasicAuth(user, passwd)
    _deleting_image(ssl, host, port, repo, tag, auth)


if __name__ == '__main__':
    registry()
