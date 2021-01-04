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

## 参数修改

