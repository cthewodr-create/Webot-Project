"""my_controller controller."""

#"""
# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor

#"""my_controller_FN controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
"""
from controller import Robot, Motor, DistanceSensor
from controller import Keyboard

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
MAX_SPEED = 6.28
setSpeed = MAX_SPEED

# ________ set up Keyboard______
keyboard = robot.getKeyboard()
keyboard.enable(timestep)


ps = []
psNames = ['ps0', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7']

for i in range(8):
    ps.append(robot.getDevice(psNames[i]))
    ps[i].enable(timestep)

#__________________Set motor____________________
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

#__________________ Velocities/Motion functions ___________
def vForward(robot):
    leftMotor.setVelocity(setSpeed)
    rightMotor.setVelocity(setSpeed)

def vBackwards(robot):
    leftMotor.setVelocity(-setSpeed)
    rightMotor.setVelocity(-setSpeed)

def stop(robot):
    leftMotor.setVelocity(0.0)
    rightMotor.setVelocity(0.0)

def turnRigth(robot):
    leftMotor.setVelocity(setSpeed)
    rightMotor.setVelocity(-setSpeed)

def rutnLeft(robot):
    leftMotor.setVelocity(-setSpeed)
    rightMotor.setVelocity(setSpeed)

#____________________Accumulator varible ______________

obstacle_counter = 0
#_______________________________________________________
while robot.step(timestep) != -1:

#__________________ To set initial Velocity ___________
    key = keyboard.getKey()
    if key == ord('A'):
        setSpeed = MAX_SPEED * 2
        print(setSpeed)
    elif key == ord("X"):
        setSpeed = MAX_SPEED * 0.5
        print(setSpeed)
    else:
        setSpeed = MAX_SPEED
        print(setSpeed)
    leftMotor.setVelocity(setSpeed)
    rightMotor.setVelocity(setSpeed)
#_________________________________________________


    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)

"""

# Enter here exit cleanup code.



from controller import Robot, Motor, DistanceSensor
from controller import Keyboard
import random


# create the Robot instance.
robot = Robot()
# get the time step of the current world.
time_step = int(robot.getBasicTimeStep())
MAX_SPEED = 3.14
setSpeed = MAX_SPEED
keyboard = robot.getKeyboard()
keyboard.enable(time_step)


ps = []
psNames = [
    'ps0', 'ps1', 'ps2', 'ps3',
    'ps4', 'ps5', 'ps6', 'ps7'
]

for i in range(8):
    ps.append(robot.getDevice(psNames[i]))
    ps[i].enable(time_step)

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)
startTime = robot.getTime()


obstacle_counter = 0
avoid_obstacle = False

def simulationResults(endTime):
    print("The Simulation has finished")
    print("Here are your results from your simulation: ")
    print("Speed: ", setSpeed) #MAX_SPEED
    run_time = endTime - startTime
    print("Simulation Time: ", run_time)
    print("Obstacles Avoided: ", obstacle_counter)

def vForward(robot):
    leftMotor.setVelocity(setSpeed)
    rightMotor.setVelocity(setSpeed)

def vBackwards(robot):
    leftMotor.setVelocity(-setSpeed)
    rightMotor.setVelocity(-setSpeed)

def stop(robot):
    leftMotor.setVelocity(0.0)
    rightMotor.setVelocity(0.0)


def turnRight(robot):
    leftMotor.setVelocity(0.5 * setSpeed)
    rightMotor.setVelocity(-0.5 * setSpeed)

def turnLeft(robot):
    leftMotor.setVelocity(-0.5 * setSpeed)
    rightMotor.setVelocity(0.5 * setSpeed)


while robot.step(time_step) != -1:

    key = keyboard.getKey()
    if key == ord('A'):
        setSpeed = MAX_SPEED * 2

    elif key == ord("X"):
        setSpeed = MAX_SPEED * 0.5

    psValues = []
    for i in range(8):
        psValues.append(ps[i].getValue())

    #obstacles = psValues[0] > 100.0 or psValues[1] > 100.0 or psValues[2] > 100.0 or psValues[5] > 100.0 or psValues[6] > 100.0 or psValues[7] > 100.0
    left_obstacle = psValues[5] > 425.0 or psValues[6] > 425.0 or psValues[7] > 425.0
    right_obstacle = psValues[0] > 425.0 or psValues[1] > 425.0 or psValues[2] > 425.0

    #leftSpeed = 0.5 * setSpeed
    #rightSpeed = 0.5 * setSpeed

    #if setSpeed > MAX_SPEED:


    """if psValues[5] > 200.0 or psValues[6] > 200.0 or psValues[7] > 200.0:
        leftMotor.setVelocity(0.0)
        rightMotor.setVelocity(0.0)
        #leftSpeed = 0.5 * MAX_SPEED
        rightSpeed = -0.5 * MAX_SPEED
        leftMotor.setVelocity(leftSpeed)
        rightMotor.setVelocity(0.5 * MAX_SPEED)

    elif psValues[0] > 200.0 or psValues[1] > 200.0 or psValues[2] > 200.0:
        # turn left
        leftMotor.setVelocity(0.0)
        rightMotor.setVelocity(0.0)
        leftSpeed = -0.5 * MAX_SPEED
        #rightSpeed = 0.5 * MAX_SPEED
        leftMotor.setVelocity(0.5 * MAX_SPEED)
        rightMotor.setVelocity(rightSpeed)

    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)"""

    """
    #for i in ps:
def obstacle_detect(list):
    first = list[0]
    rest_of_sensors = list[1:]
    if first.getValue() > 100:
        rest_of_sensors.disable()
        if first in right_obstacle:
            turnLeft(robot)
            avoid_obstacle = True
        if first in left_obstacle:
            turnRight(robot)
            avoid_obstacle = True
    else:
        return obstacle_detect(rest_of_sensors)

obstacle_detect(ps)
    """
    if left_obstacle:
        turnRight(robot)


    if right_obstacle:
        turnLeft(robot)


    else:
        vForward(robot)

    if left_obstacle or right_obstacle:
        avoid_obstacle = True


    elif avoid_obstacle:
        obstacle_counter += 1
        print("Number of Obstacles: ", obstacle_counter)
        avoid_obstacle = False

    obstacle_end = random.randint(21, 30)
    if obstacle_counter == obstacle_end:
        stop(robot)
        #leftMotor.setVelocity(0.0)
        #rightMotor.setVelocity(0.0)
        endTime = robot.getTime()
        simulationResults(endTime)
        break




"""
from controller import Robot, Motor, DistanceSensor

robot = Robot()
time_step = int(robot.getBasicTimeStep())
MAX_SPEED = 10

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

while robot.step(time_step) != -1:
    leftMotor.setVelocity(MAX_SPEED)
    rightMotor.setVelocity(MAX_SPEED)
"""