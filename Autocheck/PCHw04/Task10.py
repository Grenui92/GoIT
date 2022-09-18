from random import randint
from typing import *


def get_random_password() -> str:
	result = ''
	for _ in range(8):
		result += chr(randint(40,126))
	return result