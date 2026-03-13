# Ros2-and-ESP32-Communication-Using-Micro-Ros_And_blink_LED
---

# Complete Setup and Running Guide

This section explains how to run this repository from scratch. The process includes:

1. Install ROS2
2. Install micro-ROS tools
3. Upload Arduino code to ESP32
4. Run the micro-ROS Agent
5. Publish ROS2 messages
6. Visualize communication using `rqt_graph.`

These instructions assume **Ubuntu 22.04 and ROS2 Humble**.

---

# 1. Install ROS2

Update the system:

```
sudo apt update
```

Install ROS2 Humble desktop version:

```
sudo apt install ros-humble-desktop
```

Source ROS2:

```
source /opt/ros/humble/setup.bash
```

To automatically source ROS2 when a terminal opens:

```
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

Verify installation:

```
ros2 --version
```

---

# 2. Create Workspace and Install micro-ROS

Create a workspace:

```
mkdir -p ~/microros_ws/src
cd ~/microros_ws/src
```

Clone the micro-ROS setup repository:

```
git clone -b humble https://github.com/micro-ROS/micro_ros_setup.git
```

Move to the workspace root:

```
cd ~/microros_ws
```

Install dependencies:

```
rosdep update
rosdep install --from-paths src --ignore-src -y
```

Build the workspace:

```
colcon build
```

Source the workspace:

```
source install/local_setup.bash
```

---
---

# 3. Clone This Repository

Open a terminal and run:

```
git clone https://github.com/saeed-5340/Ros2-and-ESP32-Communication-Using-Micro-Ros_And_blink_LED.git
```

Move into the repository folder:

```
colcon build --symlink-install
```

This repository contains the Arduino program used in this tutorial.

Main file:

```
source install/setup.bash
```
---


# 3. Create and Build the micro-ROS Agent

The **micro-ROS Agent** connects the ESP32 micro-ROS node with the ROS2 network.

Create the agent workspace:

```
ros2 run micro_ros_setup create_agent_ws.sh
```

Build the agent:

```
ros2 run micro_ros_setup build_agent.sh
```

Source again:

```
source install/local_setup.bash
```

---

# 4. Install Arduino IDE and micro-ROS Library

Download Arduino IDE from:

https://www.arduino.cc/en/software

### Install ESP32 Board

Open Arduino IDE and go to:

```
File → Preferences
```

Add this URL to **Additional Board Manager URLs**:

```
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
```

Then install **ESP32 boards** from the Board Manager.

---

### Install micro-ROS Arduino Library

In Arduino IDE:

```
Sketch → Include Library → Manage Libraries
```

Search and install:

```
micro_ros_arduino
```

---

# 5. Upload Code to ESP32

Open the Arduino file from this repository:

```
led_blink_code_for_arduino_using_micro_ros.ino
```

Then:

1. Select **ESP32 board**
2. Select the correct **USB port**
3. Click **Upload**

After uploading, keep the ESP32 connected.

---

# 6. Run micro-ROS Agent

Open a terminal:

```
source /opt/ros/humble/setup.bash
source ~/microros_ws/install/local_setup.bash
```

Start the micro-ROS agent:

```
ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyUSB0
```

If the port is different, check:

```
ls /dev/ttyUSB*
```

After starting the agent, **press the RESET button on the ESP32**.
Note: If failed to connect with the ESP32, then first run
```
fuser /dev/ttyUSB0 2>&1 
```
{If /dev/tty* (Can be different, use correct port check the correct port using ``` ls /dev/ttyUSB*``` or ``` ls /dev/ttyACM* ``` }. After entering this command, you see a number, then type
```
kill (the number in the terminal shows)
```
After that, start the micro-ROS agent and **press the RESET button on the ESP32**.
```
ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyUSB0
```
---

# 7. Publish ROS2 Message

Open another terminal:

```
source /opt/ros/humble/setup.bash
```

Check available topics:

```
ros2 topic list
```

Publish message to control LED:

```
ros2 topic pub /blink_led std_msgs/msg/Int32 "{data: 1}"
```
or
```
 ros2 run led_blink_package blink_led_node 
```

LED behavior:

| Data | LED State |
| ---- | --------- |
| 1    | LED ON    |
| 0    | LED OFF   |

---

# 8. Visualize ROS Graph

Open another terminal:

```
source /opt/ros/humble/setup.bash
rqt_graph
```

This will show the connection between:

* ROS2 publisher
* micro-ROS agent
* ESP32 micro-ROS node

---

# Terminal Workflow

### Terminal 1 — Run Agent

```
source /opt/ros/humble/setup.bash
source ~/microros_ws/install/local_setup.bash
ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyUSB0
```

### Terminal 2 — Publish Message

```
source /opt/ros/humble/setup.bash
ros2 topic pub /blink_led std_msgs/msg/Int32 "{data: 1}"
```
or
```
source /opt/ros/humble/setup.bash
ros2 run led_blink_package blink_led_node 
```

### Terminal 3 — Visualization

```
rqt_graph
```

---

# Communication Flow

```
ROS2 Node
   │
   ▼
Publish Topic
   │
   ▼
micro-ROS Agent
   │
   ▼
ESP32 micro-ROS Node
   │
   ▼
LED ON / OFF
```

This demonstrates **ROS2 ↔ ESP32 communication using micro-ROS**.
