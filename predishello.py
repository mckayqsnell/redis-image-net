import redis
import settings
import time


# Establish a connection to the Redis database at settings.REDIS_DB

host = settings.REDIS_HOST
port = settings.REDIS_PORT
password = settings.REDIS_PASSWORD

r = redis.Redis(host=host, port=port, password=password, db=settings.REDIS_DB)


# SET hello world

r.set('hello', 'world') # True


# GET hello

world = r.get('hello')

print(world.decode()) # "world"




# SET bye "In 60 seconds, I'll self-delete" EX 60

r.set('bye', "In 60 seconds, I'll self-delete", ex=60) # True

expiring_message = r.get('bye')

print(expiring_message.decode()) # "In 60 seconds, I'll self-delete"


# Wait 60 seconds

time.sleep(60)


# GET bye

expired_message = r.get('bye')

if expired_message == None:

    print('key "bye" is not there anymore.')

else:

    print(expired_message.decode()) # "None"







# DEL hello

r.delete('hello')

ans = r.get('hello')

if ans == None:

    print('key "hello" is not there anymore.')

else:

    print(ans.decode()) # "None"