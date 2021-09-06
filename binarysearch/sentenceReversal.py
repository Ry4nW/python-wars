class Solution:
    def solve(self, sentence):
        sentence = ''.join(sentence).split()
        sentence.reverse()
        ret = []

        for i in range(len(sentence)):
            for j in sentence[i]:
                ret.append(j)
            
            if i != len(sentence) - 1:
                ret.append(' ')
                
        return ret
        