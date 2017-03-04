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
argument_parser.add_argument('-search'  ,action='store'                 ,dest='search_value'    ,help='Search string'                                           ,required=True  )
argument_parser.add_argument('-apikey'  ,action='store' ,default=False  ,dest='apikey_value'    ,help='Api key'                                                 ,required=True  )

argument_parser_result = argument_parser.parse_args()

search_string = ''
if argument_parser_result.country_value:
        search_string = search_string + 'Country:'+argument_parser_result.country_value + ' '
if argument_parser_result.org_value:
        search_string = search_string + 'org:"'+argument_parser_result.org_value + '" '
search_string = search_string + argument_parser_result.search_value


shodan_api_key = argument_parser_result.apikey_value

try:
        api = shodan.Shodan(argument_parser_result.apikey_value)
        results = api.search(search_string)
        print '#' + str(results['total']) + ' results found for ' + search_string
        for result in results['matches']:
                print(result['ip_str'])
except:
        print(sys.exc_info()[0])
