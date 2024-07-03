def write(width, height):
  firstNone = True
  f = open("table.txt", 'w')
  for i in range(1, width*height+1):
      if i % width == 1:
          if firstNone == False:
           f.write("\n")
          else:
             firstNone = False
      f.write(str(i) + " ")

write(4, 4)

def get_number(x, y):
  f = open('table.txt', 'r')
  lines = f.readlines()
  row = lines[y-1].strip().split()
  return int(row[x-1])

number = get_number(2, 3)
print(number)