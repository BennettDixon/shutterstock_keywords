#!/usr/bin/env python3


class KeywordRank():
    """class for holding data about keyword ranking for unique keywords
    """
    def __init__(self, keyword):
        self.keyword = keyword
        self.occurances = 0
        self.page_rank = 0
        self.overall_rank = 0

    @property
    def keyword(self):
        return self.__keyword

    @keyword.setter
    def keyword(self, value):
        if type(value) is not str:
            raise TypeError("KeywordRank keyword must be a string")
        if len(value) < 1:
            raise ValueError("KeywordRank keyword len <= 0")
        self.__keyword = value

    @property
    def occurances(self):
        return self.__occurances

    @occurances.setter
    def occurances(self, value):
        if type(value) is not int:
            raise TypeError("Keyword occurances must be of int type")
        if value < 0:
            raise ValueError("KeywordRank occurances must be > 0")
        self.__occurances = value

    @property
    def page_rank(self):
        return self.__page_rank

    @page_rank.setter
    def page_rank(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("KeywordRank page_rank must be int or float")
        if value < 0:
            raise ValueError("KeywordRank page_rank must be > 0")
        self.__page_rank = value

    @property
    def overall_rank(self):
        return self.__overall_rank

    @overall_rank.setter
    def overall_rank(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("KeywordRank overall_rank must be int or float")
        if value < 0:
            raise ValueError("KeywordRank overall_rank must be > 0")
        self.__overall_rank = value
