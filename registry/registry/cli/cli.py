import click

from registry.conf import ConfigUrl as conf
from .help import ClickHelp


@click.group(help=ClickHelp.help)
def main() -> None:
    return


@main.command(help=ClickHelp.list)
@click.option('-h', '--host', default=conf.host, show_default=True,
              required=False, type=str, help=ClickHelp.host)
@click.option('-p', '--port', default=conf.port, show_default=True,
              required=False, type=int, help=ClickHelp.port)
@click.option('-s', '--ssl', default=False, show_default=True,
              required=False, type=bool, help=ClickHelp.ssl)
@click.option('-u', '--user', default=conf.user, show_default=False,
              required=False, type=str, help=ClickHelp.user)
@click.option('-pwd', '--passwd', default=conf.passwd, show_default=False,
              required=False, type=str, help=ClickHelp.passwd)
def list(ssl, host, port, user, passwd) -> None:
    click.echo("\t\033[96m {} => {}:{}\033[00m" .format(ClickHelp.list,
                                                        host, port))
    from registry.apps import repo_list
    repo_list(ssl, host, port, user, passwd)


@main.command(help=ClickHelp.info)
@click.option('-h', '--host', default=conf.host, show_default=True,
              required=False, type=str, help=ClickHelp.host)
@click.option('-p', '--port', default=conf.port, show_default=True,
              required=False, type=int, help=ClickHelp.port)
@click.option('-s', '--ssl', default=False, show_default=True,
              required=False, type=bool, help=ClickHelp.ssl)
@click.option('-r', '--repo', default='', required=False, type=str)
@click.option('-u', '--user', default=conf.user, show_default=False,
              required=False, type=str, help=ClickHelp.user)
@click.option('-pwd', '--passwd', default=conf.passwd, show_default=False,
              required=False, type=str, help=ClickHelp.passwd)
def info(ssl, host, port, repo, user, passwd) -> None:
    name_repo = repo if repo else 'all'
    click.echo("\t\033[96m {} => {}:{} | Репозиторий => {}\033[00m" .format(
        ClickHelp.info, host, port, name_repo))
    from registry.apps import repos_info
    repos_info(ssl, host, port, repo, user, passwd)


@main.command(help=ClickHelp.delete)
@click.option('-h', '--host', default=conf.host, show_default=True,
              required=False, type=str, help=ClickHelp.host)
@click.option('-p', '--port', default=conf.port, show_default=True,
              required=False, type=int, help=ClickHelp.port)
@click.option('-s', '--ssl', default=False, show_default=True,
              required=False, type=bool, help=ClickHelp.ssl)
@click.option('-r', '--repo', required=True, type=str)
@click.option('-t', '--tag', required=True, type=str)
@click.option('-u', '--user', default=conf.user, show_default=False,
              required=False, type=str, help=ClickHelp.user)
@click.option('-pwd', '--passwd', default=conf.passwd, show_default=False,
              required=False, type=str, help=ClickHelp.passwd)
def delete(ssl, host, port, repo, tag, user, passwd) -> None:
    click.echo("\t\033[96m {} => {}:{} => {}:{}\033[00m" .format(
        ClickHelp.delete, host, port, repo, tag))
    from registry.apps import img_del
    img_del(ssl, host, port, repo, tag, user, passwd)
