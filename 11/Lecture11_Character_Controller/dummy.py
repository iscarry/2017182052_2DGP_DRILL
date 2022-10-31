from pico2d import*

class Star: #class 는 생성자가 없이 사용하면 객체의 의미가 아닌 namespace와 비슷한 역할을 한다.
    name = 'star'
    x = 100
    @staticmethod
    def change():
        x = 200
        print('x is ', x)

print('x is ', Star.x)

Star.change()

star = Star() #생성자가 없는데 생성이 가능할까?
print(type(Star))
print(Star.x) #만약 같은 이름의 클레스가 있다면 클레스가 우선
Star.change() # 호출블가
