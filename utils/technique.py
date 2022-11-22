import os
import json

def convert_from_mitre(data : dict, technique : str):
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
        'data_sources' : data['x_mitre_data_sources'],
        'platforms' : data['x_mitre_platforms'],
        'domains' : data['x_mitre_domains']
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