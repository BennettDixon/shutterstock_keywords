#!/usr/bin/env python3


from models.keyword_searcher import KeywordSearcher
from models.search_result import MediaResult


def main():
    """entry point for program
    """
    searcher = KeywordSearcher("california trees")
    links = searcher.get_media_links()
    page_results = []
    for media in links:
        keywords = searcher.get_keywords(media)
        result = MediaResult(keywords, searcher.page_num)
        print(result.keywords)
        page_results.append(result)

    print(page_results.pop().result_n)
main()
