'''다음 명령을 반복하여 입력받아 해당하는 기능을 출력하는 프로그램을 작성하시오.

단, E를 입력하면 "EXIT"를 출력한 후 프로그램을 종료한다.

'''
while True:
    cmd = input()
    
    if cmd == 'A':
        print("ADD")
    elif cmd == 'B':
        print("BACK")
    elif cmd == 'C':
        print("COPY")
    elif cmd == 'D':
        print("DELETE")
    elif cmd == 'E':
        print("EXIT")
        break
    else:
        print("NONE")
