sugar = int(input())
bag = 0
while sugar >=0: #총 설탕 무게가 0 될 때 까지 반복한다.
    if sugar % 5 == 0: # 5의 배수일 경우
        bag += (sugar//5) 
        print(bag)
        break
    sugar -= 3 #설탕이 5의 배수가 아닐 경우 3을 빼주고 다시 5의 배수인지 확인
    bag += 1 #이때 3을 한번 뺄 수 있으니 가방 수는 1 증가함
else:
   print(-1)
