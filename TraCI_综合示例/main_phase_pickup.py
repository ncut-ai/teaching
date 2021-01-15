import traci


if __name__ == "__main__":
    sumo_start_config_gui = ["sumo-gui", "-c", "./4RL-test/simple6nodes.sumocfg", '--start']
    sumo_start_config_cmd = ["sumo", "-c", "./4RL-test/simple6nodes.sumocfg", '--start']

    traci.start(sumo_start_config_gui)

    step=0

    phase_0_extended = 0
    while step < 360:


        """判断是否开始某个相位"""
        current_phase_id = traci.trafficlight.getPhase('J1')
        current_phase_duration = traci.trafficlight.getPhaseDuration('J1')
        next_switch = traci.trafficlight.getNextSwitch('J1')
        sim_time = traci.simulation.getTime()

        if next_switch - sim_time == current_phase_duration-1:  # 开始直行某个相位
            if current_phase_id == 0:
                print('开始：东西直行相位')
                phase_0_extended = 0  # 恢复标志，即允许修改
            elif current_phase_id == 2:
                print('开始：南北直行相位')
            else:
                pass

        """执行仿真"""
        traci.simulationStep()
        step += 1

        """判断是否完成某个相位"""
        current_phase_id = traci.trafficlight.getPhase('J1')
        current_phase_duration = traci.trafficlight.getPhaseDuration('J1')
        next_switch = traci.trafficlight.getNextSwitch('J1')
        sim_time = traci.simulation.getTime()

        if next_switch == sim_time:# 当前相位直行结束
            if current_phase_id == 0:
                print('结束：东西直行相位')
                if phase_0_extended == 0:
                    traci.trafficlight.setPhaseDuration('J1',3)# 加了3秒
                    phase_0_extended = 1 # 修改相位时长标识，修改标志后执行完该相位前，不再修改相位长度
            elif current_phase_id == 2:
                print('结束：南北直行相位')
            else:
                pass


