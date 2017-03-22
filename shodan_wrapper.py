'''
Created on 4 mar. 2017

@author: glezo1
'''

import shodan
import sys
import argparse

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('-country' ,action='store' ,default=False  ,dest='country_value'   ,help='Country to search in'                                                    )
argument_parser.add_argument('-org'     ,action='store' ,default=False  ,dest='org_value'       ,help='Organizacion (ASN). Encapsulate between " if seval words'                )
argument_parser.add_argument('-port'    ,action='store' ,default=False  ,dest='port_value'      ,help='Port'                                                                    )
argument_parser.add_argument('-search'  ,action='store' ,default=False  ,dest='search_value'    ,help='Banner to search for'                                                    )
argument_parser.add_argument('-apikey'  ,action='store' ,default=False  ,dest='apikey_value'    ,help='Api key'                                                 ,required=True  )

argument_parser_result = argument_parser.parse_args()

search_string = ''
number_of_search_criteria = 0
if argument_parser_result.country_value:
        search_string = search_string + 'Country:'+argument_parser_result.country_value + ' '
        number_of_search_criteria = number_of_search_criteria + 1
if argument_parser_result.org_value:
        search_string = search_string + 'org:"'+argument_parser_result.org_value + '" '
        number_of_search_criteria = number_of_search_criteria + 1
if argument_parser_result.port_value:
        search_string = search_string + 'port:'+argument_parser_result.port_value + ' '
        number_of_search_criteria = number_of_search_criteria + 1
if argument_parser_result.search_value:
        search_string = search_string + argument_parser_result.search_value
        number_of_search_criteria = number_of_search_criteria +1

if number_of_search_criteria == 0:
        argument_parser.print_help()
        sys.exit(1)

shodan_api_key = argument_parser_result.apikey_value

try:
        api = shodan.Shodan(shodan_api_key)
        results = api.search(search_string)
        print '#' + str(results['total']) + ' results found for ' + search_string
        for result in results['matches']:
                #print(result['ip'])
                print(result['ip_str'])
                #print(result['data'])
except:
        print(sys.exc_info()[0])
