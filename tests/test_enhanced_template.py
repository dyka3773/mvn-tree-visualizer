from mvn_tree_visualizer.enhanced_template import _dict_to_js_object


def test_dict_to_js_object_non_dict_values():
    assert _dict_to_js_object("hello") == '"hello"'
    assert _dict_to_js_object(True) == "true"
    assert _dict_to_js_object(42) == "42"


def test_dict_to_js_object_nested_dict():
    data = {"a": 1, "b": "text", "c": {"inner": False}}

    result = _dict_to_js_object(data)

    assert '"a": 1' in result
    assert '"b": "text"' in result
    assert '"c": {"inner": false}' in result
