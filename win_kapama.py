import os
import time

dak = int(input("Dakika : "))
kapa = (dak * 60)
print(kapa)
time.sleep(1)
print("Kapanmaya 5")
time.sleep(1)
print("Kapanmaya 4")
time.sleep(1)
print("Kapanmaya 3")
time.sleep(1)
print("Kapanmaya 2")
time.sleep(1)
print("Kapanmaya 1")
time.sleep(1)
print("Kapatılıyor ...")
os.system("shutdown -s -f -t {}".format(kapa))



