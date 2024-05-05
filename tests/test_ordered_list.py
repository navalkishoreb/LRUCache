from src.ordered_list import OrderedList


def test_order_list():
    ordered_obj = OrderedList()
    ordered_obj.update("a")
    assert ordered_obj == ["a"]
    ordered_obj.update("b")
    assert ordered_obj == ["b", "a"]
    ordered_obj.update("a")
    assert ordered_obj == ["a", "b"]
