import csv

def save_locator_name(locator_name: str):
    print("saving locator name...")
    print("saved locator name")

def save_locator_xpath(locator_xpath: str):
    print("saving locator xpath...")
    print("saved locator xpath")

def save_locator_name_and_xpath(locator_name: str, locator_xpath: str):
    print("saving locator name...")
    print("saved locator name")

import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {
    'ServerAliveInterval': '45',
    'Compression': 'yes',
    'CompressionLevel': '9'
    }
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)
