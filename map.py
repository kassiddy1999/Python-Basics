from random import shuffle
# function jumble with arguement word
def jumble(word):
    # creating a variable that contains word in a list
    anagram =list(word)
    # applying the shuffle module to the anagram
    shuffle(anagram)
    # rejoining the letters after reshuffling
    return''.join(anagram)
words = ['beetroot','carrots','potatoes']
anagrams = []

# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)
# using the map function
print(list(map(jumble,words)))

# using the comprehension method
print([jumble(word) for word in words])