from ctypes import cdll, c_char_p, c_int, c_void_p
import ctypes.util


class Agent(object):
    def __init__(self, agent_name, socket='/var/agentx/master', mib_path=None):
        self._mib_path = mib_path
        self._started = False
        self._lib = NetSNMPWrapper()

        # Set the master socket
        self._lib.ds_set_string(DS_APPLICATION_ID, DS_AGENT_X_SOCKET, socket)

        # Set the agent role to agentx subagent
        self._lib.ds_set_boolean(DS_APPLICATION_ID, DS_AGENT_ROLE, True)

        # Init
        self._lib.init_agent(agent_name)
        self._lib.init_snmp(agent_name)

        # Load the MIB
        if mib_path is not None:
            self._lib.init_mib()
            self._lib.read_mib(mib_path)

    def run(self):
        self._started = True

        while self._started:
            self._lib.agent_check_and_process(1)

        self._lib.snmp_shutdown()

    def stop(self):
        self._started = False

    @property
    def socket(self):
        return self._lib.ds_get_string(DS_APPLICATION_ID, DS_AGENT_X_SOCKET)


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


class NetSNMPWrapper(object):
    def __init__(self):
        self._netsnmpagent = self._init_library()

    def _init_library(self):
        lib = cdll.LoadLibrary(ctypes.util.find_library('netsnmpagent'))

        function_defs = [
            (lib.init_agent, [c_char_p], c_int),
            (lib.init_snmp, [c_char_p], c_int),
            (lib.agent_check_and_process, [c_int], c_int),
            (lib.snmp_shutdown, [c_char_p], None),
            (lib.init_mib, [], None),
            (lib.read_mib, [c_char_p], c_void_p),  # Real return type is struct tree* but we don't care right now.

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

    def init_agent(self, name):
        _parse_exceptions(
            self._netsnmpagent.init_agent(name))

    def init_snmp(self, name):
        _parse_exceptions(
            self._netsnmpagent.init_snmp(name))

    def init_mib(self):
        self._netsnmpagent.init_mib()

    def read_mib(self, mib_path):  # TODO: var name
        self._netsnmpagent.read_mib(mib_path)

    def agent_check_and_process(self, block):
        """
        Checks for packets arriving on the SNMP port and processes them if any are found.
        :param block: If true the function call will block until a packet arrives or an alarm must be run
        :return: A positive integer if packets were processed, zero if an alarm occurred and -1 if an error occured
        """
        return self._netsnmpagent.agent_check_and_process(1 if block else 0)

    def snmp_shutdown(self, name):
        self._netsnmpagent.snmp_shutdown(name)

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
