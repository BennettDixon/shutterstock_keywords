#!/usr/bin/env python3


from models.media_result import MediaResult
from models.keyword_rank import KeywordRank


class ResultCollection():
    """class for use in collecting results
    """
    def __init__(self, search_term):
        self.__results = list()
        self.search_term = search_term
        self.__ranking = dict()

    def append_result(self, value):
        """appends a result to results attr,
            no setter for it b/c dangerous
        """
        if type(value) != MediaResult:
            raise TypeError('ResultCollection append_result val must be SearchResult type')
        self.__results.append(value)

    @property
    def ranking(self):
        """getter for ranking property, no setter, use generate_ranking
        """
        return self.__ranking

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

    def generate_ranking(self):
        """generates ranking data based on current result data
            -> Check Ranking class for more info
            -> does # of times used and a more complex ranking method
                -> involving positional data
        """
        ranking_list = {}
        for result in self.results:
            for kw in result.keywords:
                if len(kw) < 1:
                    continue
                if kw not in ranking_list.keys():
                    ranking_list[kw] = KeywordRank(kw)
                ranking_list[kw].occurances += 1
                diff = (1 - (result.page_num * 0.01))
                if diff < 0:
                    diff = 0
                ranking_list[kw].page_rank += diff
                diff = (1 - (result.result_n * 0.001))
                if diff < 0:
                    diff = 0.001
                ranking_list[kw].overall_rank += diff
        ranking_list = sorted(ranking_list.items(), key=lambda kv: kv[1].overall_rank, reverse=True)
        self.__ranking = ranking_list
        return self.ranking
