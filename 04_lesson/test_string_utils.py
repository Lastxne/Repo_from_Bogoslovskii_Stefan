import pytest
from string_utils import StringUtils

utils = StringUtils()


# --- capitalize ---
@pytest.mark.parametrize("input_str,expected", [
    ("skypro", "Skypro"),
    ("SkyPro", "Skypro"),
    ("123abc", "123abc"),
    (" s", " s"),
    ("", "")
])
def test_capitalize_positive(input_str, expected):
    assert utils.capitalize(input_str) == expected


def test_capitalize_negative():
    with pytest.raises(AttributeError):
        utils.capitalize(None)
    with pytest.raises(AttributeError):
        utils.capitalize(123)


# --- trim ---
@pytest.mark.parametrize("input_str,expected", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("   ", ""),
    ("", "")
])
def test_trim_positive(input_str, expected):
    assert utils.trim(input_str) == expected


def test_trim_negative():
    with pytest.raises(AttributeError):
        utils.trim(None)
    with pytest.raises(AttributeError):
        utils.trim(123)


# --- contains ---
@pytest.mark.parametrize("string,symbol,expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("abc", "a", True)
])
def test_contains_positive(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


def test_contains_negative():
    assert utils.contains("abc", "") is True  # known defect
    with pytest.raises(TypeError):
        utils.contains("abc", None)
    with pytest.raises(AttributeError):
        utils.contains(None, "a")


# --- delete_symbol ---
@pytest.mark.parametrize("string,symbol,expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("aaa", "a", ""),
    ("abc", "x", "abc"),
    ("", "a", "")
])
def test_delete_symbol_positive(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


def test_delete_symbol_negative():
    assert utils.delete_symbol("abc", "") == "abc"  # questionable behavior
    with pytest.raises(TypeError):
        utils.delete_symbol("abc", None)
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "a")
