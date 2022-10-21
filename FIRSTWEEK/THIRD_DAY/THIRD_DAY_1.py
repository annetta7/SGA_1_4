# lets create a list
# break statement
stationaries = ['pencil', 'eraser', 'ruler']
#exit the loop when it gets to eraser
for x in stationaries:
    if x == 'eraser':
        break
    print(x)


#continue statement
stationaries = ['pencil', 'eraser', 'ruler']
for x in stationaries:
    if x == 'eraser':
        continue
    print(x)

# pass statement
stationaries = ['pencil', 'eraser', 'ruler']
for x in stationaries:
    pass

# accessing list elements
stationaries = ['pencil', 'eraser', 'ruler']
print(stationaries[0:2])

# change items of a list
stationaries = ['pencil', 'eraser', 'ruler']
stationaries[1] = 'marker'
print(stationaries)


# using insert method to add an item to my list
stationaries.insert(1,'pen')
print(stationaries)

stationaries.append('jotter')
print(stationaries)

school_supply = ['chairs', 'tables', 'boards']
stationaries = ['pencil', 'eraser', 'ruler']

school_supply.extend(stationaries)
print(school_supply)

#remove method
school_supply.remove('eraser')
print(school_supply)


school_supply.pop(1)
print(school_supply)















