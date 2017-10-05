# DPC 022 [E]
# List Compare and Append



L1 = ["a","b","c",1,4]
L2 = ["a", "x", 34, "4"]

for k in L2:
  if (k not in L1):
    L1 += [k]
    
print L1
