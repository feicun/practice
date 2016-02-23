#!/usr/bin/env python
# encoding: utf-8

import requests
import json
import ceilometerclient.v2 as c_client
import keystoneclient.v2_0.client as k_client

from apscheduler.schedulers.blocking import BlockingScheduler


def create_ceilomenter_client():
    OS_USERNAME = "admin"
    OS_PASSWORD = "su123"
    OS_TENANT_NAME = "admin"
    OS_AUTH_URL = "http://10.10.1.14:5000/v2.0/"
    CEILOMETER_ENDPOINT = "http://10.10.1.14:8777"

    keystone = k_client.Client(auth_url=OS_AUTH_URL, username=OS_USERNAME,
                               password=OS_PASSWORD, tenant_name=OS_TENANT_NAME)

    auth_token = keystone.auth_token

    ceilometer = c_client.Client(
        endpoint=CEILOMETER_ENDPOINT, token=lambda: auth_token)
    return ceilometer


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
    ceilometer = create_ceilomenter_client()
    resources = ceilometer.resources.list()
    for i in resources:
        print '\n'
        print i
    # Run this job in certian time, with parameter 'text'
    sched = BlockingScheduler()
    sched.add_job(my_job, 'interval', seconds=5, args=['test'])
    sched.start()


if __name__ == "__main__":
    main()
