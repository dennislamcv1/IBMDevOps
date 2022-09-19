"""
Internet Movie Database Access

Implements the SearchTitle, Reviews, and Ratings APIs
"""
import logging
import requests

logger = logging.getLogger()

class IMDb:
    """Access the Internet Movie database"""

    def __init__(self, apikey: str):
        self.apikey = apikey

    def search_titles(self, title) -> dict:
        """Search for a movie by Title"""
        logger.info("Searching IMDb for Title: %s", title)
        results = requests.get(f"https://imdb-api.com/API/SearchTitle/{self.apikey}/{title}")
        if results.status_code == 200: 
            return results.json()
        return {}

    def movie_reviews(self, imdb_id: str) -> dict:
        """Get reviews for a movie"""
        logger.info("Searching IMDb for Reviews: %s", imdb_id)
        results = requests.get(f"https://imdb-api.com/API/Reviews/{self.apikey}/{imdb_id}")
        if results.status_code == 200: 
            return results.json()
        return {}

    def movie_ratings(self, imdb_id: str) -> dict:
        """Get ratings for a movie"""
        logger.info("Searching IMDb for Ratings: %s", imdb_id)
        results = requests.get(f"https://imdb-api.com/API/Ratings/{self.apikey}/{imdb_id}")
        if results.status_code == 200: 
            return results.json()
        return {}
