index1 = [1, 2, 3]
languages = ['python', 'c', 'c++']

dictionary = dict(zip(index1, languages))
print(dictionary)

index2 = [1, 2, 3]
languages = ['python', 'c', 'c++']

dictionary = {k: v for k, v in zip(index2, languages)}
print(dictionary)
