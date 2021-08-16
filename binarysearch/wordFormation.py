class Solution:
    def solve(self, words, letters):

        longestWord = 0
        cantBeMade = False
        originalLetters = letters

        for word in words:

            if len(word) > longestWord:

                for letter in word:

                    if letter in letters:
                        letters = letters.replace(letter, '', 1)
                    else:
                        cantBeMade = True
                        break

                if not cantBeMade:
                    longestWord = len(word)

            letters = originalLetters
            cantBeMade = False

        return longestWord
                        