# CURRENT LAYOUT, TBF

'''
class Solution:
    def solve(self, s):

        time = list(''.join(s.split(':')))
        minimum = str(min(time))
        cur = ''
        i = 0

        while int(cur) <= int(''.join(time)):

            if len(cur) >= 4:
                return f'{minimum * 2}:{minimum * 2}'
            elif len(cur) >= 2:
                if int(cur) > int(time[0] + time[1]):
                    return f'{cur}:{minimum * 2}'
                elif int(cur) == int(time[0] + time[1]):
                    return 
        
        return f'{cur[:2]}:{cur[2:]}'
'''