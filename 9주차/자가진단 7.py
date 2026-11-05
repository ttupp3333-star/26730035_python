'''다음 메뉴를 반복해서 출력하고 번호를 입력받아 해당 기능을 출력하는 프로그램을 작성하시오.

단, 4를 입력하면 "QUIT"을 출력한 후 프로그램을 종료한다.'''
while True:
    n = int(input())
    
    if n == 1:
        print("NEW")
    elif n == 2:
        print("OPEN")
    elif n == 3:
        print("SAVE")
    elif n == 4:
        print("QUIT")
        break
    else:
        print("AGAIN")
