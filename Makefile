#!/usr/bin/make

.PHONY: default
default: docs

.PHONY: clean
clean:
	rm -f Documentation/control-diagram.png

.PHONY: docs
docs:
	dihaa ./Documentation/control-diagram -p
