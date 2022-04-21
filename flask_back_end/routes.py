#!/usr/bin/env python

from global_vars import get_app, get_mongo
#from run import mongo
app = get_app()
mongo = get_mongo()

import datetime
#from datetime import datetime, timedelta

import os
import zipfile

from bson import ObjectId
from flask import Flask, render_template, send_from_directory
from flask import request
from flask_pymongo import PyMongo, DESCENDING
from flask import jsonify
from flask import make_response

#import flask_uploads
from werkzeug.utils import secure_filename
import jwt

from functools import wraps


#////////////////////////////////////////////////////////////// HELPERS //////////////////////////////////////////////////////////////////////////////////////////////////
def get_human_readable_file_size(file_path):
    size_in_bytes = 0
    #check below  is necessary, get size returns size of a dir if file_path points to a dir
    if os.path.isfile(file_path):        
        size_in_bytes = os.path.getsize(file_path)
    
    if size_in_bytes // (1024*1024*1024) > 0 :
        return str(size_in_bytes // (1024*1024*1024)) + " Gb"
    elif size_in_bytes // (1024*1024) > 0:
        return str(size_in_bytes // (1024*1024)) + " Mb"
    elif  size_in_bytes // (1024) > 0:
        return str(size_in_bytes // (1024)) + " Kb"
    
    return str(size_in_bytes ) + " bytes"



def get_app_root_dir():
    return './uploads'


def ensure_dir_exists(dir):
   if not os.path.isdir( dir ):
        os.mkdir( dir )


def get_project_from_run(run_id):
    run = mongo.db.runs.find_one({'_id': ObjectId(run_id)})
    if run is not None:
        project_id = str(run['project_id'])
        return project_id
    else:
        return None


# stores file in a folder corresponding to given run_id
def store_file(file, run_id):
    #find project for this run
    run = mongo.db.runs.find_one({'_id': ObjectId(run_id)})
    if run is not None:
        project_id = str(run['project_id'])
    
        # if dir for this run does not exist - create dir;
        # after that store file in a dir corresponding to this run

        run_dir_path = os.path.join(get_app_root_dir(), 'Projects', project_id, 'Runs', run_id)
        #TODO: vai seit ir jabut ensure dir exists izsaukumam ?
        ensure_dir_exists( run_dir_path )
        file.save(os.path.join( run_dir_path, secure_filename(file.filename)))



def get_gold_label_map(project_id):
    #print("gold label map1")
    if not os.path.isdir(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Train')):
        return {}
    #print("gold label map2")
    # r=root, d=directories, f = files
    labels_file_path = ""
    for r, d, f in os.walk(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Train')):
        for file in f:
            #print("fname " + file)
            if os.path.isfile(os.path.join(r, file)) and file == "labels.txt":
                labels_file_path = os.path.join(r, file)
    #print("lbfp " + labels_file_path)
    if labels_file_path == "":
        return {}
    #print("gold label map3")
    #print(labels_file_path)
    labels_2_list_of_files = {}
    with open(labels_file_path, "r") as f:
        for line in f:
            parts = line.strip().split(',', 2)
            if len(parts) == 2:
                fname = parts[0].strip()
                label = parts[1].strip()
                if not label in labels_2_list_of_files:
                    labels_2_list_of_files[label] = []
                labels_2_list_of_files[label].append(fname)
    #print("gold label map ")
    return labels_2_list_of_files


def get_gold_label_map_for_test_data(project_id):
    #print("gold label map1")
    if not os.path.isdir(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Test')):
        return {}
    #print("gold label map2")
    # r=root, d=directories, f = files
    labels_file_path = ""
    for r, d, f in os.walk(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Test')):
        for file in f:
            #print("fname " + file)
            if os.path.isfile(os.path.join(r, file)) and file == "labels.txt":
                labels_file_path = os.path.join(r, file)
    #print("lbfp " + labels_file_path)
    if labels_file_path == "":
        return {}
    #print("gold label map3")
    #print(labels_file_path)
    labels_2_list_of_files = {}
    with open(labels_file_path, "r") as f:
        for line in f:
            parts = line.strip().split(',', 2)
            if len(parts) == 2:
                fname = parts[0].strip()
                label = parts[1].strip()
                if not label in labels_2_list_of_files:
                    labels_2_list_of_files[label] = []
                labels_2_list_of_files[label].append(fname)
    #print("gold label map ")
    return labels_2_list_of_files


def get_silver_label_map_for_test_data(project_id, run_id):
    #print("gold label map1")
    if not os.path.isdir(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Runs', run_id)):
        return None, None
    #print("gold label map2")
    # r=root, d=directories, f = files
    labels_file_path = ""
    for r, d, f in os.walk(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Runs', run_id)):
        for file in f:
            #print("fname " + file)
            if os.path.isfile(os.path.join(r, file)) and file == "labels.txt":
                labels_file_path = os.path.join(r, file)
    #print("lbfp " + labels_file_path)
    if labels_file_path == "":
        return None, None
    #print("gold label map3")
    #print(labels_file_path)
    labels_2_list_of_files = {}
    file_2_label = {}
    with open(labels_file_path, "r") as f:
        for line in f:
            parts = line.strip().split(',', 2)
            if len(parts) == 2:
                fname = parts[0].strip()
                label = parts[1].strip()

                file_2_label[fname] = label
                
                if not label in labels_2_list_of_files:
                    labels_2_list_of_files[label] = []
                labels_2_list_of_files[label].append(fname)
    #print("gold label map ")
    return labels_2_list_of_files, file_2_label


#TODO: rename to get_gold_labels from test-data
def get_gold_labels(project_id):
    # get first dir in os.path.join('./uploads', project_id, 'unzipped_data')
    # from that dir get file labels.txt


    if not os.path.isdir(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Test')):
        return {}

    first_dir = None
    for dirn in os.listdir(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Test')):
        print(dirn)
        if os.path.isdir(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Test', dirn)):
            first_dir = dirn
            break
    # print(first_dir)

    file_name2label = {}
    if first_dir is not None:
        label_file_path = os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Test', first_dir, "labels.txt")
        if os.path.isfile(label_file_path):
            with open(label_file_path, "r") as f:
                for line in f:
                    parts = line.strip().split(',', 2)
                    if len(parts) == 2:
                        file_name2label[parts[0]]=parts[1]

    print(file_name2label)
    return file_name2label


def get_silver_labels(project_id, run_id):
    
    label_file_path = os.path.join(get_app_root_dir(), 'Projects', project_id, 'Runs', run_id, 'silver_labels.txt' )
    res = {}
    if os.path.isfile(label_file_path):
        with open(label_file_path, "r") as f:
            for line in f:
                parts = line.strip().split(',', 2)
                if len(parts) == 2:
                    res[parts[0]] = parts[1]
    return res


#////////////////////////////////////////////////////////////// END OF HELPERS //////////////////////////////////////////////////////////////////////////////////////////////////



#////////////////////////////////////////////////////////////// ROUTES //////////////////////////////////////////////////////////////////////////////////////////////////


def require_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token is missing.'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message':'Token is invalid'}), 403

        return f(*args, **kwargs)

    return decorated


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')


@app.route('/start_run/<string:name>')
@require_token
def start_run(name):
    print("Recieved request from " + str(request.remote_addr) )
    #find proj by name
    proj = mongo.db.projects.find_one({'name': name})
    # create run tied to this proj
    if proj is not None:
        proj_id = proj['_id']
        
        comment = ""
        if 'comment' in request.args:
            comment = request.args.get('comment')
        
        git_commit_url = ""
        if 'git_commit_url' in request.args:
            git_commit_url = request.args.get('git_commit_url')
        
        run = mongo.db.runs.insert_one({'project_id': proj_id,
                                        'comment' : comment,
                                        'start_time': datetime.datetime.now(),
                                        'git_commit_url':git_commit_url,
                                        'remote_address' : request.remote_addr
                                        })
        run_id = run.inserted_id
        
        ensure_dir_exists( os.path.join(get_app_root_dir(), 'Projects', str(proj_id), 'Runs', str(run_id)) )

        return jsonify({'id': str(run_id)})
    else:
        print(name)
        #return jsonify({'err': 'project named not found.'})
        return jsonify({'err': 'Project named \'' + name + '\' not found.'}), 404


@app.route('/finish_run')
@require_token
def finish_run():
    run_id = request.args.get('run_id')
    if run_id is not None:
        run = mongo.db.runs.find_one({'_id': ObjectId(run_id)})
        if run is not None:

            x = mongo.db.runs.update_one({'_id': ObjectId(run_id)},
                                         {"$set": {"finished": True, 'finish_time': datetime.datetime.now()}}
                                         )

            return 'ok'
        else:
            return jsonify({'err': 'Run with id \'' + request.args['run_id'] + '\' not found.'}), 404
    else:
        #print(run_id)
        #return jsonify({'err': 'project named not found.'})
        return jsonify({'err': 'Malformed request. Param run_id must be present.'}), 404


@app.route('/log')
@require_token
def log():
    #check we have 2 args run_id and msg
    if 'run_id' in request.args and 'msg' in request.args:
        #check that run with id = run_id is present and is not finished
        run = mongo.db.runs.find_one({'_id': ObjectId(request.args['run_id'])})
        if run is None:
            return jsonify({'err': 'Run with id \'' + request.args['run_id'] + '\' not found.'}), 404
        elif 'finished' in run and run['finished']:
            return jsonify({'err': 'Run with id \'' + request.args['run_id'] + '\' has been finished.'}), 403
        else:
            role_name = ""
            if 'role_name' in request.args :
                role_name = request.args['role_name']

            # insert log message in to the given run
            mongo.db.logs.insert_one(
                {'run_id': request.args['run_id'], 
                 'msg': request.args['msg'],
                 'logged_on': datetime.datetime.utcnow(),
                 'role_name' : role_name
                }
            )

            print("logging msg " + request.args['msg'])
            return 'ok'
    else:
        return jsonify({'err': 'Malformed request. Params run_id and msg must be present.'}), 404


@app.route('/get_logs')
def view_logs():
    output = []
    logs = None
    if 'project_id' in request.args:
        logs = mongo.db.logs.find({'project_id': request.args['project_id']})
    else:
        logs = mongo.db.logs

    for l in logs:
        role_name = ""
        if 'role_name' in l:
            role_name = l['role_name']
        
        output.append({'id': str(l['_id']), 'msg': l['msg'], 'role_name': role_name})
    print(output)

    response = jsonify({'res': output})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_projects')
def get_projects():

    #print(request.args)
    output = []
    projects = None
    if 'user_id' in request.args:
        projects = mongo.db.projects.find({'user_id': request.args['user_id']})
    else:
        projects = mongo.db.projects.find()

    for curr_proj in projects:
        num_of_runs = mongo.db.runs.find({'project_id' : ObjectId(curr_proj['_id'])}).count()
        last_updated = "0:00"
        if num_of_runs > 0:
            #pedeja uzsakta run`a sakumlaiks
            last_run = mongo.db.runs.find({'project_id' : ObjectId(curr_proj['_id'])}).sort('start_time', DESCENDING).limit(1)
            last_updated = last_run[0]['start_time'] 
        else:
            if 'created_at' in curr_proj:
                last_updated = curr_proj['created_at']
                
        output.append({
            'id': str(curr_proj['_id']), 
            'name': curr_proj['name'],
            'last_update_time': last_updated,
            'num_of_runs' : num_of_runs,
            'owner_id' : str(curr_proj['user_id'])
            })

    #print(output)

    response = jsonify({'projects': output})
    #https://stackoverflow.com/questions/26980713/solve-cross-origin-resource-sharing-with-flask
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#TODO: get_runs drizak ir view project details, butu labak parsaukt gan seit, gan js puse

@app.route('/get_runs/<string:project_id>')
def get_runs(project_id):
    output = []
    runs = mongo.db.runs.find({'project_id': ObjectId(project_id)})

    #TODO : add field  user_id present in table header, but not being filled in runs table

    for run in runs:
        comment = ""
        if 'comment' in run:
            comment = run['comment']
        
        git_commit_url = ""
        git_commit_url_shortened = ""
        if 'git_commit_url' in run:
            git_commit_url = run['git_commit_url']
            if len(git_commit_url) > 10 :
                git_commit_url_shortened = git_commit_url[ len(git_commit_url) - 10 :]
            else:
                git_commit_url_shortened = git_commit_url

        remote_address = ""
        if 'remote_address' in run:
            remote_address = run['remote_address']


        output.append({'id': str(run['_id']),
                       'start_time': run['start_time'],
                       'finish_time': run['finish_time'] if 'finish_time' in run else "",
                       'comment': comment,
                       'git_commit_url' : git_commit_url,
                       'git_commit_url_shortened' : git_commit_url_shortened,
                       'remote_address' : remote_address
                       })

    #print(output)

    training_data_file_path = ""
    for fpath in os.listdir(os.path.join(get_app_root_dir(),'Projects', project_id, 'Data', 'Train')):
        print(fpath)
        if os.path.isfile(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Data', 'Train', fpath)) and os.path.splitext(fpath)[1] == ".zip":
            training_data_file_path = fpath
            break

    testing_data_file_path = ""
    for fpath in os.listdir(os.path.join(get_app_root_dir(),'Projects', project_id, 'Data', 'Test')):
        print(fpath)
        if os.path.isfile(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Data', 'Test', fpath)) and os.path.splitext(fpath)[1] == ".zip":
            testing_data_file_path = fpath
            break

    project =  mongo.db.projects.find_one({'_id': ObjectId(project_id)})
    proj_name = ""
    proj_descr = ""
    proj_creation_time = ""
    if project is not None:
        proj_name = project['name']
        if 'description' in project:
            proj_descr = project['description']
        if 'created_at' in project:
            proj_creation_time = project['created_at']

    response = jsonify({'runs': output,
                        'training_data_download_link': training_data_file_path,
                        'training_file_size': 
                            get_human_readable_file_size( os.path.join(get_app_root_dir(), 'Projects', project_id, 'Data', 'Train', training_data_file_path)),
                        'testing_data_download_link' : testing_data_file_path,
                        'testing_file_size': 
                            get_human_readable_file_size( os.path.join(get_app_root_dir(), 'Projects', project_id, 'Data', 'Test', testing_data_file_path)),
                        'name' : proj_name,
                        'description' : proj_descr,
                        'created_at' : proj_creation_time
                        })
    # https://stackoverflow.com/questions/26980713/solve-cross-origin-resource-sharing-with-flask
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST' and 'file' in request.files:
        filename = uploadedFiles.save(request.files['file'])
        print('a')
        print(uploadedFiles.url(filename))
        print('b')

        return "uploaded successfully by flask-uploads"


@app.route('/upload_file', methods=['POST'])
@require_token
def upload_file():
    if 'file' in request.files and 'run_id' in request.args:
        file = request.files['file']
        run_id = request.args['run_id']
        store_file(file, run_id)
        #saglabat info par failu ieks Mongo
        
        comment = ""
        if 'comment' in request.args:
            comment = request.args.get('comment')

        role_name = ""
        if 'role_name' in request.args:
            role_name = request.args.get('role_name')

        mongo.db.files.insert_one(
            {'file_name' : secure_filename(file.filename),
             'run_id' : ObjectId(run_id),
             'comment' : comment,
             'upload_time' : datetime.datetime.utcnow(),
             'role_name' : role_name
             }
        )
             
        return 'File uploaded successfully'
    return 'Malformed request. No \'file\' found.'


@app.route('/upload_training_data', methods=['POST'])
def upload_training_data():
    project_id = request.form.get('project_id')
    print("upload training data ... ")
    print(project_id)
    print(request)

    if 'zip_file' in request.files and project_id is not None:
        f = request.files['zip_file']

        if not os.path.isdir(os.path.join(get_app_root_dir(), 'Projects', project_id)):
            return 'Project dir does not exist'
        else:
            ensure_dir_exists(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Data', 'Train'))
            ensure_dir_exists(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Train'))
            zip_file_path = os.path.join(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Data', 'Train', secure_filename(f.filename)))
            f.save(zip_file_path)

            with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                zip_ref.extractall(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Train'))

        response = jsonify({'msg':'file uploaded successfully'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    return 'Malformed request. Params \'zip_file\' and \'project_id\' must be present. ', 400


@app.route('/upload_testing_data', methods=['POST'])
def upload_testing_data():
    # project_id = request.args.get('project_id')
    # print(project_id)
    # print(request)
    # print(request.args)
    # print(request.args.get('project_id'))
    # print(request.form)
    # print(request.form.get('project_id'))
    # print(request.files)
    # request.form.keys()
    project_id = request.form.get('project_id')
    if 'zip_file' in request.files and project_id is not None:
        f = request.files['zip_file']

        if not os.path.isdir(os.path.join(get_app_root_dir(), 'Projects', project_id)):
            return 'Project dir does not exist'
        else:
            # ensure_dir_exists(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Data', 'Test'))
            # ensure_dir_exists(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Test'))
            zip_file_path = os.path.join(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Data', 'Test', secure_filename(f.filename)))
            f.save(zip_file_path)

            with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                zip_ref.extractall(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Test'))
        
        response = jsonify({'msg':'file uploaded successfully'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    return 'Malformed request. Params \'zip_file\' and \'project_id\' must be present. ', 400


@app.route('/create_new_project', methods=['POST'])
def create_new_project():

    print(request)
    #print(request.raw)
    print(request.form)
    print(request.files)

    project_name = request.form.get('project_name')
    print(project_name)
    
    if project_name is not None:
        #TODO: Vai vajag parbaudit vai nebija jau eksistejis projekts ar tadu pasu vardu ?
        proj_descr = ""
        if 'project_description' in request.form:
            proj_descr = request.form.get('project_description')
        
        user_id = ""
        if 'user_id' in request.form:
            user_id = request.form.get('user_id')

        res = mongo.db.projects.insert_one( {'name': project_name, 
                                            'user_id': ObjectId(user_id), #replace to value from user
                                            'description': proj_descr,
                                            'created_at': datetime.datetime.utcnow()
                                            })
        proj_id = str(res.inserted_id)

        ensure_dir_exists( os.path.join(get_app_root_dir(), 'Projects'))	
        ensure_dir_exists( os.path.join(get_app_root_dir(), 'Projects', proj_id ))
        ensure_dir_exists( os.path.join(get_app_root_dir(), 'Projects', proj_id, 'Runs' ))

        ensure_dir_exists( os.path.join(get_app_root_dir(), 'Projects', proj_id, 'Data'))
        ensure_dir_exists( os.path.join(get_app_root_dir(), 'Projects', proj_id, 'Data', 'Train'))
        ensure_dir_exists( os.path.join(get_app_root_dir(), 'Projects', proj_id, 'Data', 'Validation'))
        ensure_dir_exists( os.path.join(get_app_root_dir(), 'Projects', proj_id, 'Data', 'Test'))
        ensure_dir_exists( os.path.join(get_app_root_dir(), 'Projects', proj_id, 'Unzipped_data'))
        ensure_dir_exists( os.path.join(get_app_root_dir(), 'Projects', proj_id, 'Unzipped_data', 'Train'))
        ensure_dir_exists( os.path.join(get_app_root_dir(), 'Projects', proj_id, 'Unzipped_data', 'Validation'))
        ensure_dir_exists( os.path.join(get_app_root_dir(), 'Projects', proj_id, 'Unzipped_data', 'Test'))
        
        #f.save(os.path.join('./uploads', 'Projects', str(res.inserted_id), 'data', secure_filename(f.filename)))

        #with zipfile.ZipFile(os.path.join('./uploads', str(res.inserted_id), 'data', secure_filename(f.filename)), "r") as zip_ref:
        #    zip_ref.extractall(os.path.join('./uploads', str(res.inserted_id), 'unzipped_data'))

        response = jsonify({'msg':'project created successfully'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    response = make_response( 
        jsonify({'msg':'Malformed request. Param \'project_name\' must be present. '}),
        400)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_file/<string:name>')
def get_file(name):
    # jasanem run id
    # jaatgriez fails ./uploads/run_id/file_name
    if 'run_id' in request.args and name is not None:
        run_id = request.args['run_id']
        proj_id = get_project_from_run(run_id)
        if proj_id is not None:
            return send_from_directory(os.path.join(get_app_root_dir(), 'Projects', proj_id, 'Runs', run_id), secure_filename(name), as_attachment=True)
        else:
            return "Project was not  found."
    return "Error. Malformed request."


@app.route('/get_training_file/<string:name>')
def get_training_file(name):
    # jasanem run id
    # jaatgriez fails ./uploads/project_id/file_name
    project_id = request.args['project_id']
    first_dir = None
    for dirn in os.listdir(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Train')):
        print(dirn)
        if os.path.isdir(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Train', dirn)):
            first_dir = dirn
            break
    # print(first_dir)
    return send_from_directory(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Train', first_dir ), secure_filename(name), as_attachment=True)


@app.route('/get_training_set/')
def get_training_set():
    file_name = request.args['file_name']
    project_id = request.args['project_id']
    return send_from_directory(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Data', 'Train'), secure_filename(file_name),
                               as_attachment=True)
    #return send_from_directory(os.path.join('./uploads', project_id, 'data'), secure_filename(file_name), as_attachment=True)
    # return 'ok'
    #return send_from_directory(os.path.join('./uploads', '5cec892a5d70c46e9de0cf3f', 'data'), 'training_data.zip', as_attachment=True)


@app.route('/get_testing_set/')
def get_testing_set():
    file_name = request.args['file_name']
    project_id = request.args['project_id']
    return send_from_directory(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Data', 'Test'), secure_filename(file_name),
                               as_attachment=True)
    #return send_from_directory(os.path.join('./uploads', project_id, 'data'), secure_filename(file_name), as_attachment=True)
    # return 'ok'
    #return send_from_directory(os.path.join('./uploads', '5cec892a5d70c46e9de0cf3f', 'data'), 'training_data.zip', as_attachment=True)


@app.route('/get_run/<string:run_id>')
def get_run(run_id):
    # find run by id
    run = mongo.db.runs.find_one({'_id': ObjectId(run_id)})
    if run is not None:
        # collect logs for this run
        logs = mongo.db.logs.find({'run_id': run_id})
        logs_output = []
        for l in logs:
          logged_on = "0:00"
          if 'logged_on' in l:
            logged_on = l['logged_on']

          role_name = ""
          if 'role_name' in l:
            role_name = l['role_name']
                
          logs_output.append(
              { 
                  'id': str(l['_id']),
                  'msg': l['msg'],
                  'logged_on': logged_on,
                  'role_name': role_name
              }
          )
        print(logs_output)

        # collect files uploaded during this run
        proj_id = str(run['project_id'])
        files_on_disk = []
        run_path = os.path.join(get_app_root_dir(), 'Projects', proj_id, 'Runs', run_id )
        if os.path.exists( run_path ):
            for f in os.listdir( run_path ):
                if os.path.isfile(os.path.join(run_path, f)):
                    files_on_disk.append(f)

        #[{'file_name':'a.txt', 'comment' : 'a', 'upload_time':''}]
        files_in_Mongo = mongo.db.files.find({'run_id' : ObjectId(run_id)})
        files_extended = []
        for mongo_file in files_in_Mongo:
           if mongo_file['file_name'] in files_on_disk:
                role_name = ""
                if 'role_name' in mongo_file:
                    role_name = mongo_file['role_name']
                                
                files_extended.append( 
                    { 'file_name': mongo_file['file_name'], 
                      'comment' : mongo_file['comment'], 
                      'upload_time': mongo_file['upload_time'],
                      'role_name' : role_name
                    }
                )


        # collect this project files
        #file_list = []
        #for f in os.listdir(os.path.join('./uploads', run_id,)):
        #    if os.path.isfile(os.path.join('./uploads', run_id, f)):
        #        file_list.append(f)

        gold_labels = get_gold_labels(str(run['project_id']))
        silver_labels = get_silver_labels(str(run['project_id']), run_id)

        print("gold")
        print(gold_labels)
        print("silver")
        print(silver_labels)

        res = []
        for k in gold_labels:
            res.append((k, gold_labels[k], silver_labels.get(k)))
        print(res)

        response = jsonify({'run': {'start_time': run['start_time'],
                                    'finish_time': run['finish_time'] if 'finish_time' in run else "",
                                    'logs': logs_output,
                                    #'files': files_on_disk,
                                    'files' : files_extended,
                                    'gold': list(gold_labels),
                                    'silver': silver_labels,
                                    'file_gold_silver': res,
                                    'project_id': str(run['project_id']),
                                    'comment' : run['comment'],
                                    'git_commit_url': run['git_commit_url'] if 'git_commit_url' in run else ""
                                    }})
    else:
        response = "run " + run_id + " not found"

    # https://stackoverflow.com/questions/26980713/solve-cross-origin-resource-sharing-with-flask
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


#find user by user login , if found check psw 
# if found and psw ok - return user id
def get_user_id(user_login, user_psw_hash):
    if user_login is not None and user_psw_hash is not None:
        user = mongo.db.users.find_one({'login': user_login})
        if user != None:
            print(user)
            if 'password' in user and user['password'] == user_psw_hash :
                user_name = ""
                if 'name' in user :
                    user_name = user['name'] 
                return user['_id'], user_name
        else:
            print("User Not found")

    return None, None

def check_credentials(user_id, user_psw_hash):
    print( get_user_id(user_id,user_psw_hash) )
    if user_id is not None and user_psw_hash is not None:
        if user_id == 'user1' and user_psw_hash == 'psw1':
            return True
        if user_id == 'user2' and user_psw_hash == 'psw2':
            return True
        
    return False


@app.route('/login/', methods=('POST',))
def login():
    print('login')
    print( request.get_data())
    print( request.headers )
    data = request.get_json(force=True)
    print("json_data:")
    print(data)
    user_id = data['user_id']
    user_psw_hash = data['user_psw_hash']

    #if not check_credentials(user_id, user_psw_hash):
    #    return jsonify({ 'message': 'Invalid credentials', 'authenticated': False }), 401

    user_id_mongo, user_name = get_user_id(user_id, user_psw_hash)
    if  user_id_mongo == None:
        response = jsonify({ 'message': 'Invalid credentials', 'authenticated': False })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 401

    token = jwt.encode({
        'sub': user_id,
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=12)},
        app.config['SECRET_KEY'])

    response = jsonify({
            'token': token.decode('UTF-8'),
            'user_id' : str(user_id_mongo),
            'user_name' : user_name
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(response)
    print( response.get_data() )
    print( response.get_json() )
    return response 



##################################################  DATA SET VIEWER #####################################################################################################

@app.route('/get_training_data_set_size/<string:project_id>')
def get_data_set_size(project_id):
    return jsonify({"size":50})


@app.route('/get_training_data_set_chunk/<string:project_id>')
def get_training_data_set_chunk(project_id):
    print(request.args)
    fromInd = int(request.args['fromInd'])
    toInd = int(request.args['toInd'])

    data = []
    # for i in range(fromInd,toInd):
    #   data.append({"first": 'John', "last":'Doe', "suffix":"#" + str(i)})
    
    # response = make_response(jsonify({"data":data}))
    # response.headers.add('Access-Control-Allow-Origin', '*')
    

    #return a list of file form proj dir 
    
    first_dir = None
    for dirn in os.listdir(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Test')):
        print(dirn)
        if os.path.isdir(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Test', dirn)):
            first_dir = dirn
            break

    print (first_dir)

    if first_dir != None:
        for file in os.listdir(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Test', first_dir)):
            if( file.endswith(".jpg") or file.endswith(".jpeg")):
                data.append(file)

    print(data)

    response = make_response(jsonify({"data":data[fromInd:max(toInd, len(data))]}))
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response


@app.route('/get_testing_file/<string:name>')
def get_testing_file(name):
    print("gettestingfile")
    print(name)
    project_id = request.args['project_id']
    first_dir = None
    for dirn in os.listdir(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Test')):
        print(dirn)
        if os.path.isdir(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Test', dirn)):
            first_dir = dirn
            break
    # print(first_dir)
    return send_from_directory(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Test', first_dir ), secure_filename(name), as_attachment=False)

# @app.route('/get_testing_file/<string:name>')
# def get_training_file(name):
#     print("gettrainingfile")
#     print(name)
#     project_id = request.args['project_id']
#     first_dir = None
#     for dirn in os.listdir(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Train')):
#         print(dirn)
#         if os.path.isdir(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Train', dirn)):
#             first_dir = dirn
#             break
#     # print(first_dir)
#     return send_from_directory(os.path.join(get_app_root_dir(), 'Projects', project_id, 'Unzipped_data', 'Train', first_dir ), secure_filename(name), as_attachment=False)


@app.route('/get_training_data_labels/<string:project_id>')
def get_training_data_labels(project_id):
    print("get training data labels")
    labels = get_gold_label_map(project_id)
    
    response = make_response(jsonify({"data":labels}))
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

@app.route('/get_testing_data_gold_labels/<string:project_id>')
def get_testing_data_gold_labels(project_id):
    print("get training data labels")
    labels = get_gold_label_map_for_test_data(project_id)
    
    response = make_response(jsonify({"data":labels}))
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

@app.route('/get_testing_data_silver_labels/<string:project_id>')
def get_testing_data_silver_labels(project_id):
    print("get testing data silver labels")
    run_id = request.args.get('run_id')
    print(project_id)
    print(run_id)
    labels_2_list_of_files,file_2_label = get_silver_label_map_for_test_data(project_id, run_id)
    
    response = make_response(jsonify({"labels_2_list_of_files":labels_2_list_of_files, "file_2_label":file_2_label }))
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response
#//////////////////////////////////////////////////////////////END OF ROUTES//////////////////////////////////////////////////////////////////////////////////////////////////
