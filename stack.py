import os

stack =[]

def push (value) :
    stack.append(value)

def pop () :
    stack.pop()

def noel () :
    print (len (stack))

def top () :
    top = len (stack) - 1
    if top  < 0:
        print ("Tidak terdefinisi")
    else :
        print (stack[top])

def isempty () :
    if len (stack) == 0:
        print ("True")
    else:
        print ("false")

def tampilkan () :
    print (stack)


def mainmenu():
    pilih = "y"
    while (pilih == "y"):
        print("=========================")
        print("|  Menu aplikasi stack  |")
        print("=========================")
        print("1. Push objek")
        print("2. Pop objek")
        print("3. Cek Empty")
        print("4. Tampil objek terakhir")
        print("5. Panjang dari stack")
        print("6. tampilkan stack ")
        print("=========================")
        pilihan = str(input(("Silakan masukan pilihan anda: ")))
        if (pilihan == "1"):
            os.system('cls')
            push(int(input("masukkan nilai : ")))

        elif (pilihan == "2"):
            os.system('cls')
            pop()
            """ print("Objek " + self.pop() + " dihapus")
            x = input("")"""
        elif (pilihan == "3"):
            os.system('cls')
            isempty()
            """print(self.isEmpty())
            x = input("")"""
        elif (pilihan == "4"):
            os.system('cls')
            top()
            """print("Objek terakhir: " + self.peek())
            x = input("")"""
        elif (pilihan == "5"):
            os.system('cls')
            noel()
            """print("Panjang dari stack adalah: " + str(self.size()))
            x = input("")"""
        elif(pilihan == "6"):
            os.system('cls')
            tampilkan()
        else:
            pilih = "n"

mainmenu()