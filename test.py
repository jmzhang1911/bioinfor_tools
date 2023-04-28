#!/share/nas2/genome/biosoft/Python//3.7.3/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2023/4/28 09:16
# @Author : jmzhang
# @Email : jmzhang1911@gmail.com
import logging

import bioinfor_tools as bt
from bioinfor_tools._bio_basic import BioBasic


@bt.cmd_wrapper(n_jobs=5)
def foo():
    cmd = list()
    for i in range(10):
        cmd.append('echo {} && sleep 6'.format(i, i))

    #cmd.insert(3, 'xxx')
    logging.info(cmd)
    return cmd, 'hello'


class B(bt.BioBasic):
    pass


bt.cmd(['sleep 2 && echo done'])
bt.cmd(['sleep 3 && echo done'])
foo()

# foo()
# print('done')

# SuperFastPython.com
# example of stopping all running tasks when one task fails
from time import sleep
from threading import Event
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
from concurrent.futures import FIRST_EXCEPTION


# mock target task function
def work(event, name):
    # pretend read data for a long time
    for _ in range(10):
        # pretend to read some data
        sleep(3)
        # check if this task should fail
        if name == 6:
            print(f'Task has failed, name={name}')
            raise Exception('Something bad happened')
        # check if the task should stop
        if event.is_set():
            print(f'Stopping, name={name}')
            return

# create an event used to stop running tasks
# event = Event()
# # create a thread pool
# with ThreadPoolExecutor(5) as executor:
#     # execute many tasks
#     futures = [executor.submit(work, event, i) for i in range(10)]
#     # wait for all tasks to complete, or one task to fail
#     print('Waiting for tasks to complete, or fail...')
#     done, not_done = wait(futures, return_when=FIRST_EXCEPTION)
#     # check if not all tasks are done
#     if len(done) > 0 and len(done) != len(futures):
#         # check if an exception was raised
#         future = done.pop()
#         if future.exception() != None:
#             print(f'One task failed with: {future.exception()}, shutting down')
#             # cancel any scheduled tasks
#             for future in futures:
#                 future.cancel()
#             # stop all running tasks
#             event.set()
# print('All done.')
