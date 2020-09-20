# guess my number
def main():
    import numpy as np
    
    print("Guess My Number 1-10 in 3 Tries Game")
    
    num = np.random.randint(1,11)
    
    def check(num, guess):
        if num < guess:
            return 'Too high!'
        else:
            return 'Too low!'
   
    def tries(ctn):
        if ctn > 1:
            return 'tries'
        else:
            return 'try'
    
    exit = 1
    count = 1
    
    print(f'***MVP: The number is: {num}***') # delete or comment out before publishing!
    
    while exit:
        guess = int(input(f'Your guess number {count}: '))
        
        if guess != num and count != 3:
            print(f'Nope! {check(num, guess)} You have {3-count} {tries(3-count)} left!')
            count += 1
            exit = 1
        elif guess == num and count < 4:
            print('Congratulations! You Won!')
            exit = 0
        else:
            print(f'{check(num, guess)}')
            print(f'Nope! Thanks for playing!')
            exit = 0
        

    
if __name__ == "__main__":
    main()