# Length of Last word
# Create a function that given a string as a parameter of upper/lower case letters
# and empty space characters (" "), return the length of the last word.
# Meaning,the word that appears far most to the right if we loop through the words.
# Example Input: "Hello World"
# Example Output: 5

# One way to solve this problem 
def word_count():
    string = input(str("Enter your sentence.")).lower()
    words = string.split()
    last_word = words [-1]
    character_count = len(last_word)
    print(f'Last word: "{last_word}"" has {character_count} characters')
    return word_count
word_count()


# Another way to solve problem
def last_word(st):
    new_string = st.strip()
    word = new_string.split()
    return len(word[-1])
print(last_word(“Hello World”))