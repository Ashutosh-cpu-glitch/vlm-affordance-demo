import pybullet as p
import pybullet_data
import numpy as np
from PIL import Image

def initialize_simulation_environment():
    """Initialize a PyBullet simulation environment for robotic manipulation.

    Configures a graphical simulation with a ground plane, table, and a target object (cube).
    The environment is designed to emulate a tabletop manipulation scenario, aligning with
    the INRIA project's focus on robotic manipulation tasks.

    Returns:
        int: Object ID of the target cube for manipulation.
    """
    p.connect(p.GUI)  # Enable graphical interface for visualization
    p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Access PyBullet's URDF assets
    p.setGravity(0, 0, -9.81)  # Set realistic gravitational force
    p.loadURDF("plane.urdf")  # Load ground plane
    p.loadURDF("table/table.urdf", [0, 0, 0])  # Load table at origin
    obj_id = p.loadURDF("cube_small.urdf", [0.5, 0, 0.8])  # Load small cube as target
    return obj_id

def acquire_image():
    """Capture an RGB image from a simulated camera in PyBullet.

    Configures a camera with a fixed viewpoint to capture the scene, simulating
    visual input for object grounding tasks as described in the INRIA project.

    Returns:
        PIL.Image: RGB image of the simulation environment.
    """
    width, height = 640, 480
    view_matrix = p.computeViewMatrix([0, -2, 1], [0, 0, 0.5], [0, 0, 1])  # Camera positioned above table
    proj_matrix = p.computeProjectionMatrixFOV(fov=60, aspect=width/height, nearVal=0.1, farVal=100.0)
    _, _, rgb, _, _ = p.getCameraImage(width, height, view_matrix, proj_matrix)
    rgb = np.reshape(rgb, (height, width, 4))[:, :, :3]  # Extract RGB channels
    return Image.fromarray(rgb)

def reposition_object(obj_id, position):
    """Reposition the target object in the simulation.

    Updates the object's position to simulate a robotic grasp action, supporting
    the evaluation of predicted grasp points.

    Args:
        obj_id (int): Object ID of the target.
        position (list): [x, y, z] coordinates in simulation space.
    """
    p.resetBasePositionAndOrientation(obj_id, position, [0, 0, 0, 1])  # Reset orientation to default