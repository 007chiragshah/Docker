#Why use the secrets module

#The cryptographically secure random generator generates random data using synchronization
#methods to ensure that no two processes can obtain the same data simultaneously.

#The random generator provided by the Python random module is a pseudo-random number generator
#that is not cryptographically secure. As a result secrets module is added in Python 3.6 and
#onwards to secure the random number generator.

#Use the secrets module for following standard security-related functions.
# 1. Generating random numbers,
# 2. Creating passwords and OTP.
# 3. Random token.
# 4. Password recovery safe URLs and session keys.

#to generate the secure numbers we need to import the class secrets
#Using the secrets.SystemRandom class, we can use all the functions of a random module.

#ex
import secrets
'''
# Getting systemRandom class instance out of secrets module
secretsGenerator = secrets.SystemRandom()

# secure random integer numbers

random_number = secretsGenerator.randint(0,10)
print(random_number)


# secure random integer number within given
random_number2 = secretsGenerator.randrange(4,40,4)
print(random_number2)


# Secure Random choice using secrets
number_list = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
secureChoice = secretsGenerator.choice(number_list)
print(secureChoice)

# Secure Random sample
secureSample = secretsGenerator.sample(number_list,3)
print(secureSample)

# Secure Random float number
secure_float = secretsGenerator.uniform(2.5, 25.5)
print(secure_float)

'''

#--------------------------------------------------------------------------------------
#Secret Module Function
import secrets
# 1. secrets.SystemRandom()	-  Get an instance of the secure random generator

# 2. secrets.randbelow(n) -  Generate a secure random integer number
#Use the secrets.randbelow function to generate a secure integer number.
#This function returns a secure random integer in the range [0, n).  Here n is the exclusive
# upper bound. 0 is the starting number in the range, and n is the last number.
#For example, secrets.randbelow(10) generate a single random number from 0 to 9.
for i in range(3):
    print(secrets.randbelow(10),end=',')

# 3. secrets.choice(seq) -  Returns a secure random element from a non-empty sequence
#The secrets.choice(sequence) method returns a secure randomly-chosen element from a non-empty
#sequence. Here sequence can be list, tuple, or string.
name = 'sdvsdvafbffb'
print(secrets.choice(name))
#or
name_list = ["Guido Van Rossum", "Bjarne Stroustrup", "Dennis Ritchie"]
print(secrets.choice(name_list))


# 4. secrets.randbits(k) - returns a secure unsigned integer with k random bits
#This method returns a secure unsigned integer with k random bits.
#It generates a random integer within a bit range.
#If k=4 then Unsigned integer From 0 to 15.
#k=8 then Unsigned integer From 0 to 255.
#If k=16 then Unsigned integer From 0 to 65,535, and so on.
print(secrets.randbits(4))
print(secrets.randbits(8))
print(secrets.randbits(16))
print(secrets.randbits(32))
print(secrets.randbits(64))


# 5. secrets.token_bytes([nbytes=None])	 -  Return a secure random byte string
#The secrets module provides functions for generating the secure tokens, useful for applications to generate reset
#password tokens and hard-to-guess URLs.

#Use the following functions to generate a secure token.

#1. secrets.token_bytes([nbytes=None]): Return a secure random byte string containing the
#               number of bytes. If n-bytes are not supplied, a reasonable default gets used.
#2. secrets.token_hex([nbytes=None]): Return a secure random text string in hexadecimal format.
#               The string has n-bytes random bytes, and each byte is converted to two hex
#               digits. If n-bytes are not supplied, a reasonable default gets used.
#3. secrets.token_urlsafe([nbytes=None]): Return a secure random URL-safe text string,
#               containing n-bytes random bytes. Use this method to generate secure
#               hard-to-guess URLs.

print(secrets.token_bytes(10))
print(secrets.token_hex(8))

PasswordResetLink = "demo.com/customer/eric/reset="
PasswordResetLink += secrets.token_urlsafe(20)
print(PasswordResetLink)

# 6. secrets.token_hex([nbytes=None])	   -  Return a secure random text string, in hexadecimal format
# 7. secrets.token_urlsafe([nbytes=None])  -  Return a secure random URL-safe text string
# 8. secrets.compare_digest(a, b)	       -  To reduce the risk of timing attacks

