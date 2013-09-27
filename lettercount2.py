from sys import argv

script, filename = argv

def main():
    # The main() function takes a command like argument that is a text file and prints out how many times each letter appears, alphabetically.
    f = open(filename)
    filetext = f.read()
    f.close()

    # initializes an empty array that has a length of 26
    alphabet_list = [0] * 26

    # for each character in the file, check if the character is a letter, conver to lowercase...
    for char in filetext:
        char = char.lower()
        if check_if_letter(char):
            # and increment the appropriate counter. in order to access the 
            # appropriate index where a = 0, we can subtract the value of ord
            # ('a') (97) from the ord value of the current character, e.x.
            # if the letter is s, ord('s') is 115. 155 - 97 = 18. S is the 19th
            # letter in the alphabet.
            alphabet_list[ord(char) - ord('a')] += 1 

    # finally, print out each of the values of alphabet_list on their own line.
    for count in alphabet_list:
        print count

def check_if_letter(char):
    # check if a character is a lowercase letter
    if ord(char) in range(ord('a'),ord('z') + 1):
        return True
    else:
        return False

main()