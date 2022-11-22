import json
MITRE='mitre.json'
f = open('static/{}'.format(MITRE))

data = json.load(f)

for object in data['objects']:
    if 'external_references' in object.keys():
        for ref in object['external_references']:
            if 'external_id' in ref.keys():
                print(ref['external_id'])
                enterprise_object = None
                found_tag = False
                if ref['external_id'][0] == 'T' and ref['external_id'][1] != 'A':
                    enterprise_object = open('static/enterprise/technique/{}.json'.format(ref['external_id']), 'w')
                    found_tag = True
                elif ref['external_id'][0] == 'D' and ref['external_id'][1] == 'S':
                    enterprise_object = open('static/enterprise/datasource/{}.json'.format(ref['external_id']), 'w')
                    found_tag = True
                elif ref['external_id'][0] == 'S' :
                    enterprise_object = open('static/enterprise/software/{}.json'.format(ref['external_id']), 'w')
                    found_tag = True
                elif ref['external_id'][0] == 'G':
                    enterprise_object = open('static/enterprise/groups/{}.json'.format(ref['external_id']), 'w')
                    found_tag = True
                if found_tag:
                    enterprise_object.write(json.dumps(object, indent=3))
                    enterprise_object.close()

f.close()