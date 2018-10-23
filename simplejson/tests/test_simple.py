import simplejson as json

JSON = r'''
[
    "JSON Test Pattern",
    {"object with 1 member":["array with 1 element"]},
    {},
    [],
    -42,
    true,
    false,
    null,
    {
        "integer": 1234567890,
        "alpha": "abcdefghijklmnopqrstuvwyz"
    },
    "rosebud"
]
'''

def test_parse():
    # test in/out equivalence and parsing
    res = json.loads(JSON)
    out = json.dumps(res)
    assert res == json.loads(out)
