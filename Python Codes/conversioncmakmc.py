#convierte cm en km, m y cm

import math

cm = int(input())

if cm >= 100000:
    km = cm/100000
    km = math.floor(km)
    print(km,'km')
    cm = cm-(km*100000)
if cm >= 100:
    m = cm/100
    m = math.floor(m)
    print(m,'m')
    cm = cm-(m*100)
if cm >= 1:
    print(cm,'cm')

