#!/usr/bin/python
# -*- coding: utf8 -*- 

import sys, csv
import StringIO
try:
	from markdown import markdown
except ImportError:
	def markdown(s):
		return s

stdin_str = sys.stdin.read()

rows = csv.reader(StringIO.StringIO(stdin_str), dialect=csv.Sniffer().sniff(stdin_str))

print "<table>"
for row in rows:
	print "<tr>" + "".join(["<td>%s</td>" % markdown(x) for x in row]) + "</tr>"
print "</table>"
