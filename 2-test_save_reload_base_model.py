#!/usr/bin/python3

from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("--Reloaded objects--")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("--create new obj--")
my_model = BaseModel()
my_model.name = "Doctware"
my_model.age = 27
my_model.save()
print(my_model)
