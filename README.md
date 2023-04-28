# bioinfor_tools
![Stars](https://img.shields.io/pypi/v/bioinfor-tools.svg)

## Install
```angular2html
pip install bioinfor-tools
```

## Quick Guide
```angular2html
import bioinfor_tools as bt
import random

# Decorate a function that generates a Linux command.
@bt.cmd_wrapper(n_jobs=2)
def foo(a='hello'):
    cmd_list = ['sleep {} && echo done!'.format(random.randint(3, 5)) for _ in range(6)]
    return cmd_list, a

foo()

# using qusb.
@bt.cmd_wrapper(n_jobs=2,use_qsub=True)
def foo2(a='hello'):
    cmd_list = ['sleep {} && echo done!'.format(random.randint(3, 5)) for _ in range(6)]
    return cmd_list, a

foo2()
```