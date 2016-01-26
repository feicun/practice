import requests
import json

# url = 'http://10.10.1.14:8777/v2/query/samples/statistics'
# data = {
#     'filter': {"=": {"counter_name": "instance"}},
#     'groupby': ["project_id"],
#     'period': 900,
# }
# filter_ = '{\"and\":[{\"=\": {\"resource_id\": \"10.10.1.14\"}}, {\"=\": {\"resource_id\": \"10.10.1.15\"}}]}'

# headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'X-Auth-Token': '1d2bef70ddf3451bbb4cd6b9200da001'}
# r = requests.post(url, data=json.dumps(filter_), headers=headers)
# r = requests.post(url, json=data, headers=headers)
# print r
# parsed = json.loads(r.text)
# print json.dumps(parsed, indent=4, sort_keys=True)

url = 'http://10.10.1.14:8777/v2/query/samples'
data = {
    "filter": "{\"and\":[{\"=\": {\"counter_name\": \"cpu_util\"}},{\">\": {\"counter_volume\": 0.13}},{\"<\": {\"counter_volume\": 0.17}}]}",
    "limit": 4
}
headers = {'Content-type': 'application/json', 'X-Auth-Token': 'e113874bffb2415aad424133962cfe56'}
r = requests.post(url, data=json.dumps(data), headers=headers)

print r
parsed = json.loads(r.text)
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
