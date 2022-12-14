from flask import Flask, Response, json, render_template
from utils import technique, datasource, group, software, datacomponent, analytic, tactic

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
            return render_template('404.html', content="Could not find: {}".format(ttp), type="technique")
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
            return render_template('404.html', content="Could not find: {}".format(dsrc), type="Datasource")
    else:
        return "404 Could not be found: {}".format(dsrc)

@app.route('/api/enterprise/datasources/<dsrc>')
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
            return render_template('404.html', content="Could not find: {}".format(grp), type="group")
    else:
        return "404 Could not be found: {}".format(grp)

@app.route('/api/enterprise/groups/<grp>')
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
            return render_template('404.html', content="Could not find: {}".format(sw), type="software")
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
        return render_template('404.html', content="Could not find: {}".format(dc), type="Data-Component")
    
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

@app.route('/api/enterprise/data-component')
def datacomponents_api_route():
    dcs = datacomponent.get_all_data_components()
    return dcs


@app.route('/car/<a>')
def car_analytic_route(a : str):
    a = a.upper()
    print(a)
    try:
        f = open('static/car/{}.json'.format(a), 'r')
        data = json.load(f)
        response = analytic.convert_from_mitre(data)
        have_contrib, have_coverage, have_impl, have_data_model, have_unit_tests, have_d3, have_platform = False, False, False, False, False, False, False
        if len(response['contributors']) > 0:
            have_contrib = True
        if len(response['coverage']) > 0:
            have_coverage = True
        if len(response['implementations']) > 0:
            have_impl = True
        if len(response['data_model_references']) > 0:
            have_data_model = True
        if len(response['unit_tests']) > 0:
            have_unit_tests = True
            print(have_unit_tests)
        if len(response['d3fend_mappings']) > 0:
            have_d3 = True
        if len(response['platforms']) > 0:
            have_platform = True
        return render_template('details.html', type='car-analytic', analytic=response,
            have_contrib=have_contrib, have_coverage=have_coverage, have_impl=have_impl, have_data_model=have_data_model,
            have_d3=have_d3, have_unit_tests=have_unit_tests, have_platform=have_platform)
    except FileNotFoundError:
            return render_template('404.html', content="Could not find: {}".format(a), type="car-analytic")

@app.route('/api/car/<a>')
def car_analytic_api_route(a : str):
    a = a.upper()
    print(a)
    try:
        f = open('static/car/{}.json'.format(a), 'r')
        data = json.load(f)
        response = analytic.convert_from_mitre(data)
        return render_template('details.html', type='car-analytic', analytic=response)
    except FileNotFoundError:
            return "404"

@app.route('/car')
def car_analytics_route():
    analytics = analytic.get_all_analytics()
    return render_template('table.html', type='car-analytic', analytics=analytics)

@app.route('/api/car')
def car_analytics_api_route():
    analytics = analytic.get_all_analytics()
    return analytics

@app.route('/enterprise/tactics/<t>')
def tactic_route(t : str):
    try:
        f = open('static/enterprise/tactics/{}.json'.format(t), 'r')
        data = json.load(f)
        print(data)
        response = tactic.convert_from_mitre(data, t)
        return render_template('details.html', type='tactic', t=response)
    except FileNotFoundError:
        return render_template('404.html', content="Could not find: {}".format(t), type="tactics")
    
@app.route('/api/enterprise/tactics/<t>')
def tactic_api_route(t : str):
    try:
            f = open('static/enterprise/tactics/{}.json'.format(t), 'r')
            data = json.load(f)
            response = tactic.convert_from_mitre(data)
            return response
    except FileNotFoundError:
            return "404"

@app.route('/enterprise/tactics')
def tactics_route():
    tactics = tactic.get_all_tactics()
    return render_template('table.html', type='tactic', tactics=tactics)

@app.route('/api/enterprise/tactics')
def tactics_api_route():
    tactics = tactic.get_all_tactics()
    return tactics


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
            'field' : 'tactics',
            'count' : tactic.get_count(),
            'description' : 'Common tactics used by APTs'
        },
        {
            'field' : 'data-component',
            'count' : datacomponent.get_count(),
            'description' : 'Data-Components of adversarial behavior'
        },
        {
            'field' : 'car',
            'count' : analytic.get_count(),
            'description' : 'MITRE analytics mapped to techniques'
        }
    ]
    return render_template('table.html', type='enterprise', e_list=e_list)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)