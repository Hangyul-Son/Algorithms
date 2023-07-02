#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#


class TrieNode:
    def __init__(self, letter, end):
        self.letter = letter
        self.end = end
        self.nodes = []
    
    
def check_tree(root, word):
    for i in word:
        if i not in [node.letter for node in root.nodes]:
            temp = TrieNode(i, False)
            root.nodes.append(temp)
            root = temp
        else:
            for node in root.nodes:
                if node.letter == i:
                    root = node
                    if root.end == True:
                        print(f'BAD SET\n{word}')
                        return False
                    break
    root.end = True
    if len(root.nodes) != 0:
        print(f'BAD SET\n{word}')
        return False
    return True
    
    
        

def noPrefix(words):
    # Write your code here
    root = TrieNode("", False)
    for word in words:
        val = check_tree(root, word)
        if val == False:
            return
    print('GOOD SET')
if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
