import os
import json

def convert_from_mitre(data : dict, tactic : str):
    response = {
        'tactic' : tactic,
        'name' : data['name'],
        'description' : data['description'],
        'created' : data['created'],
        'modified' : data['modified'],
        'domains' : data['x_mitre_domains']
    }
    return response

def get_all_tactics():
    tactics_list = []
    tactics = os.listdir(
        os.path.join(os.getcwd(),
        'static/enterprise/tactics/')
        )
    for tactic in tactics:
        f = open(os.path.join('static/enterprise/tactics/',tactic), 'r')
        data = json.load(f)
        tactics_list.append(
            {
            'tactic' : data['external_references'][0]['external_id'],
            'name' : data['name'],
            'modified' : data['modified'],
            }
        )
    print(tactics_list)
    return tactics_list

def get_count():
    return len(os.listdir(os.path.join(os.getcwd(), 'static/enterprise/tactics/')))