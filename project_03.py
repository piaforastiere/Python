
easy_level = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

easy_level_answers = ["function", "elements", "none", "list"]

medium_level = '''HyperText Markup Language (___1___) is the standard markup
language for creating web pages and web applications. With Cascading Style
Sheets (___2___), and ___3___, it forms a triad of cornerstone technologies
for the World Wide Web. Web browsers receive ___1___ documents from a webserver
or from local storage and render them into multimedia web pages. ___1___
describes the structure of a web page semantically and originally included cues
for the appearance of the ___4___.'''

medium_level_answers = ["HTML", "CSS", "JavaScript", "document"]

hard_level = '''___1___ is a widely used high-level, general-purpose,
interpreted, dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express concepts in
fewer lines of code than possible in languages such as C++ or Java. The
language provides constructs intended to enable writing ___2___ programs on
both a small and large scale. ___1___ supports multiple programming paradigms,
including object-___3___, imperative, ___4___ programming, and procedural
styles. It features a dynamic type system and automatic memory management and
has a large and comprehensive standard library.'''

hard_level_answers = ["Python", "clear", "oriented", "functional"]

replacement_list = ["__1__", "__2__","__3__","__4__"]

def level_choose():
    print "Welcome to fill in the blanks game. Remember you only have 4 attemps per question!"
    level_name = raw_input("Please choose level of difficulty: easy, medium, hard.\n").lower()
    if level_name=="easy":
        process_paragraph(easy_level, replacement_list, easy_level_answers)
    elif level_name=="medium":
        process_paragraph(medium_level, replacement_list, medium_level_answers)
    elif level_name=="hard":
        process_paragraph(hard_level, replacement_list, hard_level_answers)
    else:
        print "Please choose only easy, medium or hard"
    print level_choose


def process_paragraph(quiz, blanks, answers):
	print quiz
	for count_blanks in range(0, len(blanks)):
		answer_input = raw_input("Complete " + blanks[count_blanks] +": ")
		attempts = 1
		max_attempts = 4
		while answer_input.lower()!= answers[count_blanks]:
			attempts += 1
			answer_input = raw_input("No, no! The answer is not correct. Try again!" + blanks[count_blanks] + ": ")
			if attempts == max_attempts:
				print try_again()
		else:
			quiz = quiz.replace(blanks[count_blanks], answers[count_blanks])
			print("Correct! " + quiz)
	if len(blanks) == len(answers):
		print play_again()

def try_again():
    print ("Sorry!.")
    continue_game = raw_input(" Want to try again? y / n\n").lower()
    if continue_game == "y":
     level_choose()
    else:
     print "See you next time"

def play_again():
    print ("You did it great!")
    play_again = raw_input(" Want to try next level? y / n\n").lower()
    if play_again == "y":
        level_choose()
    else:
        print "That's a pity, but see you next time buddy!"


level_choose()
