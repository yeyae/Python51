#클래스 변수
class Family:
    lastname = "김"

print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

#클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징
