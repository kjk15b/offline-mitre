import os
import json

def convert_from_mitre(data : dict, software : str):
    aliases = ''
    if 'aliases' in data.keys():
        aliases = data['x_mitre_aliases']
    else:
        aliases = data['name']
    platforms = 'None listed'
    if 'x_mitre_platforms' in data.keys():
        platforms = data['x_mitre_platforms']
    response = {
        'software' : software,
        'labels' : data['labels'],
        'platforms' : platforms,
        'aliases' : aliases,
        'name' : data['name'],
        'type' : data['type'],
        'description' : data['description'],
        'created' : data['created'],
        'modified' : data['modified'],
        'domains' : data['x_mitre_domains']
    }
    return response

def get_all_groups():
    software_list = []
    softwares = os.listdir(
        os.path.join(os.getcwd(),
        'static/enterprise/software/')
        )
    for software in softwares:
        f = open(os.path.join('static/enterprise/software/',software), 'r')
        data = json.load(f)
        for ref in data['external_references']:
            if 'external_id' in ref.keys():
                if ref['external_id'][0] == 'S':
                    sid = ref['external_id']
        aliases = ''
        if 'aliases' in data.keys():
            aliases = data['x_mitre_aliases']
        else:
            aliases = data['name']
        platforms = 'None listed'
        if 'x_mitre_platforms' in data.keys():
            platforms = data['x_mitre_platforms']
        software_list.append(
            {
                'software' : sid,
                'name' : data['name'],
                'labels' : data['labels'],
                'aliases' : aliases,
                'platforms' : platforms,
                'modified' : data['modified']
            }
        )
    print(software_list)
    return software_list

def get_count():
    return len(os.listdir(os.path.join(os.getcwd(), 'static/enterprise/software/')))