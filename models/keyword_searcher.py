#!/usr/bin/python3


import requests
from bs4 import BeautifulSoup
import urllib


class KeywordSearcher():
    """class for use in finding keywords in shutterstock
    """
    base_url = "https://www.shutterstock.com"

    def __init__(self, search_term, mode=None):  # refactor when adding modes
        self.__image_mode = "image"
        self.__video_mode = "video"
        self.__page_num = 1
        if mode is None:
            self.__mode = self.__video_mode
        else:
            self.__mode = mode
        self.search_term = search_term

    @property
    def search_term(self):
        return self.__search_term

    @search_term.setter
    def search_term(self, value):
        if type(value) is not str:
            raise TypeError('KeywordSearcher search_term must be str type')
        if value is None or len(value) == 0:
            raise ValueError('KeywordSearcher search_term must have len > 0')
        self.__search_term = value

    @property
    def mode(self):
        return self.__mode

    def inc_page_num():
        """increments the page number
        """
        self.__page_num += 1

    def get_video_term(self):
        """gets the search term encoded for use with video url pattern
        """
        return self.search_term.replace(' ', '-')

    def get_image_term(self):
        """gets the search term encoded for use with img url pattern
        """
        return self.search_term

    def set_image_mode(self):
        """sets the current mode to image mode regardless of state
        """
        self.__mode = self.__image_mode
        self.__page_num = 1

    def set_video_mode(self):
        """sets the current mode to video mode regardless of state
        """
        self.__mode = self.__video_mode
        self.__page_num = 1

    def get_media_links(self):
        """gets current page numbers page links as a list of strings
        """
        if self.mode == self.__video_mode:
            video_term = self.get_video_term()
            search_add = '/video/search/{}?page={}'.format(video_term,
                                                           self.__page_num)
            search_url = self.base_url + search_add
            req = requests.get(search_url)
            soup = BeautifulSoup(req.content, 'html.parser')
            links = [self.base_url + str(link)[str(link).find("/video/clip"):]
                     for link in soup.find_all('a')
                     if "/video/clip" in str(link)]
            real_links = []
            for link in links:
                real_links.append(link[:link.find('"><div class="')])
            return real_links
        elif self.mode == self.__image_mode:
            image_term = self.get_image_term()
            search_add = urllib.parse.urlencode({'image_type': 'all',
             'search_source': 'base_search_form', 'language': 'en',
             'searchterm': image_term, 'page': self.__page_num, 'section': 1})
            search_url = self.base_url + '/search?' + search_add
            return search_url
        else:
            raise Exception("KeywordSearcher is in an unknown mode")
