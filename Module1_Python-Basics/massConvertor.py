unit = input("T or Kg? ")

amount = float(input("Amount: "))

if unit =="T":
    print(f"{amount*1000} Kg")
elif  unit=="Kg":
    print(f"{amount/1000} Kg")
else:
    print("Write correct Unit!")
