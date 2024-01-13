# dictionary = A changeable, unordered collection of unique key:value pairs
    # Fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC', 
            'France': 'Paris',
            'UK': 'London',
            'India': 'New Delhi',
            'China': 'Beijing'}

# capitals.update({'Germany': 'Berlin'})

# #you can also update existing variables using update

# capitals.update({'France':'Not Paris'})
# capitals.pop('China') # removes the item from the dictionary
# capitals.clear() # clears the dictionary

# print(capitals['UK']) # returns the value of the key but throws an error if not found
# print(capitals.get('Germany')) # returns none if not found so a safer method to use as it will not interrupt the flow.
# print(capitals.keys()) # returns all the keys in the dictionary
# print(capitals.values()) # returns all the values in the dictionary
# print(capitals.items()) # returns all the items in the dictionary

for key, value in capitals.items():
    print(key, value)