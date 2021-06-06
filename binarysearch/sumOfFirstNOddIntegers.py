def solve(n):
        oddnums = []
        i = 1

        while len(oddnums) != n:
            oddnums.append(i)
            i += 2
        
        return sum(oddnums)
