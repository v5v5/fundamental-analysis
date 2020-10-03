import configparser

financial_statement_parameters_file = './data-output/financial_statement_parameters.ini'
config = configparser.ConfigParser()
config.optionxform = str

def save_locator_template(statement_name: str, locators):
    if os.path.exists(financial_statement_parameters_file):
        config.read(financial_statement_parameters_file)
    if not config.has_section(statement_name):
        config.add_section(statement_name)  

    print(f'saving to {financial_statement_parameters_file} file...')
    for locator in locators:
        locator_name = locator[0]
        locator_template = locator[1].template
        config.set(statement_name, locator_name, locator_template)
        print(f'add locator: name={locator_name}, xpath={locator_template} to section {statement_name}')

    with open(financial_statement_parameters_file, 'w') as configfile:
        config.write(configfile)
    print(f'saved to {financial_statement_parameters_file} file')

def print_financial_statement_parameters():
    config.read(financial_statement_parameters_file)
    for section in config.sections():
        print(f'Section: {section}')
        for key, value in config.items(section):
            print(f'{key}: {value}')

import os
directory = os.path.dirname(financial_statement_parameters_file)
if not os.path.exists(directory):
    os.makedirs(directory)