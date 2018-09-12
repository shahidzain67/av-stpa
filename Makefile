#!/usr/bin/make

.PHONY: docs
docs:
	java -jar ./Documentation/ditaa0_9/ditaa0_9.jar ./Documentation/control-diagram -o
