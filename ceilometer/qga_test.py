import subprocess
import json
import base64

# out = subprocess.check_output(["bash", "-c", "'ls /var/'"])
list_sock = subprocess.check_output("sudo bash -c 'ls /var/lib/libvirt/qemu/*.sock'", shell=True)
# out = subprocess.check_output("sudo bash -c 'ls /var/'", shell=True)

# out = subprocess.check_output(["ls", "-l"])
# print str(out) + "     "
# print type(out)

sock_files = list_sock.split()
# print type(sock_files)
# print sock_files

# instance-0000003a

for file_name in sock_files:
    # Get instance name
    temp_list = file_name.split(".")
    instance = temp_list[-2]

    # Write test file into vm
    prefix = '''virsh -c qemu:///system qemu-agent-command '''
    suffix = ''' '{"execute": "guest-execute", "arguments": {"path": "/bin/sh", \
    "argv": ["-c", "echo 'msg from vm' > ~/testfile"]}}' '''
    exe_cmd = prefix + instance + suffix
    subprocess.call(exe_cmd, shell=True)

    # Open test file from VM
    suffix = ''' '{"execute":"guest-file-open", \
    "arguments":{"path":"/home/ubuntu/testfile","mode":"r"}}' '''
    exe_cmd = prefix + instance + suffix
    output = subprocess.check_output(exe_cmd, shell=True)
    # print "message from vm: "
    # print output

    # Read test file from VM
    # dump = json.dumps(output)
    js1 = json.loads(output)
    handle = js1['return']
    suffix = ''' '{"execute":"guest-file-read", "arguments":{"handle":''' + str(handle) + ''',"count":1024}}' '''
    exe_cmd = prefix + instance + suffix
    output = subprocess.check_output(exe_cmd, shell=True)

    # Get message from VM
    js2 = json.loads(output)
    msg = js2['return']['buf-b64']
    msg_string = base64.b64decode(msg)

    # Close handle
    suffix = ''' '{"execute":"guest-file-close","arguments":{"handle":''' + str(handle) + '''}}' '''
    exe_cmd = prefix + instance + suffix
    output = subprocess.call(exe_cmd, shell=True)

    print "\n"
    print msg_string
