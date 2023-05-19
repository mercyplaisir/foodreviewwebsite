from enum import Enum, StrEnum,auto
from typing import List

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model
from django.db.utils import IntegrityError
groups = ['restaurant_owner','simple_user']


class Perm(StrEnum):
    CHANGE = auto()
    DELETE = auto()
    VIEW = auto()
    ADD = auto()
def get_group(name):
    gr = Group.objects.get(name=name)
    return gr
def group_exist(name):
    if Group.objects.count()<1:
        return False
    return Group.objects.filter(name = name).exists()
def create_group(name,model:Model,perm:List[Perm]):
    if group_exist(name):
        return get_group(name)
    gr  = Group.objects.create(name=name)
    ct = ContentType.objects.get_for_model(model)
    for permission in perm:
        p = _create_permission(permission,ct,model)
        _add_permission(gr,p)
    print(f'{gr} created')
    return gr
def _create_permission(perm:Perm,ct:ContentType,model:Model):
        
    return Permission.objects.create(codename=f'{perm.value}_{model.__name__}',
                                name=f'{perm.value} {model.__name__}',
                                content_type=ct)
def _add_permission(gr:Group,perm:Permission):
    gr.permissions.add(perm)       

