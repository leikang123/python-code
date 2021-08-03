import math
'''导入一个随机数的包'''
import random 
'''定义一个方法带参数的x'''

"""def guess(x):
    '''定义一个变量'''
    
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('sorry ,guess agin .Too low.')
        elif guess > random_number:
            print('sorry ,guess agin .Too hight')
    print(f'Yay,congrats.You have guessed the number {random_number} gor')"""
            
def computer_guess(x):
    low =1
    hight=x
    feedback =''
    while feedback != 'c' :
      if low !=hight:
         guess = random.randint(low,hight)
      else:
         guess =low
    feedback = input(f'is {guess} ,too low(l),too hight(h),or cabbory(c)')
    if feedback == 'h':
        hight == guess - 1
    elif feedback == 'l' :
        low = guess +1

print(f'Yay! The computer guessed your number,{guess},correctly!')
        
    
    
guess(20)
