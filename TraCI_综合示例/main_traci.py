import traci

sumo_start_config_gui = ["sumo-gui", "-c", "./4RL-test/simple6nodes.sumocfg", '--start']
sumo_start_config_cmd = ["sumo", "-c", "./4RL-test/simple6nodes.sumocfg", '--start']

traci.start(sumo_start_config_gui)

step = 0
while step < 3600:
    traci.simulationStep()
    step += 1
