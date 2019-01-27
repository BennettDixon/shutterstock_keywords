#!/usr/bin/env python3


from models.media_result import MediaResult


class ResultCollection():
    """class for use in collecting results
    """
    def __init__(self, search_term):
        self.__results = list()
        self.search_term = search_term

    def append_result(self, value):
        """appends a result to results attr,
            no setter for it b/c dangerous
        """
        if type(value) != MediaResult:
            raise TypeError('ResultCollection append_result val must be SearchResult type')
        self.__results.append(value)

    @property
    def results(self):
        """getter for results property
        """
        return self.__results

    @property
    def search_term(self):
        return self.__search_term

    @search_term.setter
    def search_term(self, value):
        if not isinstance(value, str):
            raise TypeError('ResultCollection search_term attr must be str')
        if len(value) < 1:
            raise TypeError('ResultCollection search_term attr must have len > 0')
        self.__search_term = value
