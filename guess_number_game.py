# guess my number
def main():
    import numpy as np
    
    print("Guess My Number 1-10 in 3 Tries Game")
    
    num = np.random.randint(1,11)
    
    def check(num, guess):
        if num < guess:
            return print('Too high!')
        else:
            return print('Too low!')
        
    
    exit = 1
    count = 1
    
    print(f'MVP: The number is: {num}')
    
    while exit:
        guess = int(input(f'Your guess number {count}: '))
        if guess != num and count != 3:
            exit = 1
            print(f'Nope! {check(num, guess)} You have {3-count} tries left!')
        elif guess == num and count < 4:
            print('Congratulations! You Won!')
            exit = 0
        else:
            print(f'Nope! {check(num, guess)} Thanks for playing!')
            exit = 0
        count += 1
        
    return '' 
    
if __name__ == "__main__":
    main()