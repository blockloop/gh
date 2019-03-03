#!/usr/bin/env python3
import sys
import subprocess
import webbrowser
import argparse
import platform

def sh(cmd,exit_on_fail=False):
	proc = subprocess.Popen(cmd,
		shell=True,
		stdout=subprocess.PIPE, 
		stderr=subprocess.PIPE)
	out,err = proc.communicate()
	code = proc.returncode
	if exit_on_fail and code != 0:
		err = err.decode('utf-8')
		sys.exit("Non-zero exit code ({})\nMessage: {}".format(code,err))
	return code,str(out+err, encoding='utf8')

def getBranch():
	code,out = sh("git branch --no-color", True)
	finds = [x for x in out.split('\n') if "*" in x]
	if len(finds) == 0:
		sys.exit("No branches found")
	return finds[0].split(" ")[1]

#
# Arguments
#
parser = argparse.ArgumentParser(description='Open browser to git remote')

parser.add_argument('-n', '--no-launch',
	dest="nolaunch",
	action='store_true',
	default=False,
	required=False,
	help="Don't launch the browser")

parser.add_argument("-b", "--branch",
	dest="branch",
	default=getBranch(),
	required=False,
	help="branch to open instead of current")

parser.add_argument("-r", "--remote",
	dest="remote",
	default="origin",
	required=False,
	help="Use remote by this name (Default: origin)")

opts = parser.parse_args()

#
# Parsing
#
code,output = sh("git remote -v", True)
remotes = [x for x in output.split("\n") if opts.remote in x]
if len(remotes) == 0:
	sys.exit("There's no remote by that name ({})".format(opts.remote))
remote = remotes[0]


url = remote\
	.split("\t")[1]\
	.split(" ")[0]\
	.replace(":", "/")\
	.replace(".git", "")\
	.replace("git@", "http://")

if opts.branch != "master":
	prefix = "tree" if "github" in url else "branch"
	url += "/{}/{}".format(prefix,opts.branch)

#
# Acting
#
print(url)
if opts.nolaunch:
	sys.exit(0)

# cygwin doesn't like webbrowser so we'll use cygstart
if 'cygwin' in platform.system().lower():
	from subprocess import call
	call(['cygstart', url])
else:
	webbrowser.open_new_tab(url)
