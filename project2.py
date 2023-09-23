#assign variable to opening file
with open("story.txt", "r") as f:
    story = f.read()

#store what different words are
words = []
#find starting index of the word
start_of_word = -1

target_start = "<"
target_end = ">"

#loop through our story, give us acces to the position of element in story
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    #find words to add to list
    if char == target_end and start_of_word != -1:
        #include ending index
        word = story[start_of_word: i + 1]
        words.append(word)
        start_of_word = -1

print(words)
