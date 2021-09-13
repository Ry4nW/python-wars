def lone_sum(a, b, c):

  original = [a, b, c]
  loneSet = list(set([a, b, c]))
  retSum = 0

  for i in loneSet:
    if original.count(i) == 1:
        retSum += i 

  return retSum
