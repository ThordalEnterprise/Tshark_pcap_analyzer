# Tshark_pcap_analyzer

[Intro]
This script is a Flask web application with several routes to perform various operations.

The application imports several Python modules such as Flask, pandas, numpy, and requests. The app has a route function index() that renders an HTML template 'index.html' and returns it to the user when they access the root URL "/".

It has several other routes including remove_string_from_other_txtfile(), which reads two text files, removes matching strings from one and writes the result into another file. Another route devide_big_txtfile() splits a large text file into smaller files. Yet another route replace_text() replaces a specific text string with another in a text file. Another route protocol_gathering_wireshark() is used to scrape a web page using selenium, specifically the content of the div tags containing fields in the Wireshark protocol.

The app uses Path to read and write text files and use urllib, requests, and pandas libraries to download, read and manipulate data from the internet.

[General]
This script is a Flask application that defines several endpoints (/, /remove_string_from_other_txtfile, /devide_big_txtfile, /replace_text, /protocol_gathering_wireshark) that perform various tasks, such as reading from and writing to text files, parsing web pages, and using Selenium to control a web browser.

/ endpoint displays an index.html page.
/remove_string_from_other_txtfile endpoint reads two text files (QA.txt and output.txt), removes any duplicate strings in output.txt that are found in QA.txt, and writes the unique strings to a new file called Resultxxx.txt. It also performs some text processing to modify the content of Resultxxx.txt.
/devide_big_txtfile endpoint reads from Result.txt and writes its contents to multiple text files, each containing a specified number of lines. The number of lines per file can be configured using the splitLen variable. The output file names are of the form output.1.txt, output.2.txt, etc.
/replace_text endpoint modifies Result.txt by replacing all occurrences of the substring ' -e ' with the string ' *^* -e '.
/protocol_gathering_wireshark endpoint uses Selenium to automate the process of scraping a web page (https://www.wireshark.org/docs/dfref/) and extracting protocol information. It performs several iterations of finding and scraping elements on the page, and it prints the results to the console.
The script also imports several Python packages (Flask, pandas, numpy, tempfile, csv, re, glob, sys, os, shutil, Path, datetime, listdir, isfile, request, Request, urlopen, requests, urllib.request) and defines a Flask application object called app.
