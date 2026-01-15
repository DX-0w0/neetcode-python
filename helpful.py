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