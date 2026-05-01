#From Claude Prompt: create a graph problem that could appear in a technical live coding interview
# Shortest transformation sequence - Medium–Hard
# A classic disguised graph problem — the trick is recognizing it as BFS on an implicit graph.

# Given two words, beginWord and endWord, and a dictionary of words, find the length of the shortest transformation sequence from beginWord to endWord such that:

# Only one letter can be changed at a time.
# Each intermediate word must exist in the word list.
# Return 0 if no such sequence exists.

# Example
# beginWord = "hit"
# endWord   = "cog"
# wordList  = ["hot","dot","dog","lot","log","cog"]

# Output: 5
# Explanation: "hit" → "hot" → "dot" → "dog" → "cog"

# Constraints
# 1 ≤ beginWord.length ≤ 10
# endWord is in the wordList
# All words have the same length
# wordList contains unique words

##TODO