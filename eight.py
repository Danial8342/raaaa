import logging

from pywebio.input import input as pw_input
from pywebio.output import put_text
from pywebio.input import PASSWORD as PW_PASSWORD
from pywebio.input import textarea
from pywebio.output import put_text, put_error, put_success, put_warning, put_html

good_answers = 0

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

name = pw_input(label='Enter your name', required=True, type=PW_PASSWORD)
logging.debug(f'User entered name {name}')

ANSWER_ONE = 'Юпітер'
ANSWER_TWO = '7'
ANSWER_THREE = 'Париж'
ANSWER_FOUR = 'Алюміній'
ANSWER_FIVE = '7'

question_one = pw_input(label='Яка планета є найбільшою у Сонячній системі')

if question_one == ANSWER_ONE:
    put_success('You are right')
    good_answers += 1
else:
    put_error('wrong :(')

question_two = pw_input(label='Скільки континентів на Землі?')

if question_two == ANSWER_TWO:
    put_success('You are right')
    good_answers += 1
else:
    put_error('wrong :(')

question_three = pw_input(label='Як називається столиця Франції?')

if question_three == ANSWER_THREE:
    put_success('You are right')
    good_answers += 1
else:
    put_error('wrong :(')

question_four = pw_input(label='Який метал є основним у виробництві алюмінієвої фольги?')

if question_four == ANSWER_FOUR:
    put_success('You are right')
    good_answers += 1
else:
    put_error('wrong :(')

question_five = pw_input(label='Скільки кольорів у веселці?')

if question_five == ANSWER_FIVE:
    put_success('You are right')
    good_answers += 1
else:
    put_error('wrong :(')

procent = good_answers * 20

put_text(f'Ви правильно відповіли на {good_answers} з 5 запитань.')
put_text(f'Ви правильно відповіли на {procent}% з 100% запитань.')

logging.info(f'THE END FOR {name}')
