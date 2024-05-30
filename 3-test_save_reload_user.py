#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_obj = storage.all()
print("-- Reloading obj ---")
for obj_id in all_obj.keys():
    obj = all_obj[obj_id]
    print(obj)

print("Creating New user 1")
my_user = User()
my_user.firstname = "Olayode"
my_user.lastname = "Yusuf"
my_user.email = "yusclever9@gmail.com"
my_user.password = "root"
my_user.save()
print(my_user)
