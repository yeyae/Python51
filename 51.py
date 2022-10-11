#클래스 변수
class Family:
    lastname = "김"

print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

#클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징!
#그렇기 떄문에 lastname을 박으로 바꾸면 박으로 출력됨

id(Family.lastname)
id(a.lastname)
id(b.lastname)

#id값이 모두 같음
