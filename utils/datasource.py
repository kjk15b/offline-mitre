import os
import json

def convert_from_mitre(data : dict, datasource : str):
    response = {
        'datasource' : datasource,
        'name' : data['name'],
        'description' : data['description'],
        'type' : data['type'],
        'created' : data['created'],
        'modified' : data['modified'],
        'source' : data['x_mitre_collection_layers']
    }
    return response

def get_all_datasources():
    ds_list = []
    datasources = os.listdir(
        os.path.join(os.getcwd(),
        'static/enterprise/datasource/')
        )
    for ds in datasources:
        f = open(os.path.join('static/enterprise/datasource/',ds), 'r')
        data = json.load(f)
        for ref in data['external_references']:
            if 'external_id' in ref.keys():
                if ref['external_id'][0] == 'D' and ref['external_id'][1] == 'S':
                    ds_id = ref['external_id']
        ds_list.append(
            {
                'datasource' : ds_id,
                'name' : data['name'],
                'type' : data['type'],
                'modified' : data['modified']
            }
        )
    print(ds_list)
    return ds_list

def get_count():
    return len(os.listdir(os.path.join(os.getcwd(), 'static/enterprise/datasource/')))