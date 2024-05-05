

## To install 

```

git clone https://github.com/navalkishoreb/LRUCache.git

cd LRUCache
python3.8 -v venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## To run test cases

` 
pytest -rA tests/
`

### Test Output

```
===================================================================================================== short test summary info ======================================================================================================
PASSED tests/test_lru_cache.py::test_cache
PASSED tests/test_lru_cache.py::test_cache_out_of_capacity
PASSED tests/test_lru_cache.py::test_cache_when_same_key_is_inserted
PASSED tests/test_ordered_list.py::test_order_list
PASSED tests/test_ordered_list.py::test_ordered_list_last_element
PASSED tests/test_ordered_list.py::test_ordered_list_remove_last_element
PASSED tests/test_ordered_list.py::test_ordered_list_remove_last_element_when_empty
======================================================================================================== 7 passed in 0.02s =========================================================================================================
```