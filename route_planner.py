#  Copyright (c) 2021. Mate Magyar

import math
import random
from typing import List, Tuple


class RangeErrorException(Exception):
    def __init__(self, expression, message='Value is out of range'):
        self.expression = expression
        self.message = message


class Attraction(object):
    def __init__(self, x: int, y: int, z: int):
        if not -10 <= x <= 10:
            raise RangeErrorException('Value of x:{value}'.format(value=x))
        else:
            self.__x = x
        if not -10 <= y <= 10:
            raise RangeErrorException('Value of y:{value}'.format(value=y))
        else:
            self.__y = y
        if not 0 <= z <= 1000:
            raise RangeErrorException('Value of z:{value}'.format(value=z))
        else:
            self.__z = z

    @property
    def coordinates(self) -> Tuple[int, int]:
        return self.__x, self.__y

    @property
    def height(self) -> int:
        return self.__z

    def __repr__(self) -> str:
        return '({x}, {y}, {z})'.format(x=self.__x, y=self.__y, z=self.__z)

    def __str__(self) -> str:
        return '(x:{x}, y:{y}, z:{z})'.format(x=self.__x, y=self.__y, z=self.__z)


class Route(object):
    def __init__(self, point_of_interests: List[Attraction]):
        self.__point_of_interests = point_of_interests

    def concatenate(self, other_route: 'Route') -> 'Route':
        return Route(list(dict.fromkeys(self.__point_of_interests + other_route.__point_of_interests)))

    def distance(self) -> float:
        return math.dist(self.__point_of_interests[0].coordinates, self.__point_of_interests[-1].coordinates)

    def filter(self, max_height: int) -> 'Route':
        return Route([item for item in self.__point_of_interests if item.height <= max_height])

    def elevation(self) -> int:
        return max(self.__point_of_interests, key=lambda attraction: attraction.height).height - min(
            self.__point_of_interests, key=lambda attraction: attraction.height).height

    def __str__(self) -> str:
        return '->'.join([str(item) for item in self.__point_of_interests])

    def __repr__(self) -> str:
        return self.__str__()


def route_planner(attractions: List[Attraction], start_coordinates: Tuple[int, int], max_distance: int = 5) -> Route:
    attractions.sort(key=lambda attraction: math.dist(start_coordinates, attraction.coordinates))
    return Route([item for item in attractions if math.dist(item.coordinates, start_coordinates) <= max_distance])


# Helper functions


def attraction_list_factory(total_number_of_attractions: int = 50) -> List[Attraction]:
    return list([Attraction(random.randint(-10, 10), random.randint(-10, 10), random.randint(0, 1000)) for _ in
                 range(total_number_of_attractions)])
