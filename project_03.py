#REPLACEMENT LIST:
replacement_list= ["___1___","___2___", "___3___", "___4___"]
easy_level= '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
easy_level_answer = ["function", "elements", "none", "list"]
medium_level= '''HyperText Markup Language (___1___) is the standard markup
language for creating web pages and web applications. With Cascading Style
Sheets (___2___), and ___3___, it forms a triad of cornerstone technologies
for the World Wide Web. Web browsers receive ___1___ documents from a webserver
or from local storage and render them into multimedia web pages. ___1___
describes the structure of a web page semantically and originally included cues
for the appearance of the ___4___.'''
medium_level_answer = ["HTML", "CSS", "JavaScript", "document"]
hard_level = '''___1___ is a widely used high-level, general-purpose,
interpreted, dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express concepts in
fewer lines of code than possible in languages such as C++ or Java. The
language provides constructs intended to enable writing ___2___ programs on
both a small and large scale. ___1___ supports multiple programming paradigms,
including object-___3___, imperative, ___4___ programming, and procedural
styles. It features a dynamic type system and automatic memory management and
has a large and comprehensive standard library.'''
hard_level_answer = ["Python", "clear", "oriented", "functional"]


def level():
    print "Welcome to fill in the blanks game. Remember you only have 4 attemps per question!"
    level_name = raw_input("Please choose level of difficulty: easy, medium, hard.").lower()
    if level_name == "easy":
        process_quiz(easy_level, replacement_list, easy_level_answer)
    elif level_name == "medium":
        process_quiz(medium_level, replacement_list, medium_level_answer)
    elif level_name == "hard":
        process_quiz(hard_level, replacement_list, hard_level_answer)
    else:
        print "Please choose between easy, medium & hard"
    print level


def process_quiz(quiz, blanks, answers):
    print quiz
    for count_blanks in range(0, len(blanks)):
        answer_input = raw_input("Complete " + blanks[count_blanks] + ":")
        attemps = 1
        max_attempts = 4
        while answer_input.lower() != answers[count_blanks]:
            attemps += 1
            answer_input = raw_input("No, no! The answer is not correct. Try again!" + blanks[count_blanks])
            if attemps == max_attempts:
                print ("Sorry! Try again next time")
                play_again = raw_input("You want to try again? Y / N").lower()
                if play_again == "Y":
                    print level()
                else :
                    print "Maybe next time!"
            else:
                quiz = quiz.replace(blanks[count_blanks], answers[count_blanks])
                print ("Thats correct! " + quiz)
            if len(blanks) == len(answers):
                print ("You did it great! Want to try next level?")
                level()

level()





# def word_in_text(word, parts_of_text):
#     for pos in parts_of_text:
#         if pos in word:
#             return pos
#     return None
#
# def complete_text(new_string, parts_of_text):
#     replaced_word = []
#     new_string = new_string.split()
#     for word in new_string:
#         replacement_word = word_in_text(word, parts_of_text)
#         if replacement_word != None:
#             user_input = raw_input ("Guess the word for: " + replacement_word + " ")
#             word = word.replace(replacement_word, user_input)
#             replaced_word.append(word)
#         else:
#             replaced_word.append(word)
#     replaced_word = " ".join(replaced_word)
#     return replaced_word
#
# print "Please choose level of difficulty: easy, medium, hard"
#
# print complete_text(text_string, replacement_list)
