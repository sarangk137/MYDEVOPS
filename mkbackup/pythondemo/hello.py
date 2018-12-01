#!/usr/bin/python 
iadskjhaskjdfhakljshflkajsdfhlkajshd

def foo():
	f = open('/var/log/kern.log')
	lines = f.readlines()
	for line in lines:
		print int(line.split()[2].split(':')[2]) * 10
		


def bar():
	print("World")


''' 
###  First Int

i = 10
st = "Helo"
l = ['a','b','c']
dic= {'language':'Python', 'editor':'vi'}
'''
foo()
bar()
