# Building a Robot: ROS2 Pub-Sub

Sample to demonstrate how to create a [ros2](https://docs.ros.org/en/galactic/index.html) Publisher and Subscriber.
The sample is derived from ROS2 examples available here: [ROS Tutorials](https://github.com/ros2/examples)

## Assumptions

- Tested on ROS2 foxy or Galactic build.
- Tested on a Linux (Ubuntu ARM64 20.04.03) build so may not work on Windows or MacOS
- Both Publisher and Listener are communicating over `demo_topic`, this can be changed or parameterized in the packages.

## Build Instructions

Use `colcon` to build and then source using the `setup.bash` in Install folder created in your ROS2 workspace.

```bash
# ensure any dependencies are managed before you build
rosdep install -i --from-path src --rosdistro galactic -y 
# build the packages 
colon build
# source install the packages into ros2
. install/setup.bash
```

## Running the Sample in a ROS2 environment

Use the following commands from the root of your ROS2 workspace
**NOTE:** Make sure you have sourced ros2 in the terminal, else all commands will fail:

```bash
source ~/<your ros2 installation>/setup.bash
```

In a new terminal start the Publisher:

```bash
[ROS2 Workspace Root]>> ros2 run demo_pub demo_pub_node

# Expected Output
[INFO] [1641630963.715973530] [demo_publisher]: Publishing: Hello World: 0
[INFO] [1641630964.203379204] [demo_publisher]: Publishing: Hello World: 1
[INFO] [1641630964.706833762] [demo_publisher]: Publishing: Hello World: 2
```

In another terminal start the Subscriber:

```bash
[ROS2 Workspace Root]>> ros2 run demo_sub demo_sub_node

# Expected Output
[INFO] [1641631802.220679292] [demo_subscriber]: Message received Hello World: 0
[INFO] [1641631802.707940321] [demo_subscriber]: Message received Hello World: 1
[INFO] [1641631803.213551280] [demo_subscriber]: Message received Hello World: 2
```
