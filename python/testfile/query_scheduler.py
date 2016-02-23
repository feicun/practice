#!/usr/bin/env python
# encoding: utf-8

import requests
import json

from datetime import time
from apscheduler.schedulers.blocking import BlockingScheduler


def fetch_statistics():
    token = ""
    start = ""
    end = ""

    response = requests.get(
        'http://10.10.1.14:8777/v2/meters/cpu_util/statistics?' +
        'q.field=timestamp&q.op=ge&q.value=' + start +
        '&q.field=timestamp&q.op=lt&q.value=' + end +
        '&q.field=resource_id&q.op=eq&q.value=4dd6b611-24a7-4f48-8787-71719c06c750',
        headers={'X-Auth-Token': token}
    )

    print response
    parsed = json.loads(response.text)
    print json.dumps(parsed, indent=4, sort_keys=True)


def my_job(text):
    print text


def main():
    # Run this job in certian time, with parameter 'text'
    sched = BlockingScheduler()
    sched.add_job(my_job, 'interval', seconds=5, args=['test'])
    sched.start()
    # while True:
        # time.sleep(10)


if __name__ == "__main__":
    main()
