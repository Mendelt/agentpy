import agentpy


def main():
    agent = agentpy.Agent()

    agent.ds_set_string(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_X_SOCKET, 'agentx_socket')
    print(agent.ds_get_string(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_X_SOCKET))

    print(agent.ds_get_boolean(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_ROLE))
    agent.ds_set_boolean(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_ROLE, True)
    print(agent.ds_get_boolean(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_ROLE))
    agent.ds_toggle_boolean(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_ROLE)
    print(agent.ds_get_boolean(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_ROLE))
    agent.ds_toggle_boolean(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_ROLE)

    agent.init_agent('Stuff')
    agent.init_snmp('Stuff')
    agent.agent_check_and_process(0)
    agent.snmp_shutdown('Stuff')

if __name__ == '__main__':
    main()
