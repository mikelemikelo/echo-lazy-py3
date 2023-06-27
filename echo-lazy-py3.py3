import sys as sys
import time

sleep_time_in_seconds = 60*3

# modelop.score
def action(datum):
	sys.stdout.flush()
	print(datum)
	act_lazy(sleep_time_in_seconds)

	yield datum


def act_lazy(sleep_time_in_seconds):
	print("I'm lazy, so I'm going to sleep for ( " + str(sleep_time_in_seconds) + " ) ")
	time.sleep(sleep_time_in_seconds) # Sleep for 3 minutes seconds

# modelop.metrics
def dict_metrics(datum):
	act_lazy(sleep_time_in_seconds)
	yield {
		"foo": 1,
		"bar": "test result"
	}
