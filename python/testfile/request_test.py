import requests
import json

start = '2016-01-19T18:58:29.002000'
end = '2016-01-20T18:58:29.002000'

response = requests.get(
    'http://10.10.1.14:8777/v2/meters/cpu_util/statistics?' +
    'q.field=timestamp&q.op=ge&q.value=' + start +
    '&q.field=timestamp&q.op=lt&q.value=' + end +
    '&q.field=resource_id&q.op=eq&q.value=4dd6b611-24a7-4f48-8787-71719c06c750',
    headers={'X-Auth-Token': 'b0f76b6d63a94c44880220f316e08e2f'}
    )

print response
parsed = json.loads(response.text)
print json.dumps(parsed, indent=4, sort_keys=True)


# q: [{"field": "timestamp",
#      "op": "ge",
#      "value": "2013-06-01T00:00:00"},
#     {"field": "timestamp",
#      "op": "lt",
#      "value": "2013-07-01T00:00:00"},
#     {"field": "resource_id",
#      "op": "eq",
#      "value": "64da755c-9120-4236-bee1-54acafe24980"}]
