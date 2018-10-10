simple_watchdog_timer
=====================

Requirements
-------------

* Python -- one of the following:

  - CPython_ : >= 3.3
  - PyPy_ : Latest version

.. _CPython: https://www.python.org/
.. _PyPy: https://pypy.org/

Installation
------------

Package is uploaded on `PyPI <https://pypi.org/project/simple_watchdog_timer>`_.

You can install it with pip::

    $ python3 -m pip install simple_watchdog_timer


Backwards compatibility
-----------------------

Backwards compatibility is only guaranteed between minor versions above the stable version (1.0)
Therefore it's advised to to pin the module on a version ether the specific version like:
simple_watchdog_timer==X.X.X

or get the latest minor version:
simple_watchdog_timer~=X.X.X

See more examples of how to pin version in `PEP-440 <https://www.python.org/dev/peps/pep-0440/#compatible-release>`_.


Documentation
-------------

For support, please refer to `StackOverflow <https://stackoverflow.com/>`_.

Example
-------

The following example showcases the usage

.. code:: python

    import simple_watchdog_timer as swt
    from random import uniform
    from time import sleep


    def cb(dog):
        # When the callback gets triggered, it's good practice to pause the WDT to prevent it firing again, while you are handling the action required when it triggers
        dog.pause()

        # Do something when the WDT triggers...
        print('WDT Triggered')

        # Update / reset the internal WDT timer (dog.reset() does the same), this is important to avoid the time spent in the callback to influence the next triggering
        dog.update()

        # Resume the WDT
        dog.resume()

        # ...or:

        # If you would like to completely stop the WDT
        # dog.stop()

        # But you regret and want to start it again
        # dog.start()

        # Tip: stop() and start() can also be used instead of the more manual pause, update and resume if that is preferred (more simple, but less in-line expressive)


    def main():
        wdt = swt.WDT(check_interval_sec=0.01, trigger_delta_sec=0.50, callback=cb)

        while True:
            zzz_sec = uniform(0, 0.60)
            print('Sleep for {}'.format(zzz_sec))
            sleep(zzz_sec)

            wdt.update()


    if __name__ == '__main__':
        main()

This example will print:

.. code:: python

    Raw data:
    Sleep for 0.1492276414753453
    Sleep for 0.5913061085397784
    WDT Triggered
    Sleep for 0.17619615161373772
    Sleep for 0.5853218597734956
    WDT Triggered
    Sleep for 0.38154937243934783
    Sleep for 0.5000195244886919
    WDT Triggered
    Sleep for 0.08607711764377268
    Sleep for 0.31192761174090605
    Sleep for 0.02722456895623042

License
-------

TimedDict is released under the MIT License. See LICENSE for more information.