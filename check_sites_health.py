import sys
import requests
import whois
from datetime import datetime
from urllib.parse import urlparse


def load_urls4check(path):

    with open(path) as url_file:
        urls_from_file = url_file.readlines()

    return [url.strip() for url in urls_from_file if url != '\n']


def is_server_respond_with_200(url):

    return requests.get(url).status_code == requests.codes.ok


def get_domain_expiration_date(domain_name):

    exp_date = whois.whois(domain_name).expiration_date
    return exp_date[0] if isinstance(exp_date, list) else exp_date


if __name__ == '__main__':

    if len(sys.argv) == 1:
        sys.exit('Syntax: python check_sites_health.py <urls.txt>')

    days_in_month = 30

    url_list = load_urls4check(sys.argv[1])

    for url in url_list:

        print('Checking for a site {}'.format(url))

        if is_server_respond_with_200(url):
            print('     <OK>\tHTTP Status 200')
        else:
            print('<WARNING>\tHTTP Status is not 200')

        domain_name = urlparse(url).netloc

        days_to_expire = (
            get_domain_expiration_date(domain_name) - datetime.today()
            ).days

        if days_to_expire > days_in_month:
            print('     <OK>\tDomain expiration date more then a month')
        else:
            print('<WARNING>\tDomain expiration date less then a month')
