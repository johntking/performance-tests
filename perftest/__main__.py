import argparse
import logging
import importlib

from .pretty_printer import pretty_print_times

logging.basicConfig(level = logging.INFO)



if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('module')
	parser.add_argument('function')
	parser.add_argument('function_ints', type = int, nargs = '*')
	parser.add_argument('--trials', type = int, nargs = '?', default = 3)

	args = parser.parse_args()

	mod = importlib.import_module(f'perftest.{args.module}_tests')
	func = getattr(mod, args.function)

	pretty_print_times(func(*args.function_ints), trials = args.trials)


"""
Usage example:

> python3 -m perftest numpy basic3d 10 --trials 5

"""

