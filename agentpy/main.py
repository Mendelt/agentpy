import agentpy


def main():
    # agent = agentpy.LibNetSNMP()
    #
    # agent.ds_set_string(agentpy.DS_APPLICATION_ID, agentpy.DS_AGENT_X_SOCKET, 'agentx_socket')
    # print(agent.ds_get_string(agentpy.DS_APPLICATION_ID, agentpy.DS_AGENT_X_SOCKET))
    #
    # print(agent.ds_get_boolean(agentpy.DS_APPLICATION_ID, agentpy.DS_AGENT_ROLE))
    # agent.ds_set_boolean(agentpy.DS_APPLICATION_ID, agentpy.DS_AGENT_ROLE, True)
    # print(agent.ds_get_boolean(agentpy.DS_APPLICATION_ID, agentpy.DS_AGENT_ROLE))
    # agent.ds_toggle_boolean(agentpy.DS_APPLICATION_ID, agentpy.DS_AGENT_ROLE)
    # print(agent.ds_get_boolean(agentpy.DS_APPLICATION_ID, agentpy.DS_AGENT_ROLE))
    # agent.ds_toggle_boolean(agentpy.DS_APPLICATION_ID, agentpy.DS_AGENT_ROLE)
    #
    # agent.init_agent('Stuff')
    # agent.init_snmp('Stuff')
    #
    # agent.init_mib()
    # agent.read_mib('mibs/AGENTPY-TESTING-MIB.txt')
    #
    # agent.agent_check_and_process(0)
    # agent.snmp_shutdown('Stuff')

    agent = agentpy.Agent('Agent', 'mibs/AGENTPY-TESTING-MIB.txt', 'socket')
    agent.run()


if __name__ == '__main__':
    main()
