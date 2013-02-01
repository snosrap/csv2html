csv2html
========

Convert CSV to formatted HTML using Markdown and Python's csv "sniffer" heuristics

Features
--------

* Guesses CSV format
* Formats each cell with Markdown (if available)

Example
-------

````bash
$ echo "**Name**,Alice" | python csv2html.py 
<table>
<tr><td><p><strong>Name</strong></p></td><td><p>Alice</p></td></tr>
</table>
````

````bash
$ echo "**Name**|**Age**
Alice|30
Bob|35" | python csv2html.py
<table>
<tr><td><p><strong>Name</strong></p></td><td><p><strong>Age</strong></p></td></tr>
<tr><td><p>Alice</p></td><td><p>30</p></td></tr>
<tr><td><p>Bob</p></td><td><p>35</p></td></tr>
</table>
````

Dependencies
------------

* [Python-Markdown](http://packages.python.org/Markdown/install.html)

Limitations
-----------

* Very short files with excessive Markdown will confuse Python's `csv` heuristics 
* No custom delimiters
