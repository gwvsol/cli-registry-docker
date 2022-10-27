import json
import requests
from .stdout import _stdout
from .conf import conf

def _requests(data: tuple):
    """ Отправка данных на ARI ASTERISK """
    _method, _url, _data = data
    try:
        if _method == "post":
            response = requests.post(_url,
                                     data=_data,
                                     timeout=conf.timeout)
        elif _method == "get":
            response = requests.get(_url,
                                    params=_data,
                                    timeout=conf.timeout)
        elif _method == "delete":
            response = requests.delete(_url, timeout=conf.timeout)
        else:
            _error = dict(error='req_method error')
            return _stdout(json.dumps(_error))

        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            _data.pop('api_key')
            _data.update(url=_url)
            data = _data

        _response = dict(status_code=response.status_code,
                         data=data)
        return _stdout(json.dumps(_response))
    except requests.exceptions.ConnectionError as err:
        return dict(error=str(err))
    except requests.exceptions.ReadTimeout as err:
        return dict(error=str(err))
