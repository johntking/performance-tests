import random


CHARS = 'abcdefghijklmnopqrstuvwxyz'


def misc(N):

	def inner():


		l = [CHARS[i % 26] for i in range(N)]
		yield 'list-init'
		random.shuffle(l)
		yield 'shuffle'
		
