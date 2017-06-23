import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds127962.mlab.com:27962/noreplicable

host = "ds127962.mlab.com"
port = 27962
db_name = "noreplicable"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())