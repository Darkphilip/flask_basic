import pymongo

mongo_host = 'localhost'
mongo_conn = pymongo.MongoClient('mongodb://%s' %(mongo_host))

def conn_mongodb():
  try:
    mongo_conn.admin.command('ismaster')
    blog_ab = mongo_conn.blog_session_db.blog_ab
  except:
    mongo_conn = pymongo.MongoClient('mongodb://%s' %(mongo_host))
  return blog_ab