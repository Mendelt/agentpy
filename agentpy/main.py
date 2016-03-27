import agentpy


def main():
    agent = agentpy.Agent()

    agent.init_agent('Stuff')

    agent.ds_set_string(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_X_SOCKET, 'agentx_socket')
    print(agent.ds_get_string(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_X_SOCKET))

    print(agent.ds_get_boolean(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_ROLE))
    agent.ds_set_boolean(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_ROLE, True)
    print(agent.ds_get_boolean(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_ROLE))
    agent.ds_toggle_boolean(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_ROLE)
    print(agent.ds_get_boolean(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_ROLE))


if __name__ == '__main__':
    main()
