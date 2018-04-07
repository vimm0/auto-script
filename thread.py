import subprocess
commands = [
	'ls', 'pwd', 'whoami'
]
processes = [subprocess.Popen(cmd, shell=True) for cmd in commands]
for i,p in enumerate(processes):
	# import ipdb
	# ipdb.set_trace()
	while p.returncode == None:
		output, _ = p.communicate()
		print('RETURN: {} {}'.format(p.returncode, i))
		print('stderr: {} {}'.format(p.stderr, i))
		print('stdin: {} {}'.format(p.stdin, i))
		print('stdout: {} {}'.format(p.stdout, i))
		print('terminate: {} {}'.format(p.terminate(), i))
		print('pid: {} {}'.format(p.pid, i))
		print('poll: {} {}'.format(p.poll(), i))
		print('_: {} {}'.format(_, i))
		print('output: {} {}'.format(output, i))
print('condition not matched')
