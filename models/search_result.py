#!/usr/bin/env python3
"""module for use with storing result data
"""


class MediaResult():
    """class for use in storing result data
    """
    results = 0

    def __init__(self, keywords, page_num):
        self.keywords = keywords
        self.__page_num = page_num
        MediaResult.results += 1
        self.__result_n = MediaResult.results

    @property
    def result_n(self):
        return self.__result_n

    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, value):
        if not isinstance(value, list):
            raise TypeError("keywords must be a list of keywords")
        for val in value:
            if type(val) is not str:
                raise TypeError("keyword in keywords list must be str")
        self.__keywords = value

    @property
    def page_num(self):
        return self.__page_num
