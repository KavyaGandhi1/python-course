# f = open('kavya.txt','w')
# f.write('Kavya is a good boy.')
# f.close()

# f = open('kavya.txt','a')
# f.write('Kavya is a good boy.\n')
# f.close()

# Handle read and write both
# r+ - for both read and write

f = open('kavya.txt','r+')
print(f.read())
f.write('thank you')