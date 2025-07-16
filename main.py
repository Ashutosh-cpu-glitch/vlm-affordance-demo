from environment import initialize_simulation_environment, acquire_image, reposition_object
from vlm import VisionLanguageProcessor
from affordance import compute_grasp_point, normalize_grasp_coordinates
import pybullet as p

def run_manipulation_pipeline():
    """Execute the VLM-guided robotic manipulation pipeline.

    Integrates object grounding and affordance prediction to simulate a manipulation task,
    demonstrating capabilities relevant to the INRIA Embodied AI project.
    """
    # Initialize simulation and VLM components
    obj_id = initialize_simulation_environment()
    vlm_processor = VisionLanguageProcessor()

    # Capture visual input
    image = acquire_image()

    # Perform object grounding
    text_prompt = "a small cube"
    grounding_prob = vlm_processor.ground_object(image, text_prompt)
    print(f"Object grounding probability for '{text_prompt}': {grounding_prob:.4f}")

    # Predict and normalize grasp point
    grasp_point = compute_grasp_point(image)
    norm_grasp_point = normalize_grasp_coordinates(grasp_point)
    print(f"Predicted grasp point: {grasp_point}, Normalized: {norm_grasp_point}")

    # Execute manipulation
    reposition_object(obj_id, norm_grasp_point)

    # Maintain simulation for visualization
    while True:
        p.stepSimulation()

if __name__ == "__main__":
    run_manipulation_pipeline()