import os
import json

def convert_from_mitre(data : dict, group : str):
    aliases = ''
    if 'aliases' in data.keys():
        aliases = data['aliases']
    else:
        aliases = data['name']
    response = {
        'group' : group,
        'name' : data['name'],
        'type' : data['type'],
        'created' : data['created'],
        'modified' : data['modified'],
        'aliases' : aliases,
        'domains' : data['x_mitre_domains']
    }
    return response

def get_all_groups():
    group_list = []
    groups = os.listdir(
        os.path.join(os.getcwd(),
        'static/enterprise/groups/')
        )
    for group in groups:
        f = open(os.path.join('static/enterprise/groups/',group), 'r')
        data = json.load(f)
        for ref in data['external_references']:
            if 'external_id' in ref.keys():
                if ref['external_id'][0] == 'G':
                    gid = ref['external_id']
        aliases = ''
        if 'aliases' in data.keys():
            aliases = data['aliases']
        else:
            aliases = data['name']
        group_list.append(
            {
                'group' : gid,
                'name' : data['name'],
                'aliases' : aliases,
                'modified' : data['modified']
            }
        )
    print(group_list)
    return group_list

def get_count():
    return len(os.listdir(os.path.join(os.getcwd(), 'static/enterprise/groups/')))