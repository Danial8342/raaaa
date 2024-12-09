import logging
from cProfile import label
from email.policy import default
from pickle import FLOAT
from tokenize import Number

from pywebio.input import input as pw_input
from pywebio.input import PASSWORD as PW_PASSWORD
from pywebio.input import textarea
from pywebio.output import put_text, put_error, put_success, put_warning, put_html

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
# HEADER
put_html('<h1>Welcome to the name processor</h1>')
put_html('<h2>demo version</h2>')

# GET LOGGING DATA
login = pw_input(label='введить свій вік.', required=True)
logging.info(f'User entered login {login}')

given_name = pw_input(label='Enter your name', required=True).strip()

name_length = len(given_name)
if name_length == 1:
    put_success(f'Strange name with length {name_length}')

name_length = len(given_name)
if name_length == 1:
    put_success(f'Strange name with length {name_length}')
elif name_length > 6:
    put_success(f'Діти до 6 років — безкоштовно. {name_length}')
elif name_length > 20:
    put_success(f'your name contains more 20 symbols {name_length}')
elif 10 >= name_length > 15:
    put_success(f'your name contains more 10-15 symbols {name_length}')
elif name_length < 5:
    put_success(f'your name contains less than 5 symbols {name_length}')
else:
    put_success(f'Name with length {name_length}')





    # weight = pw_input(label = 'Enter your weight', required = True, type=Number, min=25, default = 50, max=1000000)
    # program_work = pw_input(label = 'Enter your weight', required = True, type=FLOAT, min=1, default = 5, max=10)

put_error('The end')