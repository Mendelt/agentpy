from ctypes import cdll, c_char_p, c_int
import ctypes.util


class Agent(object):

    DS_LIBRARY_ID = 0
    DS_APPLICATION_ID = 1
    DS_TOKEN_ID = 2

    # Boolean values
    DS_AGENT_VERBOSE = 0  # 1 if verbose output desired
    DS_AGENT_ROLE = 1  # 0 if master, 1 if client
    DS_AGENT_NO_ROOT_ACCESS = 2  # 1 if we can't get root access
    DS_AGENT_AGENTX_MASTER = 3  # 1 if AgentX desired
    DS_AGENT_QUIT_IMMEDIATELY = 4  # 1 to never start the agent
    DS_AGENT_DISABLE_PERL = 5  # 1 to never enable perl
    DS_AGENT_NO_CONNECTION_WARNINGS = 6  # 1 = !see !connect msgs
    DS_AGENT_LEAVE_PIDFILE = 7  # 1 = leave PID file on exit
    DS_AGENT_NO_CACHING = 8  # 1 = disable netsnmp_cache
    DS_AGENT_STRICT_DISMAN = 9  # 1 = "correct" object ordering
    DS_AGENT_DONT_RETAIN_NOTIFICATIONS = 10  # 1 = disable trap logging
    DS_AGENT_DONT_LOG_TCPWRAPPERS_CONNECTS = 12  # 1 = disable logging
    # TODO DS_APP_DONT_LOG         NETSNMP_DS_AGENT_DONT_RETAIN_NOTIFICATIONS /* compat */
    DS_AGENT_SKIPNFSINHOSTRESOURCES = 13  # 1 = don't store NFS entries in hrStorageTable
    DS_AGENT_REALSTORAGEUNITS = 14  # 1 = use real allocation units in hrStorageTable, 0 = recalculate it to fit 32bits

    # String values
    DS_AGENT_X_SOCKET = 1

    def __init__(self):
        self._netsnmpagent = self._init_library()

    def _init_library(self):
        lib = cdll.LoadLibrary(ctypes.util.find_library('netsnmpagent'))

        function_defs = [
            (lib.init_agent, [c_char_p], c_int),

            (lib.netsnmp_ds_get_boolean, [c_int, c_int], c_int),
            (lib.netsnmp_ds_set_boolean, [c_int, c_int, c_int], c_int),
            (lib.netsnmp_ds_toggle_boolean, [c_int, c_int], c_int),

            (lib.netsnmp_ds_get_string, [c_int, c_int], c_char_p),
            (lib.netsnmp_ds_set_string, [c_int, c_int, c_char_p], c_int),
        ]

        for function, args, res in function_defs:
            function.argtypes = args
            function.restype = res

        return lib

    def init_agent(self, agent_name):
        _parse_exceptions(
            self._netsnmpagent.init_agent(agent_name))

    def ds_get_boolean(self, storeid, which):
        return self._netsnmpagent.netsnmp_ds_get_boolean(storeid, which) == 1

    def ds_set_boolean(self, storeid, which, value):
        _parse_exceptions(
            self._netsnmpagent.netsnmp_ds_set_boolean(storeid, which, 1 if value else 0))

    def ds_toggle_boolean(self, storeid, which):
        _parse_exceptions(
            self._netsnmpagent.netsnmp_ds_toggle_boolean(storeid, which))

    def ds_get_string(self, storeid, which):
        return self._netsnmpagent.netsnmp_ds_get_string(storeid, which)

    def ds_set_string(self, storeid, which, value):
        _parse_exceptions(
            self._netsnmpagent.netsnmp_ds_set_string(storeid, which, value))


_SNMP_ERR_NO_ERROR = 0


def _parse_exceptions(code):
    if code == _SNMP_ERR_NO_ERROR:
        return
    else:
        raise AgentPyException()


class AgentPyException(Exception):
    pass
