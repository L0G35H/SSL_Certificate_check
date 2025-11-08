import requests

#function to check SSL Certificate

def check_ssl(url):
    try:
        respose = requests.get(url, verify=True)
        print(f"SSL Certifide is valid for: {url}")
        
    except requests.exceptions.SSLError:
        print(f"SSL certificate is invalid for: {url}")
        
#List of websites to check 
website = [
    "https://www.imdb.com/",
    "http://chatgpt.com/",
    "https://self-signed.badssl.com"
]

#check SSL for website
for site in website:
    check_ssl(site)