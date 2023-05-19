from dataclasses import dataclass,field
from enum import Enum
from typing import Protocol
from main.utils import Perm

class RestaurantModel(Protocol):
    ...


class Restaurant_owner:
    name = 'restaurant_owner'
    model = RestaurantModel
    perm = [Perm.ADD,
                Perm.CHANGE,
                Perm.DELETE,
                Perm.VIEW]
        