from unittest import TestCase, mock
import json

from entrez.esearch import search
from entrez.data import EntrezResultSet


class TestESearch(TestCase):

    @mock.patch('entrez.esearch.requests.get')
    def test_esearch(self, mock_get):
        with open('entrez/tests/data/esearch_pubmed_response.json') as f:
            mock_get.return_value = mock.MagicMock(
                status_code=200,
                json=mock.MagicMock(return_value=json.load(f))
            )
        results = search('pubmed', 'cancer', 'test', 'test@test.edu')
        self.assertIsInstance(results, EntrezResultSet)
        self.assertEqual(len(results.results), 100)
        self.assertEqual(results.count, 22984)
