#!/usr/bin/env python3


from models.keyword_searcher import KeywordSearcher


def main():
    """entry point for program
    """
    searcher = KeywordSearcher("california trees")
    links = searcher.get_media_links()
    for link in links:
        print(link)
    searcher.set_image_mode()
    links = searcher.get_media_links()
    for link in links:
        print(link)

main()
