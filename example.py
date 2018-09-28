from simple_watchdog_timer.simple_watchdog_timer import WDT
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
    wdt = WDT(check_interval_sec=0.01, trigger_delta_sec=0.50, callback=cb)

    while True:
        zzz_sec = uniform(0, 0.60)
        print('Sleep for {}'.format(zzz_sec))
        sleep(zzz_sec)

        wdt.update()


if __name__ == '__main__':
    main()
