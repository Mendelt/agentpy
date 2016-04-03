from pytest import fixture
from agentpy.agentpy import Agent


@fixture
def agent():
    return Agent('name', 'mib', 'socket')


def test_can_construct_agent(agent):
    assert agent is not None
