f = open("text.txt", 'w')

def write_persons():

  name = input("Введите имя: ")
  last_name = input("Введите фамилию: ")

  f.writelines(name+" "+last_name+"\n")



def read_persons():
  file_read = open("text.txt", 'r')
  print("\n")
  for i in range(0,2):
    print(file_read.readline())


for i in range(0,2):
  write_persons()


f.close()
read_persons()