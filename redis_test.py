import redis

r = redis.Redis("localhost")
r.set("name", "javi")
name = r.get("name")
print(name)         # b'javi'
r.set('count', 1)    # true
r.incr('count')     # 2
r.incr('count')     # 3
r.decr('count')     # 2
# r.rpush('hispanic', 'uno')      #creamos una lista
# r.rpush('hispanic', 'dos')
# r.rpush('hispanic', 'tres')
# r.delete("hispanic")
# print(r.llen("hispanic"))
user2 = {"Name": "Javi", "Company": "Cepsa", "Address": "Mad", "Location": "Madrid"}

r.hmset("pythonDict", user2)                # almacena el diccionario
r.hdel("pythonDict", "Address")             # elimina la key y su valor
print(r.hgetall("pythonDict"))              # te devuelve el diccionario entero
print(r.hexists("pythonDict", "Name"))      # te devuelve un true si existe
val = r.hkeys("pythonDict")                 # [b'Name', b'Company', b'Location'] lista de las keys
print(val[1])                               # b'Company'

