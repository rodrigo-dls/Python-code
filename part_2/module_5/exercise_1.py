# Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not. Use the prior prime number exercise as a starting point. For example, a GET request for number 31 is given as: http://127.0.0.1:5000/prime_number/31. The response must be in the format of {"Number":31, "isPrime":true}.

from flask  import Flask, request

app = Flask(__name__)
@app.route('/prime_number/<int:number>')
def is_prime(number):
    isPrime = bool()
    if number <= 1:
        isPrime = False
    elif number == 2:
        isPrime = True  # 2 is a prime number
    elif number % 2 == 0:
        isPrime = False # numbers that are multiples of 2 are not prime numbers
    else:
        for i in range(3, number, 2):
            if number % i == 0:
                isPrime == False
        else:
            isPrime = True # if it passes everytest, then it is prime
            # print(f"{number} is a prime number.")
    return {
        'Number': number,
        'isPrime': isPrime
    }

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)