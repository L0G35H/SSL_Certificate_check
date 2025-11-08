# SSL_Certificate_check

SSL Certificate Checker 

This repository contains a simple Python script that checks whether a website’s SSL certificate is valid. It uses the requests library to send secure HTTPS requests and identifies sites with valid or invalid SSL configurations.

Features

✅ Checks SSL certificate validity for any URL

✅ Handles SSL errors gracefully

✅ Supports multiple websites via a simple list

✅ Easy to extend and integrate into larger security or monitoring tools

How It Works

The script sends a request to each website in the list using verify=True.

If the SSL certificate is valid → It prints a success message

If invalid or self-signed → It catches the exception and prints an error

Tech Used

Python

Requests library

Use Case

Quick security testing

Educational demonstration of SSL verification

Website monitoring tools

Automation scripts
