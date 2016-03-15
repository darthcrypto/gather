#!/usr/bin/env python

#A System Information Gathering Script

import subprocess

def uname_func():
	uname = "uname"
	uname_arg = "-a"
	print
	print "Gathering system information with %s command:" % uname
	subprocess.call([uname, uname_arg])
	print 

def disk_func():
	diskspace = "df"
	diskspace_arg = "-h"
	print "Gathering diskspace information %s command:" % diskspace
	subprocess.call([diskspace, diskspace_arg])
	print	

def main():
	uname_func()
	disk_func()

main()
	
