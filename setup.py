from setuptools import setup
from setuptools.command.test import test
import sys


class PyTest(test):
    def initialize_options(self):
        test.initialize_options(self)
        self.pytest_args = ['agentpy']

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='agentpy',
    version='0.1a0',
    author='Mendelt Siebenga',
    description='Implement your own agentX subagent using netsnmp',
    license='MIT',
    keywords='',
    url='',
    packages=['agentpy'],
    setup_requires=[],
    tests_requires=['pytest'],
    cmdclass={'test': PyTest}
)

