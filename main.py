#!/usr/bin/env python3


from models.keyword_searcher import KeywordSearcher
from models.media_result import MediaResult
from models.result_collection import ResultCollection


def main():
    """entry point for program
    """
    search_term = "california sky"
    searcher = KeywordSearcher(search_term)
    links = searcher.get_media_links()
    results = ResultCollection(search_term)
    for media in links:
        keywords = searcher.get_keywords(media)
        result = MediaResult(keywords, searcher.page_num)
        print(result.keywords)
        results.append_result(result)

    print(page_results.pop().result_n)
main()
