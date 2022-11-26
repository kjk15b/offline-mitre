from flask import Flask, Response, json, render_template
from utils import technique, datasource, group, software, datacomponent

app = Flask(__name__)

@app.route('/enterprise/techniques/<ttp>')
def technique_route(ttp : str):
    ttp = ttp.upper()
    if ttp[0] == 'T' and ttp[1] != 'A':
        try:
            f = open('static/enterprise/technique/{}.json'.format(ttp), 'r')
            data = json.load(f)
            response = technique.convert_from_mitre(data, ttp)
            multiple_data_sources = False
            if type(response['data_sources']) == list:
                multiple_data_sources = True 
            no_ext_ref = len(response['external_ref'])
            return render_template('details.html', type='technique', ttp=response, multiple_data_sources=multiple_data_sources, no_ext_ref=no_ext_ref)
        except FileNotFoundError:
            return "404"
    else:
        return "404 Could not be found: {}".format(ttp)

@app.route('/api/enterprise/techniques/<ttp>')
def technique_api_route(ttp : str):
    ttp = ttp.upper()
    if ttp[0] == 'T' and ttp[1] != 'A':
        try:
            f = open('static/enterprise/technique/{}.json'.format(ttp), 'r')
            data = json.load(f)
            response = technique.convert_from_mitre(data, ttp)
            return response
        except FileNotFoundError:
            return "404"
    else:
        return "404 Could not be found: {}".format(ttp)

@app.route('/enterprise/techniques')
def techniques_route():
    ttps = technique.get_all_techniques()
    return render_template('table.html', type='technique', ttps=ttps)

@app.route('/api/enterprise/techniques')
def techniques_api_route():
    ttps = technique.get_all_techniques()
    return ttps



@app.route('/enterprise/datasources/<dsrc>')
def datasource_route(dsrc : str):
    dsrc = dsrc.upper()
    print(dsrc)
    if dsrc[0] == 'D' and dsrc[1] == 'S':
        try:
            f = open('static/enterprise/datasource/{}.json'.format(dsrc), 'r')
            data = json.load(f)
            response = datasource.convert_from_mitre(data, dsrc)
            return render_template('details.html', type='datasource', ds=response)
        except FileNotFoundError:
            return "404"
    else:
        return "404 Could not be found: {}".format(dsrc)

@app.route('/enterprise/datasources/<dsrc>')
def datasource_api_route(dsrc : str):
    dsrc = dsrc.upper()
    print(dsrc)
    if dsrc[0] == 'D' and dsrc[1] == 'S':
        try:
            f = open('static/enterprise/datasource/{}.json'.format(dsrc), 'r')
            data = json.load(f)
            response = datasource.convert_from_mitre(data, dsrc)
            return response
        except FileNotFoundError:
            return "404"
    else:
        return "404 Could not be found: {}".format(dsrc)


@app.route('/enterprise/datasources')
def datasources_route():
    datasources = datasource.get_all_datasources()
    return render_template('table.html', type='datasource', datasources=datasources)

@app.route('/api/enterprise/datasources')
def datasources_api_route():
    datasources = datasource.get_all_datasources()
    return datasources


@app.route('/enterprise/groups/<grp>')
def group_route(grp : str):
    grp = grp.upper()
    print(grp)
    if grp[0] == 'G':
        try:
            f = open('static/enterprise/groups/{}.json'.format(grp), 'r')
            data = json.load(f)
            response = group.convert_from_mitre(data, grp)
            return render_template('details.html', type='group', group=response)
        except FileNotFoundError:
            return "404"
    else:
        return "404 Could not be found: {}".format(grp)

@app.route('/enterprise/groups/<grp>')
def group_api_route(grp : str):
    grp = grp.upper()
    print(grp)
    if grp[0] == 'G':
        try:
            f = open('static/enterprise/groups/{}.json'.format(grp), 'r')
            data = json.load(f)
            response = group.convert_from_mitre(data, grp)
            return response
        except FileNotFoundError:
            return "404"
    else:
        return "404 Could not be found: {}".format(grp)

@app.route('/enterprise/groups')
def groups_route():
    groups = group.get_all_groups()
    return render_template('table.html', type='group', groups=groups)

@app.route('/api/enterprise/groups')
def groups_api_route():
    groups = group.get_all_groups()
    return groups


@app.route('/enterprise/software/<sw>')
def software_route(sw : str):
    sw = sw.upper()
    print(sw)
    if sw[0] == 'S':
        try:
            f = open('static/enterprise/software/{}.json'.format(sw), 'r')
            data = json.load(f)
            response = software.convert_from_mitre(data, sw)
            return render_template('details.html', type='software', software=response)
        except FileNotFoundError:
            return "404"
    else:
        return "404 Could not be found: {}".format(sw)

@app.route('/api/enterprise/software/<sw>')
def software_api_route(sw : str):
    sw = sw.upper()
    print(sw)
    if sw[0] == 'S':
        try:
            f = open('static/enterprise/software/{}.json'.format(sw), 'r')
            data = json.load(f)
            response = software.convert_from_mitre(data, sw)
            return response
        except FileNotFoundError:
            return "404"
    else:
        return "404 Could not be found: {}".format(sw)

@app.route('/enterprise/software')
def softwares_route():
    softwares = software.get_all_groups()
    return render_template('table.html', type='software', softwares=softwares)

@app.route('/api/enterprise/software')
def softwares_api_route():
    softwares = software.get_all_groups()
    return softwares

@app.route('/enterprise/data-component/<dc>')
def datacomponent_route(dc : str):
    try:
        f = open('static/enterprise/data-component/{}.json'.format(dc), 'r')
        data = json.load(f)
        print(data)
        response = datacomponent.convert_from_mitre(data)
        return render_template('details.html', type='datacomponent', dc=response)
    except FileNotFoundError:
        return "404"
    
@app.route('/api/enterprise/data-component/<dc>')
def datacomponent_api_route(dc : str):
    try:
            f = open('static/enterprise/data-component/{}.json'.format(dc), 'r')
            data = json.load(f)
            response = datacomponent.convert_from_mitre(data)
            return response
    except FileNotFoundError:
            return "404"

@app.route('/enterprise/data-component')
def datacomponents_route():
    dcs = datacomponent.get_all_data_components()
    return render_template('table.html', type='datacomponent', dcs=dcs)

@app.route('/api/enterprise/software')
def datacomponents_api_route():
    dcs = datacomponent.get_all_data_components()
    return dcs


@app.route('/enterprise')
@app.route('/')
def enterprise_route():
    e_list = [
        {
            'field' : 'techniques',
            'count' : technique.get_count(),
            'description' : 'Threats, Techniques and Procedures of APTs' 
        },
        {
            'field' : 'groups',
            'count' : group.get_count(),
            'description' : 'Advanced Persistent Threat Groups'
        },
        {
            'field' : 'datasources',
            'count' : datasource.get_count(),
            'description' : 'Datasources for use with detecting TTPs'
        },
        {
            'field' : 'software',
            'count' : software.get_count(),
            'description' : 'Software and Malware lists used by TTPs'
        },
        {
            'field' : 'data-component',
            'count' : datacomponent.get_count(),
            'description' : 'Data-Components of adversarial behavior'
        }
    ]
    return render_template('table.html', type='enterprise', e_list=e_list)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)