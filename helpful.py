# map(function, iterable)

nums = [1, 2, 3]
result = list(map(lambda x: x + 1, nums))
# lambda is an anonymous function, the map function applies it to each element in nums
# similar to js nums.map(x => x + 1)
# lambda is one liner function, if more complex function is needed, define a separate function using def keyword
# map returns a map object (lazy object), it computes the values when iterated over, so we convert it to a list


dict = {}
dict.get("key", 0)
dict["key"] 
# the get method return None if the key is not found, or the default value provided as second argument
# the square bracket notation raises a KeyError if the key is not found

dict['key'] = dict.get('key', 0) + 1
# this increments the value for 'key' in the dictionary, initializing it to 0 if

# looping with enumerate
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(index, name)

# loop with range
for i in range(len(names)):
    print(i, names[i])

fruits = ["apple", "banana", "cherry"]
# all function returns True if all elements in the iterable are true
all(fruit[0] == 'a' for fruit in fruits)

# finding the minimum length string in a list
strs = ["flower", "flow", "flight"]
# min function with key argument
shortest_word = min(strs, key=len, default="") 
# flow is the shortest word

scores = {"Alice": 85, "Bob": 72, "Charlie": 90}
lowest_score_name = min(scores, key=scores.get)
# Bob has the lowest score of 72

numbers_range = [5,2,9,1,5,6]
# sorted returns a new sorted list, sort method sorts the list in place
sorted_numbers = sorted(numbers_range)
numbers_range.sort()