import os
import json

def get_mapped_data_components(dc : list):
    print("Mappings Search: {}".format(dc))
    mapped_dc = {}
    mappings_file = open('static/mappings/datacomponents.json', 'r')
    mappings = json.load(mappings_file)
    mappings_file.close()
    for component in dc:
        if component in mappings.keys():
            mapped_dc[component] = mappings[component]
    return mapped_dc

def get_car_analytics(technique : str):
    analytics = {}
    try:
        f = open('static/car/{}.json'.format(technique), 'r')
        data = json.load(f)
        analytics = data
        analytics['analytics_found'] = True
    except FileNotFoundError:
        analytics = {
            "analytics_found" : False
        }
    print(20*"*")
    print(analytics)
    return analytics

def convert_from_mitre(data : dict, technique : str):
    print(data)
    data_sources = ''
    mapped_dc = {}
    if 'x_mitre_data_sources' in data.keys():
        data_sources = data['x_mitre_data_sources']
        mapped_dc = get_mapped_data_components(data_sources)
    else:
        data_sources = 'None listed'
        mapped_dc['dc_found'] = False
    response = {
        'technique' : technique,
        'name' : data['name'],
        'description' : data['description'],
        'type' : data['type'],
        'created' : data['created'],
        'modified' : data['modified'],
        'kill_chain' : data['kill_chain_phases'],
        'detection' : data['x_mitre_detection'],
        'is_subtechnique' : data['x_mitre_is_subtechnique'],
        'data_sources' : data_sources,
        'platforms' : data['x_mitre_platforms'],
        'domains' : data['x_mitre_domains'],
        'analytics' : get_car_analytics(technique),
        'mapped_dc' : mapped_dc
    }
    return response

def get_all_techniques():
    ttp_list = []
    ttps = os.listdir(
        os.path.join(os.getcwd(),
        'static/enterprise/technique/')
        )
    for ttp in ttps:
        f = open(os.path.join('static/enterprise/technique/',ttp), 'r')
        data = json.load(f)
        technique = ''
        for ref in data['external_references']:
            if 'external_id' in ref.keys():
                if ref['external_id'][0] == 'T':
                    technique = ref['external_id']
        ttp_list.append(
            {
                'technique' : technique,
                'name' : data['name'],
                'type' : data['type'],
                'modified' : data['modified']
            }
        )
    print(ttp_list)
    return ttp_list

def get_count():
    return len(os.listdir(os.path.join(os.getcwd(), 'static/enterprise/technique/')))