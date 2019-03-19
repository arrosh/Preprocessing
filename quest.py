from question import question

question_prompt = [
    "what colour is apples?\n(a) Red/green\n(b) yellow\n(c) white",
    "what colour is strawberry?\n(a)\nRed\n(b) yellow\n(c) purple",
    "what colour is orange?\n(a) Yellow\n(b)red\n(c) white"
]

questions = [
    question(question_prompt[0], "a"),
    question(question_prompt[1], "a"),
    question(question_prompt[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question_prompt)
        if answer == question.answer:
            score += 1
            print("you got " + str(score) + "/" + str(len(questions)) + " correct") 
        else:
            print("you got only " + str(score))
run_test(questions)
