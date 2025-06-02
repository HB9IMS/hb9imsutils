import pmutils as pm
import time


DELAY = "1m"


def _test_number_converter(string):
	print(f"{string} -> {pm.unitprint(pm.number_converter(string))} ({pm.number_converter(string)})")


@pm.timed
def test(x, y, z):
	# number_converter test
	delay = pm.number_converter(DELAY)
	# unitprint tests
	print(f"Delay in loop set to {delay} ({pm.unitprint(delay, 's')})")
	print()
	print(x)
	print(pm.unitprint(x, "m"))
	print(pm.unitprint(x, "m", power=1))
	print(pm.unitprint(x, "m", power=2))
	print(pm.unitprint(x, "m", power=3))

	# number_converter tests

	_test_number_converter("5k6")
	_test_number_converter("5.6k")
	_test_number_converter("5.6ex")
	_test_number_converter("5.6e9")

	# progres_bar tests

	t_s = time.time()
	for i in range(y):
		print(pm.progress_bar(i, y, time.time() - t_s), end="")
		time.sleep(delay)
	print(pm.progress_bar(y, y, time.time() - t_s))

	t_s = time.time()
	for i in range(y):
		print(pm.progress_bar(i, z, time.time() - t_s), end="")
		time.sleep(delay)
	print(pm.progress_bar(y, z, time.time() - t_s))

	# ProgressBar tests

	for i in pm.ProgressBar(range(y), y):
		time.sleep(delay)

	for i in pm.ProgressBar(range(y), z):
		time.sleep(delay)

	pb = pm.ProgressBar(None, y)
	for i in range(y):
		time.sleep(delay)
		pb()
	print()

	pb = pm.ProgressBar(None, z)
	for i in range(y):
		time.sleep(delay)
		pb()
	print()


test(1e-18, 200, 100)

time.sleep(5)