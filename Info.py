def findDuplicateCharacters(s):
    # Create a dictionary to store the frequency of each character
    charFrequency = {}
    # Create a list to store the duplicate characters
    duplicateCharacters = []
    # Iterate through the string
    for char in s:
        # If the character is already in the dictionary, increment its frequency by 1
        if char in charFrequency:
            charFrequency[char] += 1
            # If the frequency of the character is 2, add it to the list of duplicate characters
            if charFrequency[char] == 2:
                duplicateCharacters.append(char)
        # If the character is not in the dictionary, add it with a frequency of 1
        else:
            charFrequency[char] = 1
    # Return the list of duplicate characters
    return duplicateCharacters

# function to remove a specific number from a list
def removeNumber(lst, num):
    # Iterate through the list
    for i in lst:
        # If the current element is equal to the number to be removed, remove it from the list
        if i == num:
            lst.remove(i)
    # Return the modified list
    return lst

def removeEvenNumbersFromList():
    # Remove even numbers from the list
    return [i for i in nums if i % 2 != 0]


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]