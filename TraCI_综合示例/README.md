# TraCI 综合示例

## 初始化

<div class="codehilite">
    <pre>
        <code class="language-python">
        import traci
        sumo_start_config_gui = ["sumo-gui", "-c", "./4RL-test/simple6nodes.sumocfg", '--start']
        sumo_start_config_cmd = ["sumo", "-c", "./4RL-test/simple6nodes.sumocfg", '--start']
        traci.start(sumo_start_config_gui)
        </code>
	</pre>
</div>



## 开始运行

<pre>
    <code>
    step = 0
	while step < 3600:
        traci.simulationStep()
        step += 1
    </code>
</pre>

## 检测数据采集

### 信号相关
<pre><code>
    # 获取当前信号灯的状态
    ryg_state = traci.trafficlight.getRedYellowGreenState('J1')
    print(ryg_state)
    # 结果：
    # GrrGGGGrrGGG
</code></pre>
<pre><code>
    #获取信号配时定义
    ryg_definition = traci.trafficlight.getCompleteRedYellowGreenDefinition('J1')
    print(ryg_definition)
    # 结果：
    [Logic(programID='0', type=0, currentPhaseIndex=2,
           phases=[Phase(duration=42.0, state='GGGGrrGGGGrr', minDur=42.0, maxDur=42.0, next=()),
                   Phase(duration=3.0, state='yyyyrryyyyrr', minDur=3.0, maxDur=3.0, next=()),
                   Phase(duration=42.0, state='GrrGGGGrrGGG', minDur=42.0, maxDur=42.0, next=()),
                   Phase(duration=3.0, state='yrryyyyrryyy', minDur=3.0, maxDur=3.0, next=())], subParameter={})]
</code></pre>      
<pre><code>
    # 获取当前相位时长
    phase_duration = traci.trafficlight.getPhaseDuration('J1')
    print('phase duration', phase_duration)
    # 获取当前相位ID或序号
    phase = traci.trafficlight.getPhase('J1')
    print('phase:', phase)
    # 获取当前program
    program = traci.trafficlight.getProgram('J1')
    print('program:', program)
    # 获取下一个相位的切换时间
    next_switch = traci.trafficlight.getNextSwitch('J1')
    print('next switch:', next_switch)
    # 获取当前仿真的时间
    sim_time = traci.simulation.getTime()
    print('simulation time:', sim_time)
    
    # 运行结果：
    # phase duration     42.0
    # phase: 2
    # program: 0
    # next switch: 357.0
    # simulation time: 322.0
</code></pre>    
<pre><code>
    # 边上的信息检索
    traci.lane.getLastStepHaltingNumber('eJ1J4') # 上一时刻排队车辆数
    traci.lane.getLastStepLength('eJ1J4') # 上一时刻，平均车辆长度 （m）
    traci.lane.getLastStepMeanSpeed('eJ1J4') #平均速度
    traci.lane.getLastStepOccupancy('eJ1J4') #占有率
    traci.lane.getLastStepVehicleNumber('eJ1J4')# 车辆数
    traci.lane.getTraveltime('eJ1J4') # 旅行时间
    traci.lane.getWaitingTime('eJ1J4') # 等待时间
</code></pre>
<pre><code>
    # 获取车道上的数据， 指定车道'eJ1J4_1'
    traci.lane.getLastStepHaltingNumber('eJ1J4_1') # 上一时刻排队车辆数
    traci.lane.getLastStepLength('eJ1J4_1') # 上一时刻，平均车辆长度 （m）
    traci.lane.getLastStepMeanSpeed('eJ1J4_1') #平均速度
    traci.lane.getLastStepOccupancy('eJ1J4_1') #占有率
    traci.lane.getLastStepVehicleNumber('eJ1J4_1')# 车辆数
    traci.lane.getTraveltime('eJ1J4_1') # 旅行时间
    traci.lane.getWaitingTime('eJ1J4_1') # 等待时间
</code></pre>
## 参数修改

