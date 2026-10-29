"""Tests designed to exercise every executable line in museum_admission.py."""
import pytest
from museum_admission import ticket_price, group_discount, gallery_entry


def test_ticket_price_unknown_category():
    with pytest.raises(ValueError, match="unknown category"):
        ticket_price("tourist", 30, "tuesday", False)


def test_ticket_price_negative_age():
    with pytest.raises(ValueError, match="invalid age"):
        ticket_price("adult", -1, "tuesday", False)


def test_ticket_price_under_five_is_free():
    assert ticket_price("child", 4, "sunday", True) == 0


@pytest.mark.parametrize("category,age,day,tour,expected", [
    ("adult", 30, "tuesday", False, 300),
    ("student", 20, "monday", False, 75),
    ("child", 8, "saturday", False, 150),
    ("senior", 70, "sunday", False, 250),
    ("student", 20, "tuesday", True, 200),
    ("adult", 30, "tuesday", True, 400),
    ("adult", 30, "monday", True, 250),
    ("senior", 70, "saturday", True, 350),
    ("adult", 30, "tuesday", False, 300),
])
def test_ticket_price_valid_scenarios(category, age, day, tour, expected):
    assert ticket_price(category, age, day, tour) == expected


def test_group_discount_invalid_size():
    with pytest.raises(ValueError, match="invalid group size"):
        group_discount(0, False)


@pytest.mark.parametrize("size,is_school,expected", [
    (20, True, 40),
    (19, True, 25),
    (15, False, 20),
    (8, False, 10),
    (7, False, 0),
])
def test_group_discount_scenarios(size, is_school, expected):
    assert group_discount(size, is_school) == expected


@pytest.mark.parametrize("inside,capacity,timed,expected", [
    (10, 10, False, "wait"),
    (9, 10, False, "queue"),
    (9, 10, True, "enter"),
    (8, 10, False, "enter"),
])
def test_gallery_entry_scenarios(inside, capacity, timed, expected):
    assert gallery_entry(inside, capacity, timed) == expected
