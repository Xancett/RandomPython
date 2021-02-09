def my_number(something):
    something += 10
    print('Value inside function: ', something)

def my_word(something):
    something += ' rocks'
    print('Value inside function: ', something)

def my_list(list):
    list.append('four')
    print('Value inside function: ', list)


# Immutable types
width = 20
word = 'Python'
my_number(width)
print('Value outside function: ', width)
my_word(word)
print('Value outside function: ', word)

# Mutable types
someList = ['one', 'two', 'three']
my_list(someList)
print('Value outside function: ', someList)