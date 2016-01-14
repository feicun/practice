import shlex


def newSplit(value):
    lex = shlex.shlex(value)
    lex.quotes = '\''
    lex.whitespace_split = True
    lex.commenters = ''
    return list(lex)

instance_name = "instance-0000033"
prefix = '''virsh -c qemu:///system qemu-agent-command '''
suffix = ''' \'{"execute": "guest-execute", "arguments": {"path": "/bin/sh", "argv": ["-c", "echo \"msg from vm\" > ~/testfile"]}}\''''
exe_cmd = prefix + instance_name + suffix
# result = newSplit('''virsh -c qemu:///system qemu-agent-command instance-00000036 \'{"execute": "guest-execute", "arguments": {"path": "/bin/sh", "argv": ["-c", "mkdir /opt/test"]}}\'''')
result = newSplit(exe_cmd)
print len(result)
print result
