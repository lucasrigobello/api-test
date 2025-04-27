from app.utils.functions import primeiro_test, get_age

def test_init():
    name = primeiro_test('Lucas')
    assert name == 'Lucas'

def test_get_age():
    # Given.
    yyyy, mm, dd = map(int, "1996/07/11".split("/"))   
    # When.
    age = get_age(yyyy, mm, dd)
    # Then.
    assert age == 29