# import module
from googlesearch import search

# print welcome message
print("Welcome to google search tool")

# taking query
query = input("What do you want to search on google? \n")

# loop over results
for i in search(query, start=0, stop=10):
	print(i)