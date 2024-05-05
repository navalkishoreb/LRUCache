from src.ordered_list import OrderedList


def test_order_list():
    ordered_obj = OrderedList()
    ordered_obj.update("a")
    assert ordered_obj == ["a"]
    ordered_obj.update("b")
    assert ordered_obj == ["b", "a"]
    ordered_obj.update("a")
    assert ordered_obj == ["a", "b"]


def test_ordered_list_last_element():
    ordered_obj = OrderedList()
    ordered_obj.update("a")
    ordered_obj.update("b")
    value = ordered_obj.last_element()
    assert value == "a"


def test_ordered_list_remove_last_element():
    ordered_obj = OrderedList()
    ordered_obj.update("a")
    ordered_obj.update("b")
    value = ordered_obj.remove_last_element()
    assert value == "a"
    assert ordered_obj == ["b"]


def test_ordered_list_remove_last_element_when_empty():
    ordered_obj = OrderedList()
    value = ordered_obj.remove_last_element()
    assert value is None
    assert ordered_obj == []
