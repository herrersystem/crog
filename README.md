# Crog
[![PyPI](https://img.shields.io/pypi/v/crog.svg)](https://pypi.python.org/pypi/apize/)
[![PyPI](https://img.shields.io/pypi/status/crog.svg)](https://pypi.python.org/pypi/apize/)
[![PyPI](https://img.shields.io/pypi/pyversions/crog.svg)](https://pypi.python.org/pypi/apize/)

Generate cronjobs for python scripts.

## Installation

```bash
pip install crog
```

## Get started

### Crog class

```python
from crog.crog import Crog
```

Class accept 6 arguments:
* name (__str__): name of cronjobs file. 
* minute (__str__ or __int__): number of minutes between each time the cron job runs, or the minute of each hour on which you wish to run the cron job.
* hour (__str__ or __int__): number of hours between each time the cron job runs, or the hour of each day on which you wish to run the cron job.
* month (__str__ or __int__): number of months between each time the cron job runs, or the month of the year in which you wish to run the cron job. (default: '*')
* week_day (__str__ or __int__): number of days between each time the cron job runs, or the day of the month on which you wish to run the cron job. (default: '*')
* month_day (__str__ or __int__): days of the week on which you wish to run the cron job. (default: '*')

### Example say_hello.py
```python
#!/usr/bin/env python3

import sys
from crog.crog import Crog

cron = Crog('helloworld', 15, 0) ## all days at 00:15
cron.user = 'herrer'

## Each lists represent 1 cronjob line with these parameters.
params = [['gerard'], ['ted']]


@cron.load(params=params)
## @cron.load() without params. 
def say_hello():
	if len(sys.argv) > 1:
		name = sys.argv[1]
		print('Hello %s'%name)

	else:
		print('Usage: %s <name>' % sys.argv[0])


if __name__ == '__main__':
	say_hello()

```

#### First execution

First execution create cronjobs file.

```
root@comuter# python say_hello.py
[crop] config file helloworld was created.
15 0 * * * herrer /root/app/say_hello.py gerard
15 0 * * * herrer /root/app/say_hello.py ted
```

#### Step to use

* Declare Crog object.
* Define user right for execution (default: 'root').
* Define params if script accept arguments (optionnal).
* Decorate main function with 'Crog.load' decorator.
* Execute your script first time (with __root__) to generate cronjobs config file.

#### Update cronjobs

Just change Crog object declaration and execute one more time your script.


