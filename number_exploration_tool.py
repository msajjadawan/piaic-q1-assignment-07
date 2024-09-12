

def main():
    name = input('Enter your name: ')
    
    num1 = int(input('Enter your first favorite number: '))
    num2 = int(input('Enter your second favorite number: '))
    num3 = int(input('Enter your third favorite number: '))

    print(f'Hello, {name}! Let\'s explore your favorite numbers.')

    favorite_numbers = [num1, num2, num3]
    print(f'Your favorite numbers are: {favorite_numbers}')

    even_odd_numbers = []
    for num in favorite_numbers:
        if num % 2 == 0:
            even_odd_numbers.append((num, 'even'))
        else:
            even_odd_numbers.append((num, 'odd'))
    print('Even/odd numbers:')
    for num, status in even_odd_numbers:
        print(f'{num} is {status}')
    
    squared_numbers = []
    for num in favorite_numbers:
        squared_numbers.append((num, num**2))
    print('\nSquared numbers:')
    for num, square in squared_numbers:
        print(f'{num}^2 = {square}')
    
    sum_numbers = sum(favorite_numbers)
    print(f'\nThe sum of your favorite numbers is {sum_numbers}')
    
    
    if sum_numbers > 1:
        for i in range(2, int(sum_numbers**0.5) + 1):
            if (sum_numbers % i) == 0:
                print(f'The sum ({sum_numbers}) is not a prime number.')
                break
            else:
                print(f'The sum ({sum_numbers}) is a prime number.')
    else:
        print(f'The sum ({sum_numbers}) is not a prime number.')

    


    



if __name__ == '__main__':
    main()