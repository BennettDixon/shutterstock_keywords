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

    results.generate_ranking()
    for kw_tup in results.ranking:
        if len(kw_tup) > 1:
            print("Key:{}\nOverall Rank:{}\nPage Rank:{}\nOccurances:{}\n".format(kw_tup[0], kw_tup[1].overall_rank, kw_tup[1].page_rank, kw_tup[1].occurances))
    print(results.results.pop().result_n)
main()
