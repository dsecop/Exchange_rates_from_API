# Exchange rates from API
## Purpose
There are millions of APIs around the world that provide access to data.
APIs from a technical standpoint, they allow the capabilities of one computer program to be used by another. 
They are a means by which two different programs are able to communicate, so why not use them. The purpose of this script was to learn how to use the "requests" library.
##  How to use the script 
- you need to create an account on exchangeratesapi.io and generate your token
- put your token here ```'access_key': 'Place your token here'```
- run the script :wink:
## Description
The script retrieves the data from the API and then saves it to a .csv file. 
In this example, I used the exchangeratesapi.io website, which provides data on exchange rates. 
The script makes an HTTP request using the Python Requests package. The downloaded data is placed in the ``user's home`` directory, in the ``currency_data`` directory, which is created automatically, if it does not exist. In addition, only the last 7 files are saved and older ones are deleted.
---
**If you would like to contact me, here are my contact details:**<br>
:link: Check out my [LinkedIn profile](https://www.linkedin.com/in/dariusz-klimowicz/)<br> 
:mailbox: E-mail: <dariusz.secop@gmail.com>
