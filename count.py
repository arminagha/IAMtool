d = {'0': ['Pyrobaculum'], 
'1': ['Mycobacterium', 'Mycobacterium', 'Mycobacterium', 'Mycobacterium', 'Mycobacterium', 'Mycobacterium', 'Mycobacterium', 'Mycobacterium', 'Mycobacterium', 'Mycobacterium', 'Mycobacterium', 'Mycobacterium', 'Mycobacterium', 'Mycobacterium'], 
'3': ['Thermoanaerobacter', 'Thermoanaerobacter'], 
'2': ['Helicobacter', 'Mycobacterium'], 
'5': ['Thermoanaerobacter', 'Thermoanaerobacter'], 
'4': ['Helicobacter'], 
'7': ['Syntrophomonas'], '6': ['Gelria'], '9': ['Campylobacter', 'Campylobacter'], '8': ['Syntrophomonas'], '10': ['Desulfitobacterium', 'Mycobacterium']}



# Iterate through and find out how many times each key occurs
vals = {}                       # A dictonary to store how often each value occurs.
for i in d.values():
  for j in set(i):              # Convert to a set to remove duplicates
    vals[j] = 1 + vals.get(j,0) # If we've seen this value iterate the count
                                # Otherwise we get the default of 0 and iterate it
print(vals)


