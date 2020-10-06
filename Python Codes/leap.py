#determina si un año es un año biesto

año = int(input())

if año>0 and (año%4)==0 and not((año%100)==0) and not((año%400)==0):
    print("True")

else:
    print("False")
