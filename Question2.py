"""
Question 2
Group Name: DAN/EXT 55
Group Members:
Thuy Chuong Duong - S385201
Kar Keat Koh - S394886
Joshua Joseph Bargamento - S394292
Sihao Cui - S399370
"""

# Run the program
if __name__ == "__main__":
    # Prompt user to input a number and find all prime numbers up to that number
    prime_limit = int(input("Input: "))
        
    primes = [] 

    # Only check for prime numbers if the input is greather than or equal to 2
    if prime_limit >= 2:
        for num in range(2, prime_limit + 1):
            is_prime = True
            for divisor in range(2, int(num**0.5) + 1):
                if num % divisor == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)   
        # Output the results
        print("Output: ")
        print("Prime numbers found:", primes)
        print("Total primes found:", len(primes))
        print("Largest prime:", max(primes))
        print("Smallest prime:", min(primes))
        print("Sum of all primes:", sum(primes))
        
    # If the input is less than 2, print a message indicating that there are no prime numbers
    else:
        print("No prime number. Please enter a number greater than or equal to 2.")