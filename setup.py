from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys


class PyTest(TestCommand):
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ['agentpy']

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='agentpy',
    version='0.01a',
    author='Mendelt Siebenga',
    author_email='mendelt@msiebenga.com',
    description='Implement your own agentX subagent using netsnmp',
    license='MIT',
    keywords='',
    url='',
    packages=['agentpy'],
    setup_requires=[],
    tests_requires=['pytest'],
    cmdclass={'test': PyTest}
)
