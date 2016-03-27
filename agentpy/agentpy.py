from ctypes import cdll, c_char_p, c_int
import ctypes.util


class Agent(object):

    DS_LIBRARY_ID = 0
    DS_APPLICATION_ID = 1
    DS_TOKEN_ID = 2

    DS_AGENT_X_SOCKET = 1

    def __init__(self):
        self._netsnmpagent = self._init_library()

    def _init_library(self):
        netsnmpagent = cdll.LoadLibrary(ctypes.util.find_library('netsnmpagent'))

        netsnmpagent.netsnmp_ds_set_string.argtypes = [c_int, c_int, c_char_p]
        netsnmpagent.netsnmp_ds_set_string.restype = c_int

        netsnmpagent.netsnmp_ds_get_string.argtypes = [c_int, c_int]
        netsnmpagent.netsnmp_ds_get_string.restype = c_char_p

        return netsnmpagent

    def init_agent(self, agent_name):
        _parse_exceptions(
            self._netsnmpagent.init_agent(agent_name))

    def ds_set_string(self, val1, val2, val3):
        _parse_exceptions(
            self._netsnmpagent.netsnmp_ds_set_string(val1, val2, val3))

    def ds_get_string(self, val1, val2):
        return self._netsnmpagent.netsnmp_ds_get_string(val1, val2)


_SNMP_ERR_NO_ERROR = 0


def _parse_exceptions(code):
    if code == _SNMP_ERR_NO_ERROR:
        return
    else:
        raise AgentPyException()


class AgentPyException(Exception):
    pass
