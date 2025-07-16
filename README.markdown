Vision-Language Guided Robotic Manipulation
Project Overview
This repository presents a modular software framework for vision-language model (VLM)-guided robotic manipulation, designed to explore the integration of vision-language processing with robotic control. The project implements a pipeline that leverages the CLIP model for object grounding and PyBullet for simulating manipulation tasks in a tabletop environment. The primary focus is on enabling a robotic system to identify objects using natural language prompts and predict grasp points for interaction, contributing to advancements in intelligent robotic systems.
Scientific Objectives
The project addresses key challenges in robotic manipulation:

Object Grounding: Utilizes CLIP to compute the likelihood of an object's presence in an image based on text prompts, enabling robust object identification.
Affordance Prediction: Implements grasp point prediction as a foundation for understanding object affordances, critical for effective manipulation.
Scalable Design: Organizes the codebase into modular components to support future research, such as multi-view pose estimation or long-horizon task planning.

Repository Structure

environment.py: Configures the PyBullet simulation environment, captures images, and manages object positioning.
vlm.py: Implements object grounding using the CLIP vision-language model.
affordance.py: Computes and normalizes grasp points for robotic manipulation.
main.py: Orchestrates the manipulation pipeline, integrating all components.
requirements.txt: Lists required Python dependencies.

Installation

Clone the repository:git clone <repository-url>
cd vlm-robotic-manipulation


Install dependencies:pip install -r requirements.txt


Run the pipeline:python main.py



Dependencies

Python 3.8+
PyTorch (>=2.0.0)
Transformers (>=4.35.0)
PyBullet (>=3.2.5)
OpenCV (>=4.8.0)
Pillow (>=9.5.0)

Pipeline Description
The pipeline operates as follows:

Environment Setup: Initializes a PyBullet simulation with a tabletop and a target cube, visualized via a graphical interface.
Image Acquisition: Captures an RGB image from a simulated camera to serve as input for object grounding.
Object Grounding: Employs CLIP to calculate the probability of a target object (e.g., "a small cube") in the image.
Grasp Point Prediction: Estimates a grasp point (currently simplified to the image center) as a baseline for affordance prediction.
Manipulation Execution: Repositions the object in the simulation to mimic a robotic grasp action.

Experimental Setup
The project uses a simulated tabletop environment with a single object (a cube) to demonstrate the pipeline. The CLIP model processes images and text prompts to ground objects, while PyBullet simulates robotic interactions. The modular design ensures reproducibility and ease of modification for further experimentation.
Future Research Directions
To advance the project’s scientific contributions, potential extensions include:

Multi-view image processing for accurate 3D object pose estimation.
Fine-tuning CLIP on video demonstration datasets to enhance affordance prediction.
Optimizing inference speed using quantized models for real-time robotic applications.
Incorporating imitation learning to support long-horizon manipulation tasks.
Extending to dexterous manipulation in complex, cluttered environments.

Author
Ashutosh Dadhich
This project serves as a foundation for exploring the intersection of vision-language models and robotic manipulation, with applications in autonomous systems and human-robot interaction. Feedback and suggestions for further development are welcome.
