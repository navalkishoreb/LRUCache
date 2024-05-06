

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
pytest
`

### Test Output

```
======================================================================================================= test session starts ========================================================================================================
platform linux -- Python 3.9.6, pytest-8.2.0, pluggy-1.5.0
rootdir: /home/naval/Documents/LRUCache
plugins: timeout-2.3.1
collected 17 items                                                                                                                                                                                                                 

tests/test_lru_cache.py ....                                                                                                                                                                                                 [ 23%]
tests/test_lru_cache_with_threads.py ..                                                                                                                                                                                      [ 35%]
tests/test_ordered_dictionary.py ......                                                                                                                                                                                      [ 70%]
tests/test_ordered_list.py ....x                                                                                                                                                                                             [100%]

================================================================================================== 16 passed, 1 xfailed in 2.24s ===================================================================================================
```