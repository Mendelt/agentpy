import agentpy


def main():
    agent = agentpy.Agent()
    test = agent.init_agent('Stuff')
    print(test)

    agent.ds_set_string(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_X_SOCKET, 'agentx_socket')
    test = agent.ds_get_string(agentpy.Agent.DS_APPLICATION_ID, agentpy.Agent.DS_AGENT_X_SOCKET)
    print(test)

if __name__ == '__main__':
    main()
