from string_utils import StringUtils

dalik=StringUtils()

def test_capitilize():
    dalik=StringUtils()
    res=dalik.capitilize("dalik")
    assert res == 'Dalik'

def test_trim():
    dalik=StringUtils()
    res=dalik.trim("   dalik")
    assert res == 'dalik'

def test_to_list():
    dalik=StringUtils()
    res=dalik.to_list("abcdef",",")
    assert res == ["a","b","c","d","e","f"]

def test_contains():
    dalik=StringUtils()
    res=dalik.contains("dalik","d")
    assert res == True

def test_delete_symbol():
    dalik=StringUtils()
    res=dalik.delete_symbol("dalik","d")
    assert res == "alik"

def test_starts_with():
    dalik=StringUtils()
    res=dalik.starts_with("dalik","d")
    assert res == True

def test_end_with():
    dalik=StringUtils()
    res=dalik.end_with("dalik","K")
    assert res == True

def test_is_empty():
    dalik=StringUtils()
    res=dalik.is_empty("")
    assert res == True

def test_list_to_string():
    dalik=StringUtils()
    res=dalik.list_to_string["dalik","d"]
    assert res == "dalik","d"

