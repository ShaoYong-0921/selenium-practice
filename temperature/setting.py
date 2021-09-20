import os

from dotenv import load_dotenv
load_dotenv()

from_email = os.getenv('from_email')
to_email = os.getenv('to_email')
password = os.getenv('password')

# print(password)