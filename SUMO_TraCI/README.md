# SUMO_TraCI

An exemplary SUMO network with a Python TraCI interface to get started quickly. 

# Installation

## Windows
* go to [SUMO Downloads](http://sumo.dlr.de/wiki/Downloads#SUMO_-_Latest_Release_.28Version_1.0.0.29) and select the 64 bit installer: sumo-win64-1.0.0.msi
* run the installer and select to set all environment variables
* make sure that `sumoBinary` points to the right executable (e.g. `C:/Program Files (x86)/Eclipse/Sumo/bin/sumo-gui`)

# Launch
* start a new terminal window and run `python main.py`

# Netedit
* to manipulate the intersection type or the road type as well as the road layout netedit can be used

# 通过例子学习SUMO

## 一、一般示例

### 1. 示例1：使用jtrrouter命令生成rou.xml
### 2. 示例2：使用routes定义rou.xml
### 3. 示例3：trips2routes方式生成rou.xml（使用duarouter命令）
### 4. 示例4：flowsrouter方式生成rou.xml（使用duarouter命令）
#### 4.1 interval实现方式1
	```begin end```
#### 4.2 interval实现方式2
	```
		<interval begin="0" end="100">
		</interval>
	```
### 5. dfrouter示例
### 6. netconvert示例
### 7. 多个additional文件 <additional-files value="vehicles.xml,poi.xml,loops.xml,tls.add.xml"/>
包括道旁树木 
### 8. netstate dump (netstate output)
### 9. netgenerate示例
### od2trips示例
### 公交车
### 行人、自行车
### 应急车辆
###  converting SUMO outputs to CSV/Spreadsheet

## 二、复杂示例
### sumo-web3D 包

## 三、Python二次开发
