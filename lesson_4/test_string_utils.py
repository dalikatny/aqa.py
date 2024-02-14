from string_utils import StringUtils

dalik=StringUtils()

def test_capitilize():
    res=dalik.capitilize("dalik")
    assert res == 'Dalik'

def test_trim():
    res=dalik.trim(" dalik")
    assert res == 'dalik'

def test_to_list():
    res=dalik.to_list("a,b,c,d,e,f")
    assert res == ["a","b","c","d","e","f"]

def test_contains():
    res=dalik.contains("dalik","d")
    assert res == True

def test_delete_symbol():
    res=dalik.delete_symbol("dalik","d")
    assert res == "alik"

def test_starts_with():
    res=dalik.starts_with("dalik","d")
    assert res == True

def test_end_with():
    res=dalik.end_with("dalik","k")
    assert res == True

def test_is_empty():
    res=dalik.is_empty("")
    assert res == True

def test_list_to_string():
    res=dalik.list_to_string(["dalik","d"])
    assert res == "dalik, d"

