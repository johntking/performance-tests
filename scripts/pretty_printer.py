from datetime import datetime


def measure_execution_times(func, trials, **pass_to_func):

	durations = []

	for _ in trials:

		t0 = datetime.now()
		_ = func(**pass_to_func)
		t1 = datetime.now()
		durations.append((t1 - t0).total_seconds())

	durations.sort()

	return durations


#def pretty_print_times()



