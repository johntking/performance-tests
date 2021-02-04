from datetime import datetime
from collections import OrderedDict
import logging
import numpy as np


logging.basicConfig(level = logging.INFO)


def measure_execution_times(generator, trials):

	durations = OrderedDict()

	for _ in range(trials):

		t0 = datetime.now()

		for flag in generator():
			t1 = datetime.now()
			durations.setdefault(flag, []).append((t1 - t0).total_seconds())
			t0 = datetime.now()

	if {len(times) for flag, times in durations.items()} != {trials}:
		logging.warning('Irregular flag counts')

	return durations



def format_time_column(times, sig = 4):
	"""
	Designing this for cases when the times should be between 1ms and ~3h.
	Not expecting any perfectly round numbers (e.g., 10 seconds exactly)
	"""

	lo, hi = [
		int(np.ceil(np.log(x) / np.log(10)))
		for x in [min(times), max(times)]
	]

	if hi <= 1 and lo <= -1:
		fmt = f'{{0:.{sig - lo + 4}}}ms'
		factor = 1000
	else:
		fmt = f'{{0:.{sig - lo}}}s'
		factor = 1

	str_times = [fmt.format(t * factor) for t in times]

	if all([t.startswith('0') for t in str_times]):
		str_times = [t.lstrip('0') for t in str_times]

	return str_times



def pretty_print_times(
		generators,
		trials = 15,
		print_indices = [0, 2, 7, 12, 14],
		colsep = '  '
	):

	for g in generators:

		print(g.__name__)
		lines = [['flag'] + [f'({i})' for i in print_indices]]

		for flag, durs in measure_execution_times(g, trials = trials).items():
			durs.sort()
			lines.append([flag] + [durs[i] for i in print_indices])

		columns = []

		for j in range(len(lines[0])):

			c0 = [l[j] for l in lines]
			c1 = [c0[0]] + format_time_column(c0[1:]) if j else c0
			maxlen = max([len(x) for x in c1])
			c2 = [x.rjust(maxlen) for x in c1]
			columns.append(c2)

		for line in zip(*columns):
			print(colsep.join(line))





