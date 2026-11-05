'''번호를 입력받아 번호에 해당하는 메뉴를 출력하는 작업을 반복하다가 5를 입력하면 "EXIT"를 출력한 후 프로그램을 종료하는 프로그램을 작성하시오.

입력된 값이 범위를 벗어나면 “ERROR"을 출력하고 다시 입력을 받는다.'''
while True:
    n = int(input())
    
    if n == 1:
        print("ADD")
    elif n == 2:
        print("DELETE")
    elif n == 3:
        print("SEARCH")
    elif n == 4:
        print("PRINT")
    elif n == 5:
        print("EXIT")
        break
    else:
        print("ERROR")
