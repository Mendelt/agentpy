import ctypes
import ctypes.util


class Agent(object):

    def __init__(self):
        self._netsnmpagent = ctypes.cdll.LoadLibrary(ctypes.util.find_library('netsnmpagent'))

    def init_agent(self, agent_name):
        self._netsnmpagent.init_agent(agent_name)
