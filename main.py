#!/usr/bin/env python3


from models.keyword_searcher import KeywordSearcher


def main():
    """entry point for program
    """
    searcher = KeywordSearcher("california trees")
    links = searcher.get_media_links()
    keywords = searcher.get_keywords(links[0])            
    for w in keywords:
        print(w)
    searcher.set_image_mode()
    links = searcher.get_media_links()
    keywords = searcher.get_keywords(links[0])
    for w in keywords:
        print(w)

main()
