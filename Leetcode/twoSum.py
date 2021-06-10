# Brute force solution.

def twoSumBruteForce(nums, target):

    for i in range(len(nums)):

        for j in range(len(nums)):

            if nums[i] + nums[j] == target:

                if i != j:
                    return [i, j]

# Hash table solution.

def twoSumHashTable(arr, total):
    hash_table = dict()

    for i in range(len(arr)):

        complement = total - arr[i]

        if complement in hash_table:

            return (i, hash_table[complement])

        else:
            
            hash_table[arr[i]] = i

    return None


