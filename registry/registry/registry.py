import click
import requests
from collections import namedtuple
from urllib.parse import urlunparse

from .conf import conf, Color


Components = namedtuple(
    typename='Components',
    field_names=['scheme', 'netloc', 'url', 'params', 'query', 'fragment']
)


def registry_requests(method: str, url: str, headers: dict = None) -> dict:
    """ Отправка данных в API REGISTRY """
    try:
        if method == "get":
            if headers:
                response = requests.get(url,
                                        timeout=conf.timeout,
                                        headers=headers)
            else:
                response = requests.get(url,
                                        timeout=conf.timeout)
        elif method == "delete":
            response = requests.delete(url, timeout=conf.timeout)
        else:
            return dict(error='req_method error')

        try:
            data: dict = response.json()
            if headers:
                data.update(headers=response.headers)
        except requests.exceptions.JSONDecodeError:
            data = dict(error='JSONDecodeError', url=url)

        return dict(status_code=response.status_code,
                    data=data)
    except requests.exceptions.ConnectionError as err:
        return dict(error=str(err), url=url)
    except requests.exceptions.ReadTimeout as err:
        return dict(error=str(err), url=url)


def check_scheme(ssl: bool, host: str, port: int) -> tuple:
    scheme = "https" if ssl else "http"
    if ssl and port == 443:
        netloc = host
    elif not ssl and port == 80:
        netloc = host
    else:
        netloc = f"{host}:{port}"
    return scheme, netloc


def _repo(ssl: bool, host: str, port: int, log: bool = True) -> list:
    """ Информация о репозиториях  """
    scheme, netloc = check_scheme(ssl, host, port)
    url = urlunparse(
        Components(
            scheme=scheme,
            netloc=netloc,
            url=f"{conf.base_url}/{conf.catalog_url}",
            params='',
            query='',
            fragment=''
        )
    )
    repo: dict = registry_requests(method="get", url=url)
    status_code = repo.get('status_code', None)
    data: dict = repo.get('data', dict())
    color: Color = Color.Turquoise4
    repositories: list = data.get('repositories', list())
    if status_code != requests.codes['ok']:
        click.echo("\t\t\033[38;5;{}m status => {}\033[0;0m" .format(
            color.value, status_code)
            )
    if log:
        click.echo("\t\t\033[38;5;{}m repositories =>\033[0;0m" .format(
            color.value)
            )
        color: Color = Color.Green
        for repository in repositories:
            click.echo("\t\t\t\033[38;5;{}m {}\033[0;0m" .format(
                color.value, repository)
                )

    return repositories


def _info_repo(ssl, host, port, repo):
    """ Информация репозитория  """
    scheme, netloc = check_scheme(ssl, host, port)
    url = urlunparse(
        Components(
            scheme=scheme,
            netloc=netloc,
            url=f"{conf.base_url}/{repo}/{conf.list_url}",
            params='',
            query='',
            fragment=''
        )
    )
    info: dict = registry_requests(method="get", url=url)
    color: Color = Color.Blue
    status_code = info.get('status_code', None)
    if status_code != requests.codes['ok']:
        click.echo("\t\t\033[38;5;{}m status => {}\033[0;0m" .format(
            color.value, status_code)
            )
    data: dict = info.get('data', dict())
    name: str = data.get('name', None)
    tags: list = data.get('tags', list())
    color: Color = Color.Green
    if name and tags:
        for tag in tags:
            click.echo("\t\t\t\033[38;5;{}m {}:{}\033[0;0m" .format(
                color.value, name, tag)
                )


def _info_repos(ssl: bool, host: str, port: int, repo: str):
    """ Информация репозиториев  """
    color: Color = Color.Turquoise4
    click.echo("\t\t\033[38;5;{}m repository =>\033[0;0m" .format(
        color.value)
        )
    if repo == '':
        repositories = _repo(ssl, host, port, log=False)
        if len(repositories) > 0:
            for repository in repositories:
                _info_repo(ssl, host, port, repository)
    else:
        _info_repo(ssl, host, port, repo)


def _deleting_image(ssl: bool, host: str, port: int, repo: str, tag: str):
    """ Удаление из репозитория образа Docker  """
    scheme, netloc = check_scheme(ssl, host, port)
    url = urlunparse(
        Components(
            scheme=scheme,
            netloc=netloc,
            url=f"{conf.base_url}/{repo}/{conf.manifests_url}/{tag}",
            params='',
            query='',
            fragment=''
        )
    )
    info: dict = registry_requests(method="get",
                                   url=url,
                                   headers=conf.headers)

    status_code = info.get('status_code', None)
    if status_code != requests.codes['ok']:
        color: Color = Color.Blue
        click.echo("\t\t\033[38;5;{}m status => {}\033[0;0m" .format(
            color.value, status_code)
            )
        return
    data: dict = info.get('data', dict())

    headers: dict = data.get('headers')
    color: Color = Color.Turquoise4
    etag: str = headers.get('Etag', '')
    etag = etag.replace('"', '')
    click.echo("\t\t\033[38;5;{}m etag => {}\033[0;0m" .format(
        color.value, etag)
        )

    url = urlunparse(
        Components(
            scheme=scheme,
            netloc=netloc,
            url=f"{conf.base_url}/{repo}/{conf.manifests_url}/{etag}",
            params='',
            query='',
            fragment=''
        )
    )
    info: dict = registry_requests(method="delete",
                                   url=url)
    status_code = info.get('status_code', None)
    if status_code != requests.codes['accepted']:
        color: Color = Color.Blue
        click.echo("\t\t\033[38;5;{}m status => {}\033[0;0m" .format(
            color.value, status_code))
        click.echo("\t\t\033[38;5;{}m etag => {}\033[0;0m" .format(
            color.value, info)
            )
