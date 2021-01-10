def reverse_string(word):
    """This function reverses a string using slicing"""
    reverse = word[::-1]
    return reverse

word = input("Enter a word: ")
#print(f"{reverse_string(word)}")

if word == reverse_string(word):
    print("This is a palindrome!")
else:
    print ("This is not a palindrome")