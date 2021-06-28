# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# The Encryption Function
def cipher_encrypt(plain_text, key): # key is used has an swifting value

    encrypted = ""

    for c in plain_text:

        if c.isupper():  # check if it's an uppercase character

            c_index = ord(c) - ord('A') # ord('A') used because A is the first value in the alphabet

            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.islower():  # check if its a lowercase character

            # subtract the unicode of 'a' to get index in [0-25] range
            c_index = ord(c) - ord('a')

            c_shifted = (c_index + key) % 26 + ord('a')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.isdigit():

            # if it's a number,shift its actual value
            c_new = (int(c) + key) % 10

            encrypted += str(c_new)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encrypted += c

    return encrypted

# The Decryption Function


def cipher_decrypt(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.isupper():

            c_index = ord(c) - ord('A')

            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.islower():

            c_index = ord(c) - ord('a')

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.isdigit():

            # if it's a number,shift its actual value
            c_og = (int(c) - key) % 10

            decrypted += str(c_og)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c

    return decrypted


plain_text = input("Enter the message:- ")

ciphertext1 = cipher_encrypt(plain_text, 4) # function calling is made

print("Your text message:\n", plain_text)

print("Encrypted ciphertext:\n", ciphertext1)


n = input("If you want to decrypt  any text press y else n: ")
if n == "y":
    ciphertext = input("Enter the Encrypted text:- ")
    decrypted_msg = cipher_decrypt(ciphertext, 4)
    print("The decrypted message is:\n", decrypted_msg)
else:
    print("Thank You!!")
