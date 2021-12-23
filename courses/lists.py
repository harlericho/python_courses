demoList = [1,'CARLOS',8.6,True,[1,2,3,4]]
print(demoList)
colors = ['blue','green','yellow']
print(colors)
numberList = list((1,2,3,4))
print(numberList)
rangeList = list(range(1,10))
print(rangeList)

# print(dir(colors))
print(colors[0])
print(colors[-1])
print(len(colors))
print('green' in colors) # booleans

colors[1] = 'red'
print(colors)
colors.append('violet') # add one a list
print(colors)
colors.extend(('orange','gray')) # add a lists with [] ()
print(colors)
colors.insert(0,'green') # add a list for position
print(colors)
colors.insert(len(colors), 'black') # add a list positiom final
print(colors)
colors.pop() # delete element final a list
colors.pop()
colors.pop(2) # delete element for position a list
print(colors)
colors.remove('green') # delete for name a list
print(colors)
colors.sort() # ORDER all list
print(colors)
colors.sort(reverse = True) # ORDER all list INVERSE
print(colors)

print(colors.index('blue')) # get index of list for name
print(colors.count('blue')) # count index of list for name

colors.clear() # delete all list
print(colors)