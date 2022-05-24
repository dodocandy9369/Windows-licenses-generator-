import random

caracteres = ["B","C","D","F","G","H","J","K","M","N","P","Q","R","T","V","W","X","Y","2","3","4","5","6","7","8","9"]


while True:
    WINCodeP1= ""
    WINCodeP2= ""
    WINCodeP3= ""
    WINCodeP4= ""
    WINCodeP5= ""
    WINCode = ""

    for i in range(5):
         WINCodeP1 = f"{WINCodeP1}{random.choice(caracteres)}"
         WINCodeP2 = f"{WINCodeP2}{random.choice(caracteres)}"
         WINCodeP3 = f"{WINCodeP3}{random.choice(caracteres)}"
         WINCodeP4 = f"{WINCodeP4}{random.choice(caracteres)}"
         WINCodeP5= f"{WINCodeP5}{random.choice(caracteres)}"
    WINCode = f"{WINCodeP1}-{WINCodeP2}-{WINCodeP3}-{WINCodeP4}-{WINCodeP5}"
    print(f"{WINCode}")

    with open ("LICENSES.txt", "a+") as winFile:
       
       winFile.write(f"slmgr /ipk {WINCode}\n")

       winFile.close()
      


         

