#!/usr/bin/env python3


from models.keyword_searcher import KeywordSearcher
from models.media_result import MediaResult
from models.result_collection import ResultCollection


def main():
    """entry point for program
    """
    search_term = "california sky"
    for pn in range(0, 5):
        searcher = KeywordSearcher(search_term)
        links = searcher.get_media_links()
        results = ResultCollection(search_term)
        for media in links:
            keywords = searcher.get_keywords(media)
            result = MediaResult(keywords, searcher.page_num)
            print(result.keywords)
            results.append_result(result)
        searcher.inc_page_num()

    results.generate_ranking()
    top60 = []
    for kw in results.ranking:
        if len(top60) >= 60:
            break
        top60.append(kw)
    for ele in top60:
        print("Key:{}\nOverall Rank:{}\nPage Rank:{}\nOccurances:{}\n".format(ele.keyword, ele.overall_rank, ele.page_rank, ele.occurances))
    print(results.results.pop().result_n)
main()
