# micro-ROS Beginner Guide (ESP32 / Arduino)

This repository demonstrates a **basic micro-ROS program on ESP32 using Arduino**.
The goal is to help beginners understand **how a micro-ROS node works internally**, using a simple example such as **LED control or message subscription**.

The README explains the **execution flow of a micro-ROS program**, so that even someone new to ROS2 can understand what happens inside the code.

---

# What is micro-ROS

**micro-ROS** is a framework that allows **microcontrollers (ESP32, STM32, Arduino, etc.) to communicate with ROS2 systems**.

Instead of running a full ROS2 environment on the microcontroller, micro-ROS provides a **lightweight ROS2 client library** that communicates with the ROS2 network through a **micro-ROS Agent**.

Typical architecture:

```
ROS2 PC
   │
   │ DDS communication
   ▼
micro-ROS Agent
   │
   │ serial / WiFi / UDP
   ▼
ESP32 / Microcontroller running micro-ROS node
```

This allows microcontrollers to **publish sensor data or receive commands from ROS2**.

---

# Example Use Case

A simple beginner example is:

* ROS2 publishes a number
* ESP32 receives the number
* ESP32 controls an LED based on that value

Example:

```
ros2 topic pub /led_control std_msgs/msg/Int32 "{data: 1}"
```

If `data = 1` → LED ON
If `data = 0` → LED OFF

---

# micro-ROS Program Architecture

A micro-ROS Arduino program is typically structured into two main parts:

```
main program
│
├── setup()
│     ├── allocator
│     ├── support
│     ├── node
│     ├── publisher/subscriber
│     └── executor
│
└── loop()
      └── executor_spin_some()
             └── callback execution
```

The **setup() function initializes the ROS system**, while the **loop() function processes incoming messages**.

---

# Step-by-Step micro-ROS Initialization

When the ESP32 starts running the program, the following sequence happens.

```
Arduino Power ON
       │
       ▼
Get Allocator
allocator = rcl_get_default_allocator()
       │
       ▼
Initialize ROS Support
rclc_support_init()
       │
       ▼
Create Node
rclc_node_init_default()
       │
       ▼
Create Publisher / Subscriber / Timer
rclc_subscription_init_default()
       │
       ▼
Create Executor
rclc_executor_init()
       │
       ▼
Add Subscription to Executor
rclc_executor_add_subscription()
```

Each step has a specific role.

---

# Step 1 — Allocator (Memory Manager)

```
allocator = rcl_get_default_allocator()
```

The **allocator defines how memory ****is allocated and freed** on the microcontroller.

Think of it as a **memory management tool** used internally by ROS.

It provides functions like:

* allocate memory
* free memory
* reallocate memory

---

# Step 2 — Support Initialization

```
rclc_support_init()
```

This step **starts the ROS client system** on the microcontroller.

It initializes:

* ROS context
* middleware communication
* system resources

Without this step, **no ROS objects can be created**.

---

# Step 3 — Node Creation

```
rclc_node_init_default()
```

A **node represents a device inside the ROS network**.

After this step, the ESP32 becomes a **ROS2 node** and can communicate with other nodes.

Example node name:

```
micro_ros_arduino_node
```

---

# Step 4 — Create Communication Interfaces

```
rclc_subscription_init_default()
```

Now we define **how the node communicates**.

A node can create:

* publishers
* subscribers
* timers
* services

Example:

```
Subscriber → receive commands from ROS2
Publisher → send sensor data to ROS2
```

---

# Step 5 — Executor (Event Manager)

```
rclc_executor_init()
```

The **executor manages all callbacks** in the program.

It constantly checks for events such as:

* new messages
* timer triggers
* service requests

When something happens, it runs the correct callback function.

---

# Step 6 — Add Subscription to Executor

```
rclc_executor_add_subscription()
```

This step connects the **subscriber to the executor**.

Now the executor knows:

* Which topic to monitor
* Which callback to execute when data arrives

---

# Runtime Execution (loop)

After initialization, the Arduino program enters the `loop()` function.

```
loop()
   │
   ▼
Executor checks the DDS network
   │
   ▼
Is a new message available?
   │
 ┌─Yes───────────────┐
 │                   ▼
 │         Execute Callback
 │         subscription_callback()
 │
 └─No───────────────►Return to loop()
```

The executor continuously checks for new data.

If a message arrives → the **callback function runs**.

---

# Internal Program Flow

Another way to visualize the system:

```
ESP32 starts
     │
     ▼
Allocator (memory tools)
     │
     ▼
Support (start ROS system)
     │
     ▼
Node created
     │
     ▼
Publishers / Subscribers added
     │
     ▼
Executor running
     │
     ▼
Message arrives
     │
     ▼
Callback executed
```


# Key Concepts to Remember

| Component              | Role                             |
| ---------------------- | -------------------------------- |
| Allocator              | Handles memory operations        |
| Support                | Initializes ROS system           |
| Node                   | Device identity in ROS network   |
| Publisher / Subscriber | Communication interface          |
| Executor               | Runs callbacks when events occur |

---

# Summary

A micro-ROS program follows a **clear initialization and execution flow**:

1. Setup ROS system
2. Create node
3. Define communication interfaces
4. Run executor
5. Process messages through callbacks

Understanding this architecture helps beginners quickly move from **simple LED control** to more advanced robotics applications, such as:

* sensor data publishing
* motor control
* robot navigation
* distributed robotic systems

---

# Learning Goal

This repository focuses on helping beginners **understand the internal logic of micro-ROS**, not just run the code.

Once you understand this flow, you can confidently build **more advanced ROS2 robotic systems using microcontrollers**.

