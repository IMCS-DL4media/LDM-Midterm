
# logging_functions

Client side functions for working with LDM framework.


## log
```python
log(msg, role_name='')
```
Log message msg to server.

Parameters:

msg (string): Message to log

role_name (string): Role name of a message. Role name is optional and can be ommited.

Returns:

None


## start_run
```python
start_run(project_name, comment='', git_commit_url='')
```

Start a new run.

Parameters:

project_name (string): Name of a project this newly started run will belong to.

comment (string): Comment for a run.  This parameter is optional and can be ommited.

git_commit_url (string): URL of a git commit representing the state of a code base used in this run. This prm is optional and can be ommited.

Returns:

None


## finish_run
```python
finish_run()
```

Finish the current run.

Parameters:

Returns:

None



## upload_file
```python
upload_file(file_name, role_name='', comment='')
```

Upload file (file_name) to the logging server and attaches it to the current run.

Parameters:

file_name (string): File path (on a local machine) of file to be uploaded.

comment (string): Comment for a file to be uploaded.  This prm is optional and can be ommited.

role_name (string): Role name for a file to be uploaded. This prm is optional and can be ommited.


Returns:

None



## login
```python
login(user_id, psw, server_url_prm='http://localhost:5000')
```

Authorize user user_id with password psw on server server_url_prm.

Parameters:

user_id (string): User ID.

psw (string): User password.

server_url_prm (URL): URL of an instance of LDM framework to connect to. All subsequent calls to LDM framework functions will be directed to this URL. This prm is optional and can be ommited, in this case default URL of "http://localhost:5000" will be used .

Returns:

True in case of success, False otherwise.

