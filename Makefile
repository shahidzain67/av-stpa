#!/usr/bin/make

.PHONY: clean
clean:
	rm -f Documentation/control-diagram.png

.PHONY: docs
docs:
	java -jar ./Documentation/ditaa0_9/ditaa0_9.jar ./Documentation/control-diagram -o
