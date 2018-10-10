from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='simple_watchdog_timer',
    version='0.1.1',
    packages=[''],
    url='https://github.com/hjortlund/simple_watchdog_timer',
    license='MIT',
    author='Christoffer Hjortlund',
    author_email='hjortlund@gmail.com',
    description='A simple WatchDog Timer (WDT) to trigger events if inactivity, of a time dependent task, occur for a specified amount of time.',
    long_description=readme(),
    long_description_content_type="text/markdown",
)
