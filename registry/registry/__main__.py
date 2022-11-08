import click
import socket

from .conf import _help
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
def repo(ssl, host, port) -> None:
    click.echo("\t\033[96m {} => {}:{}\033[00m" .format(_help.repo,
                                                        host, port))
    _repo(ssl, host, port)


@registry.command(help=_help.info)
@click.option('-h', '--host', default=_host, show_default=True,
              required=False, type=str, help=_help.host)
@click.option('-p', '--port', default=5000, show_default=True,
              required=False, type=int, help=_help.port)
@click.option('-s', '--ssl', default=False, show_default=True,
              required=False, type=bool, help=_help.ssl)
@click.option('-r', '--repo', default='', required=False, type=str)
def info(ssl, host, port, repo) -> None:
    name_repo = repo if repo else 'all'
    click.echo("\t\033[96m {} => {}:{} | Репозиторий => {}\033[00m" .format(
        _help.info, host, port, name_repo))
    _info_repos(ssl, host, port, repo)


@registry.command(help=_help.delete)
@click.option('-h', '--host', default=_host, show_default=True,
              required=False, type=str, help=_help.host)
@click.option('-p', '--port', default=5000, show_default=True,
              required=False, type=int, help=_help.port)
@click.option('-s', '--ssl', default=False, show_default=True,
              required=False, type=bool, help=_help.ssl)
@click.option('-r', '--repo', required=True, type=str)
@click.option('-t', '--tag', required=True, type=str)
def delete(ssl, host, port, repo, tag) -> None:
    click.echo("\t\033[96m {} => {}:{} => {}:{}\033[00m" .format(
        _help.delete, host, port, repo, tag))
    _deleting_image(ssl, host, port, repo, tag)


def main():
    registry()


if __name__ == '__main__':
    main()
