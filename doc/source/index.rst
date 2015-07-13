.. DataAPIsamplePy documentation master file, created by
   sphinx-quickstart on Thu Jul  9 12:09:55 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to DataAPIsamplePy's documentation!
===========================================

*“An investment in knowledge always pays the best interest.”*
Benjamin Franklin

- Usage::

    from indexstream import main
    key = "your_key_with_32_characters"
    request = main.Request(key)
    request.fetch("{'currencies': ['EUR/GBP', 'EUR/USD']}")

Contents:

.. toctree::
   :maxdepth: 2

**The IndexStream module**

.. automodule:: indexstream
    :members:
    :undoc-members:
    :inherited-members:
    :show-inheritance:

    .. autoclass:: indexstream.order.Urlformat
        :members:
        :undoc-members:
        :inherited-members:
        :show-inheritance:

    .. autoclass:: indexstream.order.Request
        :members:
        :undoc-members:
        :inherited-members:
        :show-inheritance:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

