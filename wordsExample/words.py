#! /usr/bin/env python3
"""Retrieve and print words from a URL.

Usage:
    python words.py <URL>
    python words.py http://sixty-north.com/c/t.txt
"""


import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL
    
        Args:
            url: The url of the UTF-8 text document.
        
        Returns:
            A list of strings containing the words from
            the document
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words
    # 2 lines between module level functions


def print_items(items):
    """Print items one per line.
        
        Args:
            An iterable series of printable items
    """  
    for word in items:
        print(word)


def main(url):   
    """Print each word from a text document from at a URL.

        Args: 
            url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename.
