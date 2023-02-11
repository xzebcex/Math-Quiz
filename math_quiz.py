# Math Quiz
import pyinputplus as pyip
import random
import sys

number_of_questions = 10
correct_answer = 0
attempts_taken = 1

for question_number in range(number_of_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s * %s = ' % (question_number + 1, num1, num2)

    while attempts_taken <= 10:
        try:
            # Right answer are handeled by allow_regexes
            # Wrong answer are handeled by block_regexes
            pyip.inputStr(prompt, allowRegexes=['^%s$' % (
                num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=10)
            break
        except:
            print('Time Out!')
            attempts_taken += 1
            if attempts_taken > 10:
                print("You've failed all 10 attempts. The game will now exit.")
                sys.exit()

    print('Correct')
    correct_answer += 1
    attempts_taken = 1

print("You've got %s out of %s questions correct." %
      (correct_answer, number_of_questions))
