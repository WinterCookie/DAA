bil1 = int(input("Masukkan Nilai Pertama:"))
bil2 = int(input("Masukkan Nilai Kedua:"))

x = bil1
y = bil2

while x != y:
    if x>y:
        y = bil2 + y
    else:
        x = bil1 + x

print("Jadi, Nilai KPK dari", bil1, "dan", bil2,"adalah", x)