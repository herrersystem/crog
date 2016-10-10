#!/usr/bin/env python

from crog.crog import Crog
import os
import sys

cron = Crog('helloworld', 15, 0) ## all days at 00:15
cron.user = 'herrer'

params = [
	['gerard'],
	['ted']
]


@cron.load(params=params)
def say_hello():
	if len(sys.argv) > 1:
		name = sys.argv[1]
		print('Hello %s'%name)

	else:
		print('Usage: %s <name>'%sys.argv[0])


if __name__ == '__main__':
	say_hello()


