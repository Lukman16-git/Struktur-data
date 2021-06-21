import os

queue =[]

def push (value) :
    queue.append(value)

def deuque () :
    queue.pop(0)

def noel () :
    print (len (queue))

def top () :
    top = len (queue) - 1
    if top  < 0:
        print ("Tidak terdefinisi")
    else :
        print (queue[top])

def isempty () :
    if len (queue) == 0:
        print ("True")
    else:
        print ("false")

def tampilkan () :
    print (queue)


def mainmenu():
    pilih = "y"
    while (pilih == "y"):
        print("=========================")
        print("|  Menu aplikasi stack  |")
        print("=========================")
        print("1. ENQUEUE objek")
        print("2. DEQUEUE objek")
        print("3. Cek Empty")
        print("4. Tampilkan objek terakhir")
        print("5. Panjang dari QUEUE")
        print("6. tampilkan QUEUE ")
        print("=========================")
        pilihan = str(input(("Silakan masukan pilihan anda: ")))
        if (pilihan == "1"):
            os.system('cls')
            push(int(input("masukkan nilai : ")))

        elif (pilihan == "2"):
            os.system('cls')
            deuque()
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