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


def convert_from_mitre(data : dict):
    print(data)
    response = {
        'name' : data['name'],
        'description' : data['description'],
        'type' : data['type'],
        'created' : data['created'],
        'modified' : data['modified']
    }
    return response

def get_all_data_components():
    dc_list = []
    dcs = os.listdir(
        os.path.join(os.getcwd(),
        'static/enterprise/data-component/')
        )
    mappings_file = open('static/mappings/datacomponents.json', 'r')
    mappings = json.load(mappings_file)
    mappings_file.close()
    for dc in dcs:
        f = open(os.path.join('static/enterprise/data-component/',dc), 'r')
        data = json.load(f)
        dc_list.append(
            {
                'name' : data['name'],
                'type' : data['type'],
                'created' : data['created'],
                'modified' : data['modified'],
                'ref' : data['name'].replace(' ', '_'),
                'description' : data['description']
            }
        )
    print(dc_list)
    return dc_list

def get_count():
    return len(os.listdir(os.path.join(os.getcwd(), 'static/enterprise/data-component/')))