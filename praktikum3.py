x=100000000
sum=0
y=0
ib = [int(0), int(0), int(x) * .1, int(x) * .1, int(x) * .5, int(x) * .5, int(x) * .5, int(x) *.2]
print ('Modal awal seorang pengusaha :',x)
for i in ib :
    sum=sum+i

    y+=1

    print('laba bulan ke -', y ,'sebesar :',i)

print('total laba yang di dapat adalah :',sum)