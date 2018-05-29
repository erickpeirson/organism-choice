"""ESearch integration."""

from typing import Optional
from datetime import date

from .data import EntrezResult, EntrezResultSet
from .util import make_request, decode_json_response


def search(db: str, term: str, tool: str, email: str,
           field: Optional[str] = None,
           sort: Optional[str] = None,
           retstart: int = 0, retmax: int = 20, rettype: str = 'uilist',
           datetype: str = 'pdat',
           mindate: Optional[date] = None,
           maxdate: Optional[date] = None) -> EntrezResultSet:
    """Perform an ESearch query."""
    params = {'db': db, 'term': term, 'tool': tool, 'email': email,
              'retmode': 'json'}
    if field:
        params['field'] = field
    if sort:
        params['sort'] = sort
    if mindate:
        params['mindate'] = mindate.strftime('%Y/%m/%d')
    if maxdate:
        params['maxdate'] = maxdate.strftime('%Y/%m/%d')
    if (mindate or maxdate) and datetype:
        params['reldate'] = datetype

    response = make_request(params)
    raw = decode_json_response(response, 'esearchresult')

    return EntrezResultSet(
        results=[
            EntrezResult(db=db, uid=uid) for uid in raw['idlist']
        ],
        count=int(raw['count']),
        start=int(raw['retstart']),
        max_results=int(raw['retmax']),
        query_key=int(raw['querykey']),
        query_translation=raw['querytranslation'],
    )
