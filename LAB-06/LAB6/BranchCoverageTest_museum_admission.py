"""Tests targeting both outcomes of each decision in museum_admission.py."""
import pytest
from museum_admission import ticket_price, group_discount, gallery_entry


@pytest.mark.parametrize("category,age,day,tour,expected", [
    ("adult", 25, "tuesday", False, 300),       # known category; age >= 0; age >= 5
    ("student", 20, "monday", False, 75),       # Monday true branch
    ("child", 8, "saturday", False, 150),       # weekend branch
    ("senior", 60, "sunday", False, 250),       # Sunday weekend branch
    ("student", 20, "tuesday", True, 200),      # tour + student surcharge
    ("adult", 25, "tuesday", True, 400),        # tour + non-student surcharge
    ("adult", 4, "sunday", True, 0),            # free under-five branch
])
def test_ticket_price_paths(category, age, day, tour, expected):
    assert ticket_price(category, age, day, tour) == expected


@pytest.mark.parametrize("category,age,day,tour,message", [
    ("invalid", 20, "tuesday", False, "unknown category"),
    ("adult", -1, "tuesday", False, "invalid age"),
])
def test_ticket_price_errors(category, age, day, tour, message):
    with pytest.raises(ValueError, match=message):
        ticket_price(category, age, day, tour)


@pytest.mark.parametrize("size,school,expected", [
    (20, True, 40),   # school group >= 20
    (19, True, 25),   # school group < 20
    (15, False, 20),  # non-school >= 15
    (8, False, 10),   # non-school >= 8 and < 15
    (7, False, 0),    # non-school < 8
])
def test_group_discount_branches(size, school, expected):
    assert group_discount(size, school) == expected


def test_group_discount_invalid_size():
    with pytest.raises(ValueError, match="invalid group size"):
        group_discount(0, True)


@pytest.mark.parametrize("inside,capacity,timed,expected", [
    (10, 10, False, "wait"),    # capacity reached
    (9, 10, False, "queue"),    # at 90%, no timed slot
    (9, 10, True, "enter"),     # at 90%, timed slot available
    (8, 10, False, "enter"),    # below 90%
])
def test_gallery_entry_branches(inside, capacity, timed, expected):
    assert gallery_entry(inside, capacity, timed) == expected
