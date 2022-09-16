# Modelling_rover_with_arm
 Modelling of rover_with_arm using solidworks and ROS Gazebo
 
## Rocker Boogie mechanism

https://user-images.githubusercontent.com/90351952/190202272-16989da3-8fe9-4551-bfe9-287c70c64e90.mp4

## INSTRUCTIONS TO LAUNCH SIMULATION IN GAZEBO

PACKAGE NAME ""VISION1
###To run the rover in empty world

#### NEW TERMINAL

````
cd catkin_ws
catkin_make clean && catkin_make
source devel/setup.bash
roslaunch vision1 vision1.launch
````

#### New terminal(ctrl+shift+t) to run the python code to control the rover

cd src/ironman/
python3 teleop_vision1.py

#### New terminal(ctrl+shift+t) to run the python code for autonomous manipulator
python3 mani_grip.py

##### To run the rover in mars terrain#
Go to vision1 package > launch > empty_world.launch> CHANGE THE PATH TO "$(find vision1)/launch/mars_curiosity.world" TO RUN IN MARS TERRAIN

#### NEW TERMINAL

cd catkin_ws
catkin_make clean && catkin_make
source devel/setup.bash
roslaunch vision1 vision1.launch

#### New terminal(ctrl+shift+t) to run the python code to control the rover#

cd src/ironman/
python3 teleop_vision1.py

#### New terminal(ctrl+shift+t) to run the python code for autonomous manipulator#
python3 mani_grip.py

#### New terminal(ctrl+shift+t) 
rviz
