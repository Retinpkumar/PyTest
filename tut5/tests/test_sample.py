# Test fixtures: Explicit, modular, scalable
# Used for database connections or request sessions
# To use a pytest fixture, pass the parameter to the function having
# the same name as the pytest fixture.

import json
import os
from tut5.myapp.sample import save_dict

def test_save_dict(tmpdir, capsys):
    filepath = os.path.join(tmpdir, "test.json")
    _dict = {"a":1, "b":2}

    save_dict(_dict, filepath)
    assert json.load(open(filepath, 'r')) == _dict
    assert capsys.readouterr().out == "saved\n"
