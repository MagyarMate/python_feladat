#  Copyright (c) 2021. Mate Magyar

from typing import List, Tuple

import pytest

from route_planner import Attraction, Route, route_planner, RangeErrorException, attraction_list_factory


@pytest.fixture
def test_attraction_list_a() -> List[Attraction]:
    return [
        Attraction(0, 0, 0),
        Attraction(-2, 1, 50),
        Attraction(2, -3, 150),
        Attraction(4, 0, 200),
        Attraction(4, 4, 250),
        Attraction(6, 7, 300),
        Attraction(-4, 8, 300),
        Attraction(3, 3, 400),
        Attraction(10, 10, 450),
        Attraction(-10, -10, 500),
    ]


@pytest.fixture
def test_starting_point_a() -> Tuple[int, int]:
    return 4, 5


@pytest.fixture
def test_starting_point_b() -> Tuple[int, int]:
    return -2, 0


def test_route_planner_1(test_starting_point_a, test_attraction_list_a):
    route_a: Route = route_planner(test_attraction_list_a, test_starting_point_a)
    assert str(route_a) == '(x:4, y:4, z:250)->(x:3, y:3, z:400)->(x:6, y:7, z:300)->(x:4, y:0, z:200)'
    assert route_a.distance() == 4


def test_route_planner_1_8km(test_starting_point_a, test_attraction_list_a):
    route_a: Route = route_planner(test_attraction_list_a, test_starting_point_a, 8)
    assert str(route_a) == '(x:4, y:4, z:250)->(x:3, y:3, z:400)->(x:6, y:7, z:300)->' \
                           '(x:4, y:0, z:200)->(x:0, y:0, z:0)->(x:-2, y:1, z:50)->(x:10, y:10, z:450)'
    assert pytest.approx(route_a.distance(), 0.01) == 8.48


def test_route_planner_1_8km_height300(test_starting_point_a, test_attraction_list_a):
    route_a: Route = route_planner(test_attraction_list_a, test_starting_point_a, 8).filter(300)
    assert str(route_a) == '(x:4, y:4, z:250)->(x:6, y:7, z:300)->(x:4, y:0, z:200)->(x:0, y:0, z:0)->(x:-2, y:1, z:50)'
    assert pytest.approx(route_a.distance(), 0.01) == 6.70


def test_route_planner_1_2_concat(test_starting_point_a, test_starting_point_b, test_attraction_list_a):
    route_a: Route = route_planner(test_attraction_list_a, test_starting_point_a)
    route_b: Route = route_planner(test_attraction_list_a, test_starting_point_b)
    assert str(route_a.concatenate(route_b)) == '(x:4, y:4, z:250)->(x:3, y:3, z:400)->(x:6, y:7, z:300)->' \
                                                '(x:4, y:0, z:200)->(x:-2, y:1, z:50)->(x:0, y:0, z:0)->' \
                                                '(x:2, y:-3, z:150)'
    assert str(route_b.concatenate(route_a)) == '(x:-2, y:1, z:50)->(x:0, y:0, z:0)->(x:2, y:-3, z:150)->' \
                                                '(x:4, y:4, z:250)->(x:3, y:3, z:400)->(x:6, y:7, z:300)->' \
                                                '(x:4, y:0, z:200)'


def test_route_planner_1_2_concat_repeating(test_starting_point_a, test_starting_point_b, test_attraction_list_a):
    route_a: Route = route_planner(test_attraction_list_a, test_starting_point_a)
    route_b: Route = route_planner(test_attraction_list_a, test_starting_point_b, 7)
    assert str(route_a.concatenate(route_b)) == '(x:4, y:4, z:250)->(x:3, y:3, z:400)->(x:6, y:7, z:300)->' \
                                                '(x:4, y:0, z:200)->(x:-2, y:1, z:50)->(x:0, y:0, z:0)->' \
                                                '(x:2, y:-3, z:150)'
    assert str(route_b.concatenate(route_a)) == '(x:-2, y:1, z:50)->(x:0, y:0, z:0)->(x:2, y:-3, z:150)->' \
                                                '(x:3, y:3, z:400)->(x:4, y:0, z:200)->(x:4, y:4, z:250)->' \
                                                '(x:6, y:7, z:300)'


def test_coordinates_lower_boundary_attraction_x():
    test_attraction = Attraction(-10, 0, 0)
    assert test_attraction.coordinates == (-10, 0)


def test_coordinates_lower_boundary_attraction_x_exception():
    with pytest.raises(RangeErrorException, match='Value of x:-11'):
        test_attraction = Attraction(-11, 0, 0)


def test_coordinates_upper_boundary_attraction_x():
    test_attraction = Attraction(10, 0, 0)
    assert test_attraction.coordinates == (10, 0)


def test_coordinates_upper_boundary_attraction_x_exception():
    with pytest.raises(RangeErrorException, match='Value of x:11'):
        test_attraction = Attraction(11, 0, 0)


def test_coordinates_lower_boundary_attraction_y():
    test_attraction = Attraction(0, -10, 0)
    assert test_attraction.coordinates == (0, -10)


def test_coordinates_lower_boundary_attraction_y_exception():
    with pytest.raises(RangeErrorException, match='Value of y:-11'):
        test_attraction = Attraction(0, -11, 0)


def test_coordinates_upper_boundary_attraction_y():
    test_attraction = Attraction(0, 10, 0)
    assert test_attraction.coordinates == (0, 10)


def test_coordinates_upper_boundary_attraction_y_exception():
    with pytest.raises(RangeErrorException, match='Value of y:11'):
        test_attraction = Attraction(0, 11, 0)


def test_height_lower_boundary_attraction_z():
    test_attraction = Attraction(0, 0, 0)
    assert test_attraction.height == 0


def test_height_lower_boundary_attraction_z_exception():
    with pytest.raises(RangeErrorException, match='Value of z:-1'):
        test_attraction = Attraction(0, 0, -1)


def test_height_upper_boundary_attraction_z():
    test_attraction = Attraction(0, 0, 1000)
    assert test_attraction.height == 1000


def test_height_upper_boundary_attraction_z_exception():
    with pytest.raises(RangeErrorException, match='Value of z:1001'):
        test_attraction = Attraction(0, 0, 1001)


def test_attraction_string():
    test_attraction = Attraction(4, 5, 745)
    assert str(test_attraction) == '(x:4, y:5, z:745)'


def test_attraction_representation():
    test_attraction = Attraction(4, 5, 745)
    assert repr(test_attraction) == '(4, 5, 745)'


def test_attraction_list_factory_size1():
    attraction_list = attraction_list_factory()
    assert len(attraction_list) == 50


def test_attraction_list_factory_size2():
    attraction_list = attraction_list_factory(100)
    assert len(attraction_list) == 100
