import logging

from pywebio.input import input as pw_input
from pywebio.output import put_text
from pywebio.input import PASSWORD as PW_PASSWORD
from pywebio.input import textarea
from pywebio.output import put_text, put_error, put_success, put_warning, put_html
good_answers = 0


ANSWER_ONE = 'Юпітер'
ANSWER_TWO = '7'
ANSWER_THREE = 'Париж'
ANSWER_FOUR = 'Алюміній'
ANSWER_FIVE = '7'


question_one = pw_input(label='Яка планета є найбільшою у Сонячній системі')

question_two = pw_input(label='Яка планета є найбільшою у Сонячній системі')

question_three = pw_input(label='Яка планета є найбільшою у Сонячній системі')

question_four = pw_input(label='Який метал є основним у виробництві алюмінієвої фольги?')

question_five = pw_input(label='Яка планета є найбільшою у Сонячній системі')


if question_one == ANSWER_ONE:
    good_answers += 1


if question_two == ANSWER_TWO:
    good_answers += 1


if question_three == ANSWER_THREE:
    good_answers += 1


if question_four == ANSWER_FOUR:
    good_answers += 1


if question_five == ANSWER_FIVE:
    good_answers += 1



put_text(f'Ви правильно відповіли на {good_answers} з 5 запитань.')
