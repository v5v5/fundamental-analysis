import csv

financial_statement_parameters_file = './data/financial_statement_parameters.ini'

def save_locator_template(statement_name: str, locators):
    import configparser
    config = configparser.ConfigParser()
    config[statement_name] = {}

    print(f'saving to {financial_statement_parameters_file} file...')
    for locator in locators:
        locator_name = locator[0]
        locator_template = locator[1].template
        config[statement_name][locator_name] = locator_template
        print(f'add locator: name={locator_name}, xpath={locator_template} to section {statement_name}')

    with open(financial_statement_parameters_file, 'a') as configfile:
        config.write(configfile)
    print(f'saved to {financial_statement_parameters_file} file')
