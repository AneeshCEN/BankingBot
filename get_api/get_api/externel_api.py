


import os.path
import sys
import yaml
from config import *




try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai


def db_query(parameter_json):
    return [parameter_json]


def process_for_loan(response, parameter_json, out_dict):
    if parameter_json['DOB'] != '' and parameter_json['Name'] != '' and parameter_json['PanNo'] != '':
        results = db_query(parameter_json)
        out_dict['ResultBuyer'] = results
        out_dict['messageText'].append([response['result']['fulfillment']['messages'][1]['payload']['messageText']])
    else:
        print 'processing'
        
    return out_dict
        
    



def call_api(dict_input):
    out_dict = {}
    out_dict['messageText'] = []
    out_dict['messageSource'] = dict_input['messageSource']
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    request = ai.text_request()
    request.lang = 'de'
    request.resetContexts = False
    request.session_id = dict_input['user_id']
    request.query = dict_input['messageText']
    response = yaml.load(request.getresponse())
    if response['result']['fulfillment']['speech'] != '':
        out_dict['messageText'].append(response['result']['fulfillment']['speech'])
    ent_dict = response['result']['parameters']
    ent_dict['_id'] = request.session_id
    if response['result']['action'] == 'LoanAvailability':
        out_dict = process_for_loan(response,ent_dict, out_dict)
    return out_dict









