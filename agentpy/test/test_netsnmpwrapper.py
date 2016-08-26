from pytest import fixture
from agentpy.agentpy import NetSNMPWrapper, DS_APPLICATION_ID, DS_AGENT_X_SOCKET, DS_AGENT_ROLE


@fixture
def wrapper():
    return NetSNMPWrapper()


def test_should_set_and_get_string(wrapper):
    wrapper.ds_set_string(DS_APPLICATION_ID, DS_AGENT_X_SOCKET, 'agentx_socket')
    assert wrapper.ds_get_string(DS_APPLICATION_ID, DS_AGENT_X_SOCKET) == 'agentx_socket'


def test_should_set_and_get_boolean(wrapper):
    # Set to true and test
    wrapper.ds_set_boolean(DS_APPLICATION_ID, DS_AGENT_ROLE, True)
    assert wrapper.ds_get_boolean(DS_APPLICATION_ID, DS_AGENT_ROLE) is True

    # Set to false and test
    wrapper.ds_set_boolean(DS_APPLICATION_ID, DS_AGENT_ROLE, False)
    assert wrapper.ds_get_boolean(DS_APPLICATION_ID, DS_AGENT_ROLE) is False


def test_should_toggle_boolean(wrapper):
    # First set to false
    wrapper.ds_set_boolean(DS_APPLICATION_ID, DS_AGENT_ROLE, False)
    wrapper.ds_toggle_boolean(DS_APPLICATION_ID, DS_AGENT_ROLE)
    assert wrapper.ds_get_boolean(DS_APPLICATION_ID, DS_AGENT_ROLE) is True
