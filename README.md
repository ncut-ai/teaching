# 北方工业大学 交通仿真技术课程 ![Image](http://www.ncut.edu.cn/images/logo.png)
 SUMO教学相关
## 软件下载、安装与环境配置

### Python
Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.

下载地址：  
https://www.python.org/downloads/



### Pycharm 社区版

适用于纯 Python 开发

面向专业开发者的 Python IDE  
PyCharm是程序员为程序员设计的开发环境，提供您进行 高效Python开发所需的所有工具。

下载地址：
https://www.jetbrains.com/zh-cn/pycharm/download/#section=windows


### Sumo

SUMO是一个微观的，空间上连续，时间上离散的交通仿真软件，采用c++语言开发，其宏观特征包括带变道的多车道道路，基于道路交叉口的靠右侧行驶规则，支持动态路由，可以管理超过10000条街道的网络。其微观特征包括允许碰撞自由的车辆移动模式，支持单车路由。该软件特点是具有快速的OpenGL图形界面，支持多种网络格式输入，缺点是sumo本身不能提供网络仿真器所需要的轨迹文件。  
SUMO可去官网下载（https://www.eclipse.org/sumo/），解压后就可以使用，图形界面软是在解压后bin文件夹下的sumo-gui.exe。使用前最好设置环境变量SUMO_HOME。其实不设置似乎也可以使用，但是会有警告。SUMO_HOME的内容就是安装文件的位置，也就是bin文件夹的上一级目录。  
SUMO解压之后，作重要的是bin文件夹下的程序和tools文件夹下的程序。bin文件夹下大部分是可执行文件，但是并不像普通的可执行文件一样打开，而是需要用命令行打开，换句话说，整个功能程序并没有被包装起来，这是出于可裁剪和可维护性角度考虑的。tools下的工具则更多的是用phyton写的。

#### sumo工程结构
SUMO的仿真至少需要两个文件：  
1.道路文件，或者叫路网文件（net.xml），就是对行车道路的描述文件；  
2.车流文件(rou.xml)，或者叫做车量行驶文件，用来描述车流量的行为。当然，更加高级的仿真可以加入别的文件，比如车辆描述文件，地形文件。  
这个很容易理解，想要做仿真，最起码要有地图吧，这就是路网文件net,xml;有了地图后是不是还要产生几辆车呢，不管你怎么产生，总之得有车，产生车的规则随意定，这就是rou.xml文件的功能。
 
道路文件的产生有好多种方法，我们先简单的来了解两个，第一个是从开源的地图上下载osm地图文件，常用的是openstreetmap（osm是一种地图信息文件，可以去openstreetmap官网下载。网址：http://www.openstreetmap.org/），然后利用sumo自带的netconvert工具将osm文件转换为net.xml文件；第二个是自己"编写"net.xml文件，我目前学习到的并不是直接开始编写net.xml文件，因为在sumo规定中，道路是由节点和边组成的，也符合我们一贯的数学思维，所以我们会先编写nod.xml节点文件和edg.xml边文件，然后通过netconvert工具去将这两个文件结合成net.xml文件；除了这两种方法外还有通过OD矩阵啊，等等产生路网文件，不过我还没了解，所以先不做深入介绍，可以到官网查看，官网介绍的很详细，本文主要是做个快速教程。  
车流行驶文件即规定车辆数量，车辆行驶规则等，实验目的不同，规则自然千变万化，所以rou.xml的产生自然也有很多的方法，本教程中使用的是sumo自带的一个radomTrips.py，它是一个工具，通过调用这个工具可以在已有的net.xml上产生车辆行驶规则，利用它和上面的net,xml就可以产生rou.xml文件，当然，本实验纯粹为了演示，所以利用的已有的随机路径

#### 教程
如果想要了解更多的话，请参考sumo官方文档http://www.sumo.dlr.de/userdoc/SUMO-GUI.html

## Sumo上机指导

见文件夹“Sumo上机指导”

## Python调用TraCI上机指导
# 通过例子学习SUMO

## 一、一般示例

### 1. 示例1：使用jtrrouter命令生成rou.xml
### 2. 示例2：使用routes定义rou.xml
### 3. 示例3：trips2routes方式生成rou.xml（使用duarouter命令）
### 4. 示例4：flowsrouter方式生成rou.xml（使用duarouter命令）
#### 4.1 interval实现方式1
	begin end
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
