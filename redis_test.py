import redis
import pickle

r = redis.Redis("localhost")        # en windows atento al localhost, tienes que descargarte el archivo .msi
r.set("name", "javi")
name = r.get("name")
if not r.get("apellido"):
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
user4 = {}
user2 = {"Name": {"nombre": "Javi", "apellido": "blasc"}, "Company": "Cepsa", "Address": "Mad", "Location": "Madrid"}
user3 = {"Name2": {"nombre": "Pedro", "apellido": "piqueras"}, "Company": "Cepsa", "Address": "Mad", "Location": "Madrid"}

# r.hmset("pythonDict", user2)                # almacena el diccionario
user4.update(user3)
user4.update(user2)
p_mydict = pickle.dumps(user4)
r.set('mydict', p_mydict)
r.hmset("NumberVsString", {"1": {"eng":{"One",2}, "esp":"Uno"}, "3":"tres"})
second_level = r.hget("NumberVsString", "3").decode("utf-8")
print(second_level)
r.hmset("NumberVsString", {"2": {"eng":"Two", "esp":"Dos"}})
second_level = r.hget("NumberVsString", "2").decode("utf-8")
print(second_level)
print(r.hget("NumberVsString", "1").decode("utf-8"))
read_dict = r.get('mydict')
yourdict = pickle.loads(read_dict)
print(yourdict)
# r.delete("pythonDict", "Address")             # elimina la key y su valor
# print(r.get("pythonDict"))              # te devuelve el diccionario entero
# print(r.exists("pythonDict", "Name"))      # te devuelve un true si existe
# val = r.("pythonDict")                 # [b'Name', b'Company', b'Location'] lista de las keys
# print(val[1])                               # b'Company'

