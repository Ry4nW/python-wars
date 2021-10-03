class Solution:
    def solve(self, stacks):

        if not stacks:
            return 0
            
        prefixSums = []
        for stack in stacks:
            curPrefixSum = []
            for i in range(1, len(stack) + 1):
                curPrefixSum.append(sum(stack[0:i]))
            prefixSums.append(curPrefixSum)

        GCM = 0

        for prefixSum in prefixSums[0]:
            common = True
            for otherPrefixSums in prefixSums[1:]:
                if prefixSum not in otherPrefixSums:
                    common = False
                    break

            if common: GCM = GCM if prefixSum < GCM else prefixSum
        
        return GCM
