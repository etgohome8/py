# A=[1]
# B=(1,)
# print(type(A))
# print(type(B))

# A = [1,2,True,"abc",1-2j]
# B = (1,2,True,"abc",1-2j)

# A[0] = "hello"
# A[2] = "world"
# print(A)

# B = list(B)   #형변환을 한 것. 
# B[0] = "hello"
# B = tuple(B)
# print(B)

# li = [1,1.2, "ABC", True, 3 ]

# print(li[0],li[3])
# li.append(4)                # 맨 뒤에 요소 추가
# li.insert(0,"Hello")        # 인덱스 지정해서 요소 추가 (index 0에 "Hello" 추가)
# del li[0]                   # 요소 삭제
# print(li.pop())             # 요소 반환, 삭제 (인덱스 지정 가능, ()의 경우 default:맨뒤 )
# print(li.count(1))          # 리스트 내 요소의 개수 반환
# print(li.index("ABC"))      # 특정 요소의 인덱스 반환
# li.sort()                   # 리스트 내의 요소가 동일한 경우*** 정렬
# li.reverse()                # 리스트 뒤집기
# a = li.copy()               # 리스트의 깊은 복사
# li.clear()                  # 리스트 초기화 (모든 요소 삭제)


# print(li)

# li = [1,2,3,4,1,2,3]
# a = li              # 얕은 복사 
# a[0] = 10           # 
# print(li)

# lo = [1,2,3,4,1,2,3]
# b=lo.copy()         # 깊은 복사
# b[0]=10             # 
# print(lo)

# A = [1,2,3,4]
# print(sum(A))
# print(len(A))
# print(sum(A)/len(A))  # 평균 구할 떄 좋음

# A = []
# N = int(input("수를 입력 : "))
# A.append(N)
# print(A)

# A = []
# N = int(input("수를 입력 : "))
# if N%2 == 1 :
#     A.append(N)
#     print(A)
# else :
#     print(A)

# for i in [1,2,3,4,5,6,7,8,9,10] :
#     print(i)


# A = []
# A.append(input("입력해봐~"))
# for i in A :
#     print(A)

# 1부터 1000 까지 출력
# for i in range(1001) :
#     print(i)

# for i in range(1,1001,1) :
#     print(i)

# for i in range(1000) :
#     print(1+i)

# range(101)
# range(20,75)
# range(100,1001)

#1에서 입력받은 수 N) 까지 출력
# N= int(input("수 입력: "))
# for i in range(1,N+1) :
#     print(i,end=" ")
# print()


#입력 받은 두 수 사이의 수 출력 (3,10)의 경우 4,5,6,7,8,9
# A= int(input("수 : "))
# B= int(input("수 : "))

# if B>A :
#     for i in range(A+1, B):
#         print(i,end=" ")
#     print()
# else :
#     for i in range(B+1, A):
#         print(i,end=" ")
#     print()

#1에서 100까지 합 구하기

# su = 0 
# for i in range(1,101):
#     su += i
# print(su)

# su= 0
# N = int(input("수: "))
# for i in range(1,N+1):
#     su += i
# print(su)

#factorial 프로그램
N = int(input("수 : "))
su = 1
for i in range(1,N+1):
    su *= i
print(su)



