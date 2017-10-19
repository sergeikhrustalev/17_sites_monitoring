import sys
import requests
import whois
from datetime import datetime


def load_urls4check(path):

    with open(path) as url_file:
        urls_from_file = url_file.readlines()

    return [url_list.strip() for url_list in urls_from_file]


def is_server_respond_with_200(url):

    status_ok = 200

    if requests.get(url).status_code == status_ok:
        return True

    return False


def get_domain_expiration_date(domain_name):

    exp_date = whois.whois(domain_name).expiration_date

    if isinstance(exp_date, list):
        exp_date = exp_date[0]

    return exp_date


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

        domain_name = url.split('//')[-1].split('/')[0]

        days_to_expire = (
            get_domain_expiration_date(domain_name) - datetime.today()
            ).days

        if days_to_expire > days_in_month:
            print('     <OK>\tDomain expiration date more then a month')
        else:
            print('<WARNING>\tDomain expiration date less then a month')
