def stairWalks(n, values):
  ans = list()
  stairWalksRecursive(n, values, (), ans)
  return ans

def stairWalksRecursive(n, values, state, ans_list):
  if n <= 0:
    if n == 0:
      ans_list.append(state)
  else:
    for value in values:
     #if n - value >= 0:
      #print(f"({n-value},{state + (value, )})", end="")
     stairWalksRecursive(n - value, values, state + (value ,), ans_list)
    #print()

print(stairWalks(10, (2, 3)))