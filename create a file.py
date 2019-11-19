filename = input('Please create a file name (For  example - name.txt): ')
text = input('Please write text: ')

file = open(filename, 'w')
file.write(text)


file.close()