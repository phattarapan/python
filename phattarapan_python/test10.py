import os
choice = 0
filename = ''

def menu():
    global choice
    print ('Menu\n 1.Open Paint\n 2.Open Notepad\n 3.Exit')
    choice = input('Select Menu :')


    def opennotepad():
        filename = 'C:\\Windows\\notepad.exe'
        print('Memorandum writing %s' &filename)
        os.system(filename)

    def openpaint():
        filename = 'C:\\Windows\\system32\\paint.exe'
        print('Memorandum writing %s'&filename)
        os.system(filename)

        while True:
            menu()
            if choice == '1':
                openpaint()
            elif choice == '2':
                opennotepad()
            else:
                    break