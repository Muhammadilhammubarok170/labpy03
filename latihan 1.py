from random import random
print('Menampilkan n bilangan acak yang lebih kecil dari 0,5')
import random
jumlah =int (input("masukan nilai n : "))
for i in range (jumlah):
    print("Data ke -> ", 1+i, "=",(random.uniform(0.0,5)))