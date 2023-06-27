import sys as sys
import time

var sleep_time_in_seconds = 60*3

# modelop.score
def action(datum):
	sys.stdout.flush()
	print(datum)

	yield datum

# modelop.metrics
def dict_metrics(datum):
  print("I'm lazy, so I'm going to sleep for ( " + sleep_time_in_seconds + " ) ")
  time.sleep(sleep_time_in_seconds) # Sleep for 3 minutes seconds
	yield {
		"foo": 1,
		"bar": "test result"
	}
