import traci


def traffic_light_value_retrieve():
    ## 信号配时
    # 获取当前信号等状态
    ryg_state = traci.trafficlight.getRedYellowGreenState('J1')
    # 获取信号配时定义
    ryg_definition = traci.trafficlight.getCompleteRedYellowGreenDefinition('J1')
    # 获取当前相位时长
    phase_duration = traci.trafficlight.getPhaseDuration('J1')
    # 获取当前相位ID
    phase = traci.trafficlight.getPhase('J1')
    #print('phase:', phase)
    # 获取当前program
    program = traci.trafficlight.getProgram('J1')
    # 获取下一相位切换时间
    next_switch = traci.trafficlight.getNextSwitch('J1')
    # 获取当前仿真运行的时间
    sim_time = traci.simulation.getTime()

def lane_value_retrieve():
    # 获取车道上的数据， 指定车道'eJ1J4_1'
    traci.lane.getWidth('eJ1J4_1')
    traci.lane.getEdgeID('eJ1J4_1')
    traci.lane.getLength('eJ1J4_1')
    traci.lane.getDisallowed('eJ1J4_1')
    traci.lane.getMaxSpeed('eJ1J4_1')

    traci.lane.getCO2Emission('eJ1J4_1')
    traci.lane.getCOEmission('eJ1J4_1')
    traci.lane.getElectricityConsumption('eJ1J4_1')
    traci.lane.getFuelConsumption('eJ1J4_1')
    traci.lane.getHCEmission('eJ1J4_1')
    traci.lane.getNOxEmission('eJ1J4_1')
    traci.lane.getNoiseEmission('eJ1J4_1')
    traci.lane.getPMxEmission('eJ1J4_1')

    traci.lane.getLastStepVehicleIDs('eJ1J4_1')

    traci.lane.getLastStepHaltingNumber('eJ1J4_1') # 上一时刻排队车辆数
    traci.lane.getLastStepLength('eJ1J4_1') # 上一时刻，平均车辆长度 （m）
    traci.lane.getLastStepMeanSpeed('eJ1J4_1') #平均速度
    traci.lane.getLastStepOccupancy('eJ1J4_1') #占有率
    traci.lane.getLastStepVehicleNumber('eJ1J4_1')# 车辆数
    traci.lane.getTraveltime('eJ1J4_1') # 旅行时间
    traci.lane.getWaitingTime('eJ1J4_1') # 等待时间

def edge_value_retrieve():
    # 边上的信息检索
    traci.lane.getLastStepHaltingNumber('eJ1J4') # 上一时刻排队车辆数
    traci.lane.getLastStepLength('eJ1J4') # 上一时刻，平均车辆长度 （m）
    traci.lane.getLastStepMeanSpeed('eJ1J4') #平均速度
    traci.lane.getLastStepOccupancy('eJ1J4') #占有率
    traci.lane.getLastStepVehicleNumber('eJ1J4')# 车辆数
    traci.lane.getTraveltime('eJ1J4') # 旅行时间
    traci.lane.getWaitingTime('eJ1J4') # 等待时间

if __name__ == "__main__":
    sumo_start_config_gui = ["sumo-gui", "-c", "./4RL-test/simple6nodes.sumocfg", '--start']
    sumo_start_config_cmd = ["sumo", "-c", "./4RL-test/simple6nodes.sumocfg", '--start']

    traci.start(sumo_start_config_gui)

    step = 0
    while step < 3600:
        traci.simulationStep()
        step += 1

        # traffic_light_value_retrieve() # 获取信号配时相关参数
        # lane_value_retrieve() # 获取车道上的参数
        # edge_value_retrieve() # 获取 边 上的数据


