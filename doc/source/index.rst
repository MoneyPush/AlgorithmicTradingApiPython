.. DataAPIsamplePy documentation master file, created by
   sphinx-quickstart on Thu Jul  9 12:09:55 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to AlgorithmicTradingApiPython's documentation!
=======================================================

*“An investment in knowledge always pays the best interest.”*
Benjamin Franklin

- Usage::

    from bigdatatrade import trade
    key = "your_key_with_32_characters"
    request = trade.Request(key)
    request.fetch("{'currencies': ['EUR/GBP', 'EUR/USD']}")

Contents:

.. toctree::
   :maxdepth: 2

**The IndexStream module**

.. automodule:: bigdatatrade
    :members:
    :undoc-members:
    :inherited-members:
    :show-inheritance:

    .. autoclass:: bigdatatrade.trade.Urlformat
        :members:
        :undoc-members:
        :inherited-members:
        :show-inheritance:

    .. autoclass:: bigdatatrade.trade.Request
        :members:
        :undoc-members:
        :inherited-members:
        :show-inheritance:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

