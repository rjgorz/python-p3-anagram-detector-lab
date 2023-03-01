# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        matches = []
        split_word = [letter for letter in self.word]
        for word in words:
            if sorted(split_word) == sorted([letter for letter in word]):
                matches.append(word)
        return matches