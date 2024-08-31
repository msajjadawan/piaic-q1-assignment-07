
'''
Instructions:
You are tasked with creating a Python program that serves as an interactive tool for a 
friend who enjoys exploring numbers. 
The program should begin by prompting the user to 
enter their name and then ask them for three of their favorite numbers.(Done) 
After gathering this information, 
the program should greet the user with a personalized message (Done)
that includes their name. The three numbers provided by the user should be stored in a list. 

The program should then check if any of the numbers are even or odd, and store this information 
in a separate list of tuples, where each tuple contains the number and a string 
indicating whether it is "even" or "odd". (done)

Following this, the program should use a for loop to iterate over the list of numbers, 
and for each number, it should create a tuple containing the number and its square. 
These tuples should be printed in a creative and engaging format.(done)

 Additionally, the program should calculate the sum of the three numbers and print the result, 
 accompanied by an encouraging message.
  
 Finally, the program should determine 
 if the sum is a prime number and notify the user with an appropriate message. 
 The goal is to make the tool both enjoyable and informative, allowing the user to explore 
 their favorite numbers in a fun and interactive way, while also introducing some interesting 
 logical checks.

'''
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