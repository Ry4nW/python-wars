class Solution:
    def solve(self, tasks, people):
        if not tasks:
            return 0

        taskCount = 0
        i = 0

        tasks.sort()
        people.sort()

        while i < len(people):
            try:
                if people[i] >= tasks[i]:
                    taskCount += 1
                    i += 1
                else:
                    del people[i]
            except:
                break
        
        return taskCount
