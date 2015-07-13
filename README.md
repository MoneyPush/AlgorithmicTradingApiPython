# AlgorithmicTradingApiPython

BigDataTrade Financial market stream API in Python enables to access to real-time financial quotes. This repository shows how to get the data with a Python Client

# Install Instructions

This package works with the most recent versions of python preferably python3.4

```
git clone [https://github.com/BigDataTrade/AlgorithmicTradingApiPython.git][https://github.com/BigDataTrade/AlgorithmicTradingApiPython.git]
cd  AlgorithmicTradingApiPython 
python setup.py install
```


# Usage Instructions

Check that your 3002 port is avalaible and opened.

The key required is available in the personal informations of your account at  [http://www.bigdata-trade.com/][http://www.bigdata-trade.com/]

```python
    from bigdatatrade import trade
    key = "your_key_with_32_characters"
    request = trade.Request(key)
    request.fetch("{'currencies': ['EUR/GBP', 'EUR/USD']}")
```

It is also possible to fetch all the symbols at the same time :

```python
    from bigdatatrade import trade
    key = "your_key_with_32_characters"
    request = trade.Request(key)
    request.fetch("{'currencies': ['AllSymbol']}")
```
