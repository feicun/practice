import requests
import json

start = '2016-01-25T18:58:29.002000'
end = '2016-01-26T22:17:05.921000'
meter = 'cpu_util'
resource_id = '4dd6b611-24a7-4f48-8787-71719c06c750'

response = requests.get(
    'http://10.10.1.14:8777/v2/meters/' + meter + '?' +
    'q.field=timestamp&q.op=ge&q.value=' + start +
    '&q.field=timestamp&q.op=lt&q.value=' + end +
    '&q.field=resource_id&q.op=eq&q.value=' + resource_id,
    headers={'X-Auth-Token': 'e113874bffb2415aad424133962cfe56'}
    )

print response
parsed = json.loads(response.text)
print json.dumps(parsed, indent=4, sort_keys=True)
