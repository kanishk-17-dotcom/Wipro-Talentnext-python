                                      # EXERCISES

# Q.1 Write a program to read the entire content from a txt file and display it to the user.

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


# Q.2 Write a program to read first n lines from a txt file. Get n as user input.

n = int(input("Enter number of lines to read: "))
with open("sample.txt", "r") as file:
    for i in range(n):
        line = file.readline()
        if not line:
            break
        print(line.strip())


# Q.3 Write a program to accept input from user and append it to a txt file.

text = input("Enter text to append: ")
with open("sample.txt", "a") as file:
    file.write(text + '\n')
print("Text appended.")


# Q.4 Write a program to read contents from a txt file line by line and store each line into a list.

with open("sample.txt", "r") as file:
    lines = [line.strip() for line in file]
print(lines)


# Q.5 Write a program to find the longest word from the txt file contents, assuming that the file will 
#     have only one longest word in it.

with open("sample.txt", "r") as file:
    words = file.read().split()
    longest = max(words, key=len)
print("Longest word:", longest)


# Q.6 Write a program to count the frequency of a user entered word in a txt file.

word_to_count = input("Enter word to count: ")
with open("sample.txt", "r") as file:
    content = file.read().split()
    count = content.count(word_to_count)
print(f"'{word_to_count}' appears {count} times.")
