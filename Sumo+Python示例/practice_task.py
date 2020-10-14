import sys
import os
import traci
import traci.constants as tc
import pandas as pd
import numpy as np

# 仿真模型
# sumoCmd = ["sumo", "-c", "*****.sumocfg"]
sumoCmd = ["sumo-gui", "-c", "./task/task.sumocfg.xml", '--start']
##--------------------------初始化仿真 traci -----------------------------
traci.start(sumoCmd)
step = 0  # 设置步长计数

y = [0, 0, 0, 0]

J1 = ['gneE12', 'gneE10', "gneE16", "gneE14"]

def queue_count(j):
    queuecountEdge0 = traci.edge.getLastStepHaltingNumber(j[0])
    queuecountEdge1 = traci.edge.getLastStepHaltingNumber(j[1])
    queuecountEdge2 = traci.edge.getLastStepHaltingNumber(j[2])
    queuecountEdge3 = traci.edge.getLastStepHaltingNumber(j[3])
    return [queuecountEdge0, queuecountEdge1, queuecountEdge2, queuecountEdge3]

def main_step():
    for r in queue_count(J1):
        if r > 4:
            traci.trafficlight.setPhaseDuration('J1', 0)

## ------------------------------  开始进行仿真  ------------------------------------------
# Run a simulation until all vehicles have arrived
while traci.simulation.getMinExpectedNumber() > 0:
    # print("step", step)
    step += 1
    traci.simulationStep()
    # print('step', step)
    y = np.row_stack((y, queue_count(J1)))

    e = pd.DataFrame(columns=None, data=y)
    print(e)
    e.to_csv('E:/pythonProject666/task/queue_count1.csv')
    main_step()

traci.close()