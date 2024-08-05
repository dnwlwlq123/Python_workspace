class MyDog:
    dog_sound = '왈왈'
    dog_legs = 4
    dog_type = '불독'
    date_of_creation = '20240801'
    country = '대한민국'

    def dog_work(self):
        print(f'우리 강아지는 {self.dog_sound} 짖습니다')
        print(f'우리 강아지의 다리는 {self.dog_legs} 개 입니다')
        print(f'우리 강아지의 종류는 {self.dog_type} 입니다')
        print(f'우리 강아지가 태어난 날은 {self.date_of_creation} 입니다')
        print(f'우리 강아지가 태어난 곳은 {self.country} 입니다')

    def __init__(self, dog_sound):
        self.dog_sound = dog_sound

뽀삐 = MyDog(dog_sound = '왈왈')
새로 = MyDog(dog_sound = '멍멍')
print(뽀삐.dog_sound)
print(새로.dog_sound)



