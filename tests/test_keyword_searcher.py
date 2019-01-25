#!/usr/bin/env python3
"""test module for use in testing keywordsearcher class
"""


import requests
import unittest
from models.keyword_searcher import KeywordSearcher


class TestSearcher(unittest.TestCase):
    """tests the searcher class
    """
    def test_video_media_grab(self):
        searcher = KeywordSearcher("california trees")
        links = searcher.get_media_links()
        for link in links:
            try:
                resp = requests.get(link)
            except:
                raise Exception('Error bad link {}'.format(link))
            self.assertEqual(resp.status_code, 200)

