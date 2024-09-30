def back_Tracking (row, score):
    if (row ==3): #재귀함수 마치는 조건
        print(score)
        return 
    for i in range(3):
        if not check[i]: #논리 부정 연산자 : not 연산자, 조건 참이면 거짓으로, 조건 거짓이면 참으로 변환
            check[i] = True
            back_Tracking(row+1, score + list[row][i])
            check[i] = False
if __name__ == "__main__":
    list = [[2, 4, 3], [1, 3, 7], [6, 5, 6]]  # 3X3 행렬
    check = [False, False, False]

    back_Tracking(0,0)