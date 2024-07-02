s = "Hello world\nHello again"

f = open("text.txt", 'w')

f.writelines(s)

f.close()

f = open("text.txt", 'r')

for i in range(0,2):
  print(f.readline())

f.close()