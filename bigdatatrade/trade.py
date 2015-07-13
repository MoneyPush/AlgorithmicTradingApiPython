#! /usr/bin/python2.7
#-*- coding: utf-8 -*-

from __future__ import unicode_literals
import requests
import ast
import json


class Urlformat:

    ''' This class allows to format an url given the necessary parameters

    - The necessary parameters are the following::

        :param host:  A hostname is a domain name assigned to a host
        computer.
        This is usually a combination of the host's local name
        with its parent domain's name.
        For example, en.example.org consists of
        a local hostname (en) and the domain name example.org.
        :param port:  A port is identified for each address
        and protocol by a 16-bit number.
        :param path:  The end of the path
        to get the required index value.

    - The final url should have the following format::

        :http://:host:/:port:/:path:

    Returns a formatted url string to access the server
    '''

    def __init__(self, host=None, port=None, path=None):
        ''' Constructor '''
        self.host = host
        self.port = port
        self.path = path

    def __str__(self):
        ''' Formatting '''
        url = "http://" + self.host
        if self.port is not None:
            url += ":" + self.port
        url += "/"
        if self.path is not None:
            url += self.path
        return url


class Request:

    ''' This class allows the user to query the financial market

    Currently, it can be used to most of the forex indexes
    on the financial market according to the users queries.

    '''

    def __init__(self, key):
        ''' Constructor '''
        self.options = {}
        self.options['key'] = key
        self.options['hostname'] = '62.210.69.57'
        self.options['endpath'] = "SubSymbol"
        self.options['portstream'] = "3002"
        self.options['timeout'] = 9.05

    def fetch(self, currencies):
        ''' Fetch financial datas

        Fetch and print to the default output a stream of indexes
        queried by the user

        - The parameters of this method are as follows::

            :param currencies: a dictionary of currencies
            formatted this way :           ['EUR/GBP', 'EUR/USD'].
            In order to get every forex indexes on the stream,
            it is also possible to write : ['AllSymbol']
            :type currencies: dictionnary

        :returns: None
        '''
        currURL = []
        try:
            json_acceptable_string = currencies.replace("'", "\"")
            self.options['currencies'] = json.loads(
                json_acceptable_string)['currencies']
            print('currencies parsed : ', self.options['currencies'])
        except KeyError as e:
            print("KeyError involving field : ", e)
        except ValueError as e:
            print("ValueError involving field : ", e)

        if (self.options['currencies'] == 'AllSymbol'):
            currURLstring = ['AllSymbol']
        else:

            for curr in self.options['currencies']:
                # print("curr : ", curr)
                currURL.append(curr.replace('/', '_'))
                # print("currURL : ", currURL)
                currURLstring = '%2c'.join(currURL)
                # print("currURLstring : ", currURLstring)

        endpath = self.options['endpath'] + '/' + \
            self.options['key'] + '/' + currURLstring
        url = Urlformat(self.options['hostname'],
                        self.options['portstream'], endpath)

        try:
            response = requests.get(str(url), verify=True,
                                    stream=True, timeout=self.options['timeout'])
            response.raise_for_status()
        except requests.exceptions.ConnectionError as e:
            print("Too Bad ! Connection Error : ", e.message)
        except requests.exceptions.HTTPError as e:
            print("HTTP Error : ", e.message)
        except requests.exceptions.ConnectTimeout as e:
            print("ConnectTimeout, you are out : ", e.message)
        except requests.exceptions.ReadTimeout as e:
            print("ReadTimeout ... too long between sended bytes: ", e.message)
        except ConnectionRefusedError as e:
            print("Connection Refused : ", e.message)
        except requests.exceptions.SSLError as e:
            print("That domain looks super sketchy, check your certificates : ",
                  e.message)

        response.encoding = 'utf8'

        lines = response.iter_lines(decode_unicode=True)
        for line in lines:
            if line:
                tick_line = json.loads(line)
                print(tick_line)


if __name__ == "__main__":
    key = "b0be3e7e6fe08feb0d3d2af68f27bb00"
    request = Request(key)
    # request.fetch("{'currencies': ['EUR/GBP', 'EUR/USD']}")
    request.fetch("{'currencies': ['AllSymbol']}")
