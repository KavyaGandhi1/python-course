# create a dictionary which takes input from user and return its meaning

d1 = {'account': 'an arrangement with a bank to keep your money there and allow you to take it out when you need to.',
      'list': 'it is a data structure in coding','dictionary' : 'dictionary are data structures with key value pair',
      'phone': 'a mini computer which people use it in day to day life'}
name = input('Enter a word: ')
print('The meaning of',name,'is',"\"",d1[name.lower()],"\"")