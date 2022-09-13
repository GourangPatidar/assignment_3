#f=open("poem.txt" , 'r')
#print(f.read())
#print(f.readline())
#print(f.readline())
#print(f.readline(4))


#f1=open("abcd" , 'w')
#f1.write("hii there")

#f1=open("abcd" , 'a')
#f1.write("gourang")
#f1.write("patidar")

#for data in f:
 #   f1.write(data)

import shutil
f=open("poem.txt" , 'r')
f1=open("data1.txt" , 'w')
shutil.copyfileobj(f,f1)


