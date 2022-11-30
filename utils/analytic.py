import os
import json

def convert_from_mitre(data : dict):
    coverage = []
    contributors = []
    implementations = []
    data_model_references = []
    unit_tests = []
    d3fend_mappings = []
    platforms = []
    if 'coverage' in data.keys():
        coverage = data['coverage']
    if 'contributors' in data.keys():
        contributors = data['contributors']
    if 'implementations' in data.keys():
        implementations = data['implementations']
    if 'data_model_references' in data.keys():
        data_model_references = data['data_model_references']
    if 'unit_tests' in data.keys():
        unit_tests = data['unit_tests']
    if 'd3fend_mappings' in data.keys():
        d3fend_mappings = data['d3fend_mappings']
    if 'platforms' in data.keys():
        platforms = data['platforms']
    response = {
        'title' : data['title'],
        'submission_date' : data['submission_date'],
        'information_domain' : data['information_domain'],
        'platforms' : platforms,
        'subtypes' : data['subtypes'],
        'analytic_types' : data['analytic_types'],
        'contributors' : contributors,
        'id' : data['id'],
        'description' : data['description'],
        'coverage' : coverage,
        'implementations' : implementations,
        'data_model_references' : data_model_references,
        'unit_tests' : unit_tests,
        'd3fend_mappings' : d3fend_mappings
    }
    return response

def get_all_analytics():
    analytic_list = []
    analytics = os.listdir(
        os.path.join(os.getcwd(),
        'static/car/')
        )
    for analytic in analytics:
        f = open(os.path.join('static/car/',analytic), 'r')
        data = json.load(f)
        implementations = []
        if 'implementations' in data.keys():
            implementations = data['implementations']
        analytic_list.append(
            {
                'id' : data['id'],
                'title' : data['title'],
                'analytic_types' : data['analytic_types'],
                'submission_date' : data['submission_date'],
                'description' : data['description'],
                'implementations' : implementations
            }
        )
    print(analytic_list)
    return analytic_list

def get_count():
    return len(os.listdir(os.path.join(os.getcwd(), 'static/car/')))