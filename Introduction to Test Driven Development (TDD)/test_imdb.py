"""
Test Cases for Mocking Lab
"""
import json
from unittest import TestCase
from unittest.mock import patch, Mock
from requests import Response
from models import IMDb

IMDB_DATA = {}

class TestIMDbDatabase(TestCase):
    """Tests Cases for IMDb Database"""

    @classmethod
    def setUpClass(cls):
        """ Load imdb responses needed by tests """
        global IMDB_DATA
        with open('tests/fixtures/imdb_responses.json') as json_data:
            IMDB_DATA = json.load(json_data)


    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    @patch('test_imdb.IMDb.search_titles')
    def test_search_by_title(self, imdb_mock):  
        """Test searching by title"""
        imdb_mock.return_value = IMDB_DATA["GOOD_SEARCH"]
        imdb = IMDb("k_12345678")
        results = imdb.search_titles("Bambi")
        self.assertIsNotNone(results)
        self.assertIsNone(results["errorMessage"])
        self.assertIsNotNone(results["results"])
        self.assertEqual(results["results"][0]["id"], "tt1375666")

    @patch('models.imdb.requests.get')
    def test_search_with_no_results(self, imdb_mock):
        """Test searching with no results"""
        imdb_mock.return_value = Mock(status_code=404)
        imdb = IMDb("k_12345678")
        results = imdb.search_titles("Bambi")
        self.assertEqual(results, {})

    @patch('models.imdb.requests.get')
    def test_search_by_title_failed(self, imdb_mock):
        """Test searching by title failed"""
        imdb_mock.return_value = Mock(
            spec=Response,
            status_code=200,
            json=Mock(return_value=IMDB_DATA["INVALID_API"])
        )
        imdb = IMDb("bad-key")
        results = imdb.search_titles("Bambi")
        self.assertIsNotNone(results)
        self.assertEqual(results["errorMessage"], "Invalid API Key")

    @patch('models.imdb.requests.get')
    def test_movie_ratings(self, imdb_mock):
        """Test movie Ratings"""
        imdb_mock.return_value = Mock(
            spec=Response,
            status_code=200,
            json=Mock(return_value=IMDB_DATA["GOOD_RATING"])
        )
        imdb = IMDb("k_12345678")
        results = imdb.movie_ratings("tt1375666")
        self.assertIsNotNone(results)
        self.assertEqual(results["title"], "Bambi")
        self.assertEqual(results["filmAffinity"], 3)
        self.assertEqual(results["rottenTomatoes"], 5)

    def test_search_by_title(self):
        """Test searching by title"""
        imdb = IMDb("k_12345678")
        results = imdb.search_titles("Bambi")
        self.assertIsNotNone(results)
        self.assertIsNone(results["errorMessage"])
        self.assertIsNotNone(results["results"])
        self.assertEqual(results["results"][0]["id"], "tt1375666")

    def test_search_with_no_results(self):
        """Test searching with no results"""
        imdb = IMDb("k_12345678")
        results = imdb.search_titles("Bambi")
        self.assertEqual(results, {})

    def test_search_by_title_failed(self):
        """Test searching by title failed"""
        imdb = IMDb("bad-key")
        results = imdb.search_titles("Bambi")
        self.assertIsNotNone(results)
        self.assertEqual(results["errorMessage"], "Invalid API Key")

    def test_movie_ratings(self):
        """Test movie Ratings"""
        imdb = IMDb("k_12345678")
        results = imdb.movie_ratings("tt1375666")
        self.assertIsNotNone(results)
        self.assertEqual(results["title"], "Bambi")
        self.assertEqual(results["filmAffinity"], 3)
        self.assertEqual(results["rottenTomatoes"], 5)