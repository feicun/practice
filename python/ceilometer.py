import keystoneclient.v2_0.client as k_client
import ceilometerclient.v2 as c_client

OS_USERNAME = "admin"
OS_PASSWORD = "123456"
OS_TENANT_NAME = "admin"
OS_AUTH_URL = "http://10.10.1.16:5000/v2.0/"
CEILOMETER_ENDPOINT = "http://10.10.1.16:8777"

keystone = k_client.Client(auth_url=OS_AUTH_URL, username=OS_USERNAME,
                           password=OS_PASSWORD, tenant_name=OS_TENANT_NAME)

auth_token = keystone.auth_token
ceilometer = c_client.Client(
    endpoint=CEILOMETER_ENDPOINT, token=lambda: auth_token)

meterlist = ceilometer.meters.list()
# print meterlist

network_outpacket_rate_sample = ceilometer.samples.list(
    'network.outgoing.packets.rate')
for each in network_outpacket_rate_sample:
    print '\n'
    print each.resource_id, each.timestamp
