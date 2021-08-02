class Solution:
    def solve(self, heights):

        if len(heights) == 0:
            return []
        
        unobstructedBuildings = []
        
        for i in range(len(heights) - 1):

            taller = False

            for j in range(i + 1, len(heights)):

                if heights[j] >= heights[i]:
                    taller = True
                    break
            
            if not taller:
                unobstructedBuildings.append(i)

        unobstructedBuildings.append(len(heights) - 1)
        return unobstructedBuildings
        