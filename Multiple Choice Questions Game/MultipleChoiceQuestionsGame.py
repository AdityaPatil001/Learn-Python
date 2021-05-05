from Questions import Question

question_prompts = [
    "What color are Apples?\n(a) Red/Green\n(b) Violet\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Red\n(b) Yellow\n(c) Indigo\n\n",
    "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Magenta\n\n",
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
]
def run_tests(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")
run_tests(questions)