def ispalindrome(name: str):
    if name[::-1]==name:
        print("Yes it is a palindrome.")

def count_the_vowels(name: str):
    vowels = {'a','e','i','o','u'}
    count = 0
    for c in name:
        if c in vowels:
            count+=1
    print(f"No of vowels: {count}")

def frequency_of_letters(name: str):
    freq = {}
    for c in name:
        if c.isalpha():
            if c in freq:
                freq[c]+=1
            else:
                freq[c]=1
    print("Frequency of letters:",end=' ')
    for key,val in freq.items():
        print(f'{key}-{val}', end=' ')
    print()
