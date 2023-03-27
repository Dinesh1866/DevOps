# Write a python script to fetch data from news API 
#API to be used:https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt
#API Key: 9cf45a75ed4148df8132b32fa9ecd57e
'''Note: Data is in json format
a.Convert it to a pandas data frame that has only 5 columns author, title, description,source_name, content.

b.Remove the “.com” word in the source_name column

c. Remove all the special characters for description column

d. Implement error handling 

import requests
import pandas as pd
from pandas import json_normalize
def get_news():  
    Your code'''

#Write a python script to fetch data from news API

'''import requests
import pandas as pd
from pandas import json_normalize
def get_news():
      url = ('https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=
      9cf45a75ed4148df8132b32fa9ecd57e')
      response = requests.get(url)
      data = response.json()
      df = json_normalize(data['articles'])
      df = df[['author','title','description','source.name','content']]
      df['source.name'] = df['source.name'].str.replace('.com','')
      df['description'] = df['description'].str.replace('[^A-Za-z0-9]+',' ')
      return df
get_news()

#Output
author	title	description	source.name	content
'''

'''implement the function sort_by_price_ascending, which:

Accepts a string in JSON format, as in the example below.
Orders items by price in ascending order.
If two products have the same price, it orders them by their name in alphabetical order.
Returns a string in JSON format that is equivalent to the one in the input format.
For example, the call

sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]');
should return

'[{"name":"eggs","price":1},{"name":"rice","price":4.04},{"name":"coffee","price":9.99}]'
'''

'''import json
def sort_by_price_ascending(json_string):

      data = json.loads(json_string)
      data.sort(key = lambda x: (x['price'], x['name']))
      return json.dumps(data)

#Output
[{"name":"eggs","price":1},{"name":"rice","price":4.04},{"name":"coffee","price":9.99}]'''


'''Implement the find_all_hobbyists function that takes a hobby, and an object consisting of people's names mapped to their respective hobbies. The function should return a List containing the names of the people (in any order) that enjoy the hobby.

For example, the following code should display the name 'Chad'. If I provide input as ‘Yoga’ and it should display [‘Chad’, ‘Patty’] if we provide input as  ‘Pets’

hobbies = { 
    "Steve": ['Fashion', 'Piano', 'Reading'],
    "Patty": ['Drama', 'Magic', 'Pets'],
    "Chad": ['Puzzles', 'Pets', 'Yoga']
}'''


'''def find_all_hobbyists(hobby, hobbies):
      hobby_list = []
      for key, value in hobbies.items():
            if hobby in value:
                  hobby_list.append(key)
      return hobby_list

#Output'''

'''n = int(input())
val = ord("A")
for i in range(n):
      a = val
      for j in range(n):
            print(chr(a),end=" ")
            a+=1
      print()
      val+=1

#or
n = int(input())
for i in range(n):
      val = ord("A")+i%26
      for j in range(n):
            print(chr(val),end=" ")
            val+=1
      print()'''


