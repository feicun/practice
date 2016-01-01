# http://docs.openstack.org/user-guide/common/cli_install_openstack_command_line_clients.html
import keystoneclient.v2_0.client as k_client
import ceilometerclient.v2 as c_client

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

# meterlist = ceilometer.meters.list()
# print meterlist
# print type(meterlist)
# for one in meterlist:
#     print '\n'
#     print type(one)

# network_outpacket_rate_sample = ceilometer.samples.list(
#     'network.outgoing.packets.rate')
# for each in network_outpacket_rate_sample:
#     print '\n'
#     # print each.resource_id, each.timestamp
#     print type(each)

# cpu_util_sample = ceilometer.samples.list(
#     'cpu_util')
# for each in cpu_util_sample:
#     print '\n'
#     print each.resource_id, each.timestamp
#     prin

# Create a query:
q = [
    # {"field": "timestamp", "op": "ge", "value": "2014-04-01T13:34:17"},
    {"field": "resource_id", "op": "eq", "value": "2f83f863-c4c6-445e-a0f4-7871c9ff641d"},
    {"field": "meter", "op": "eq", "value": "cpu_util"}
    ]

# Pass above query in:
cpu_util_sample = ceilometer.new_samples.list(q)
for each in cpu_util_sample:
    print '\n'
    print str(type(each)) + "value is: "
    print each
