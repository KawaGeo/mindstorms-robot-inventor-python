# Blast - Basics

# Imports as needed
from mindstorms import MSHub, Motor, MotorPair, DistanceSensor
from mindstorms.control import wait_for_seconds

def calibrate_blast(motor):
    # Configure the motor
    motor.set_stall_detection(True)
    motor.set_stop_action('brake')

    # Perform the motor to the rest position. (experimental verson)
    motor.run_for_seconds(3, 100)
    motor.run_for_rotations(-2, 50)


# Create objects.
hub = MSHub()
torso_motor = Motor('D')
wheels = MotorPair('C', 'A')
arm_motor = Motor('B')
distance = DistanceSensor('F')

# Configure the objects
hub.status_light.on('red')
hub.light_matrix.set_orientation('left')
hub.light_matrix.show_image('SKULL') # in place of the animation

# Execute actions
calibrate_blast(torso_motor)
wheels.start(0, 20)
wait_for_seconds(0.5)
torso_motor.run_for_rotations(1.8, 100)
distance.light_up_all(100)
wait_for_seconds(1)
wheels.stop()
distance.light_up_all(0)