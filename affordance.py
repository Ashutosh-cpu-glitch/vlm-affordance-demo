import numpy as np

def compute_grasp_point(image):
    """Estimate a grasp point for an object in the image.

    Implements a simplified grasp point prediction by selecting the image center,
    serving as a baseline for affordance prediction as described in the INRIA project.

    Args:
        image (PIL.Image): Input image containing the target object.

    Returns:
        tuple: (x, y) pixel coordinates of the predicted grasp point.
    """
    height, width, _ = np.array(image).shape
    grasp_point = (width // 2, height // 2)  # Simplified: use image center
    return grasp_point

def normalize_grasp_coordinates(grasp_point, image_width=640, image_height=480):
    """Normalize grasp point coordinates to simulation space.

    Converts pixel coordinates to simulation coordinates for robotic manipulation.

    Args:
        grasp_point (tuple): (x, y) pixel coordinates.
        image_width (int): Width of the input image.
        image_height (int): Height of the input image.

    Returns:
        list: [x, y, z] normalized coordinates in simulation space.
    """
    x, y = grasp_point
    return [x / image_width, y / image_height, 0.8]  # Fixed z for tabletop