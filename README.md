# Sites Monitoring Utility

check_sites_health.py - checking sites http status and domain expiration information


# Requirements
This scripts require python3.5+  
See requirements.txt for a dependencies requirements.

# How to run
```bash
$python check_sites_health.py urls.txt
Checking for a site http://google.com
     <OK>	HTTP Status 200
     <OK>	Domain expiration date more then a month
Checking for a site http://instagram.com
     <OK>	HTTP Status 200
     <OK>	Domain expiration date more then a month
Checking for a site http://yandex.ru
     <OK>	HTTP Status 200
     <OK>	Domain expiration date more then a month
Checking for a site http://facebook.com
     <OK>	HTTP Status 200
     <OK>	Domain expiration date more then a month
Checking for a site http://mail.ru/
     <OK>	HTTP Status 200
     <OK>	Domain expiration date more then a month
Checking for a site http://vk.com
     <OK>	HTTP Status 200
     <OK>	Domain expiration date more then a month
Checking for a site http://devman.org/qwerty
<WARNING>	HTTP Status is not 200
     <OK>	Domain expiration date more then a month
```

File urls.txt must contains site urls divided by a new line


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
