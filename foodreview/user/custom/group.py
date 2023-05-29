from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from restaurant.models import Restaurant
from enum import StrEnum,auto
from django.db import models
from django.db.utils import IntegrityError

from typing import List

class Perm(StrEnum):
    ADD = auto()
    DELETE = auto()
    CHANGE = auto()
    VIEW = auto()

class Restaurant_owner_group:
    NAME='restaurant_owner'
    MODEL = Restaurant
    PERMISSION = [Perm.ADD,Perm.DELETE,Perm.CHANGE,Perm.VIEW]
    
    @classmethod
    def dict(cls):
        return {
        'name':cls.NAME,
        'model' : cls.MODEL,
        'permission' : cls.PERMISSION
    }
    @classmethod
    def group(cls):
        return Group.objects.get(name = cls.NAME)
groups = [
    Restaurant_owner_group.dict()
    
]

def instantiate_groups():
    for group in groups:
        create_group(**group)


def create_group(name:str,model:models.Model,permission:List[str]):
    try:
        gr =  Group.objects.create(name = name)
        ct = ContentType.objects.get_for_model(model)
        for _ in permission:
            _ = _permission(_,ct)
            perm_to_gr(_,gr)
    except IntegrityError:
        pass

def _permission(name:str,ct:ContentType):
    return Permission.objects.create(codename=f'can_{name}',
                                   name=name,
                                   content_type=ct)

def perm_to_gr(perm:Permission,gr:Group):
    gr.permissions.add(perm)

def get_group(name):
    return Group.objects.get(name=name)


