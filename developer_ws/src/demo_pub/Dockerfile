FROM arm64v8/ros
ARG ROS2_DISTRO=humble
COPY . /app
RUN make /app/demo_pub
# CMD echo "Starting Publisher for ROS 2"
RUN /bin/bash -c 'echo $ROS2_DISTRO'
RUN /bin/bash -c 'source /opt/ros/$ROS2_DISTRO/setup.bash;'

#RUN [source, "/opt/ros/humble/setup.bash"]
#RUN /bin/bash -c 'source $HOME/.bashrc; echo $HOME'

#ENTRYPOINT ["ros2", "/app/demo_pub/demo_pub_node.py"]
#ENTRYPOINT "/bin/bash"