from src.teste import Teste
from src.connection import Connection
import datetime
import configparser


#teste = Teste(10,20)

#print(teste.soma())

cfg =configparser.ConfigParser()
cfg.read('config.ini')

url= cfg.get('development','url')
port = cfg.getint('development','port')
bd = cfg.get('development','bd')

print(url + ' ' + str(port))

c = Connection(url,port,bd)

db = c.getDB()

json = {'nome':'teste',
        'date':datetime.datetime.now()}

db.tickets.replace_one({'nome':'teste'},json, True)
