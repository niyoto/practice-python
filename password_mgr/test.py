# my_string = "how are you"
# list = my_string.split()
# print(list)
# for i in my_string:
#     print(i)
# str2 = " ".join(list)
# print(str2)


from collections import deque

d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.extendleft([7,8,9])
print(d)
d.rotate(2)
print(d)
#print(g)

# x = 'aaajojooe'
# y = collections.Counter(x)

# print(y.most_common(2))