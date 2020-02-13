file=open('testing.jpg','rb')
save=file.read()
file.close

file1=open('biju.txt','wb')
file1.write(save)
file1.close