from typing import NamedTuple, List, Optional

SCHEME = 'http'
NETLOC = 'eutils.ncbi.nlm.nih.gov'
SEARCH = 'entrez/eutils/esearch.fcgi'


class EntrezResult(NamedTuple):
    db: str
    uid: str


class EntrezResultSet(NamedTuple):
    results: List[EntrezResult]
    count: int
    start: int
    max_results: int
    query_key: int
    query_translation: str
