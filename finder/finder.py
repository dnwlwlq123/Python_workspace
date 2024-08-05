"""Implement a better finder to find the right argument for the function. 

Your job is to implement a function that accepts another function(call this f) and additional information(related to possible candidates) as input, and returns the argument that f returns True. 

As a hint, f will return 'up' or 'down'. When f needs larger input value to return True, it will return 'up'. Else, it will return 'down'. 

You will be asked to implement 2 finder functions; naive_finder and smart_finder. 

1) naive_finder

Function naive_finder assumes that the test function only accepts integer inputs; therefore, naive_finder can (naively) iterate all the possible candidates. It will take long - but that's why it's called naive.  Function naive_finder accepts another function f and a candidate list as input. When naive_finder is called, it iterates over all possible candidates, applies all candidates to the function one at a time, and returns when the result is True. 

naive_finder should be able to find right argument for updown_game.updown_game_easy and updown_game.updown_game_medium. 

2) smart_finder

Function smart_finder accepts another function, and the max/min value of the input for the function f. To implement the smart_finder function, think of how you actually play '업다운 게임'. 

smart_finder should be able to find right argument for updown.game.updown_game_hard and animation.check_collision. 
"""
import random
def manual_finder(f):
    while True:
        i = input(f'Guess the argument!\nGuess is: ')
        res = f(float(i))
        if res is True:
            print(f'You found the right argument!; {float(i)}')
            return float(i)
            
        print(res) 
    
def naive_finder(f, lst = list(range(5))):
   for _ in lst:
        com = 0
        guest = random.randint(0, 10000000)
        print(f"Guest number: {guest}")

        guest_input = f(float(guest))
        print(f"{guest}")
        if guest_input is True:
            print(f"정답입니다. 정답은 {float(com)}입니다.") 
            return float(guest)
        else:
            print(f"계속 숫자 뽑는중....")
        print(guest_input)

    

def smart_finder(f, min_input = 0, max_input = 100):
    pass 