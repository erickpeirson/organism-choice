import urllib
import json
from typing import Optional
import requests

from .data import SCHEME, NETLOC, SEARCH
from .exceptions import BadResponse, ParseError, BadParameter, RequestFailed


def decode_json_response(response: requests.Response,
                         key: Optional[str] = None) -> dict:
    if response.status_code != requests.codes.ok:
        raise BadResponse(f'Response {response.status_code}: {response.text}')
    try:
        data = response.json()
    except (json.decoder.JSONDecodeError, KeyError) as e:
        raise ParseError('Failed to parse response') from e
    if data:
        data = data[key]
    return data


def make_request(params: dict) -> requests.Response:
    try:
        query = urllib.parse.urlencode(params)
    except Exception as e:
        raise BadParameter('Bad parameter') from e

    target = urllib.parse.urlunsplit((SCHEME, NETLOC, SEARCH, query, ''))
    try:
        response = requests.get(target)
    except Exception as e:
        raise RequestFailed('Request to NCBI failed') from e
    return response
