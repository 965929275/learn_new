#encoding:utf8
from flask import Flask,jsonify,abort,make_response,request,url_for
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

app = Flask(__name__)

tasks = [
    {
        'id':1,
        'title':u'Buy groceries',
        'description':u'Milk,Chess,Pizza,Fruit,Tylenol',
        'done':False
    },
    {
        'id':2,
        'title':u'Learn Python',
        'description':u'Need to find a good Python tutorial on the web',
        'done':False
    }
]


@auth.get_password            #回调函数
def get_password(username):   #验证用户名和密码
    if username == 'miguel':  #用户名
        return 'python'       #密码
    return None

@auth.error_handler           #给客户端发送未授权错误代码
def unauthorized():
    return make_response(jsonify({'error':'Unauthorized access'}),403)


def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['url'] = url_for('get_task',task_id=task['id'],_external=True)
        else:
            new_task[field] = task[field]
    return new_task

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': map(make_public_task,tasks)})

@app.route('/todo/api/v1.0/tasks/<int:task_id>',methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id,tasks)
    print(task)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }

    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>',methods=['PUT'])
def uodate_task(task_id):
    task = filter(lambda t: t['id'] == task_id,tasks)
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title',task[0]['title'])
    task[0]['description'] = request.json.get('description',task[0]['description'])
    task[0]['done'] = request.json.get('done',task[0]['done'])
    return jsonify({'task':task[0]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>',methods=['DELETE'])
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id,tasks)
    if len(task) == 0:
        abort(404)
        tasks.remove(task[0])
        return jsonify({'result':True})




if __name__ == '__main__':
    app.run(debug=True)
