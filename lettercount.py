from sys import argv

script, filename = argv

alphabet_dict = dict.fromkeys(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'], 0)


def main():
    # open file
    # count for each character in alphabet
    # count number of times it appears in file
    # print count


    # for each char in file:
    #   check if it's a letter (using ord())
    #   increment how many times we've seen it
    # when done, print out the counts in alphabetical order

    f = open(filename)
    filetext = f.read()

    for char in filetext:
        if check_if_letter(char):
            char = char.lower()
            alphabet_dict[char] += 1 

    f.close()

    list_of_values = alphabet_dict.values()

    for i in range(len(list_of_values)):
        print list_of_values[i]


def check_if_letter(char):
    #check if either upper or lower, if upper, return lowercase
    if (65 <= ord(char) <= 90) or (97 <= ord(char) <= 122):
        return True
    else:
        return False

main()