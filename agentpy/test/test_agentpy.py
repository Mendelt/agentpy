from pytest import fixture
from agentpy.agentpy import Agent


@fixture
def agent():
    return Agent('name', socket=None, mib_path='agentpy/test/AGENTPY-TESTING-MIB.txt')


def test_can_construct_agent(agent):
    assert agent is not None
