csv2html
========

Convert CSV to richly-formatted HTML using Markdown and Python's csv "sniffer" heuristics

Features
--------

* Automatic [sniffing](http://docs.python.org/2/library/csv.html#csv.Sniffer) of CSV delimiter
* Rich formatting via [Markdown](http://packages.python.org/Markdown/) (if available)

Examples
-------

#### Simple CSV

````bash
$ echo "Alice,Bob,Cathy" | python csv2html.py 
<table>
<tr><td><p>Alice</p></td><td><p>Bob</p></td><td><p>Cathy</p></td></tr>
</table>
````

<table>
<tr><td><p>Alice</p></td><td><p>Bob</p></td><td><p>Cathy</p></td></tr>
</table>

#### Pipe-Separated with Markdown

````bash
$ echo "**Name**|**Age**
Alice|30
Bob|*35*" | python csv2html.py
<table>
<tr><td><p><strong>Name</strong></p></td><td><p><strong>Age</strong></p></td></tr>
<tr><td><p>Alice</p></td><td><p>30</p></td></tr>
<tr><td><p>Bob</p></td><td><p><em>35</em></p></td></tr>
</table>
````

<table>
<tr><td><p><strong>Name</strong></p></td><td><p><strong>Age</strong></p></td></tr>
<tr><td><p>Alice</p></td><td><p>30</p></td></tr>
<tr><td><p>Bob</p></td><td><p><em>35</em></p></td></tr>
</table>

Dependencies
------------

* [Python-Markdown](http://packages.python.org/Markdown/install.html)

Limitations
-----------

* Very short files with excessive Markdown will confuse Python's csv "sniffer" heuristics 
* No custom delimiters

Similar
-------

* https://github.com/mrc/csv2html
