#assign variable to opening file
with open("story.txt", "r") as f:
    story = f.read()

#get unique elements
words = set()
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
        words.add(word)
        start_of_word = -1

#give us value of each of the words
answers = {}
#loop through unique words and ask user to give us the value
for word in words:
    answer = input("Enter a word for " + word + ": ")
    #create dictionary that has all the words associated with the value
    answers[word] = answer

print(answers)
