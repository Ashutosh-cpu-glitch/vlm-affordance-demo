# Vision-Language Guided Robotic Manipulation

## Project Overview
This repository presents a modular software framework for vision-language model (VLM)-guided robotic manipulation, developed to demonstrate my technical expertise for the INRIA PhD position in the Willow research team. The project implements a pipeline for object grounding and grasp point prediction using the CLIP model and PyBullet simulation environment. It aligns with the INRIA Embodied AI project's objectives, specifically in leveraging VLMs for object grounding and affordance prediction in robotic manipulation tasks.

## Relevance to INRIA PhD Project
This project addresses key components of the INRIA Embodied AI project:
- **Object Grounding**: The `vlm.py` module employs CLIP to compute the likelihood of an object's presence based on text prompts, supporting precise object identification as outlined in the INRIA project.
- **Affordance Prediction**: The `affordance.py` module predicts grasp points, providing a foundation for spatial affordance estimation, a core focus of the INRIA project.
- **Modular Design**: The codebase is organized into distinct modules (`environment.py`, `vlm.py`, `affordance.py`, `main.py`) to facilitate scalability and future extensions, such as multi-view pose estimation or fine-tuning VLMs on video demonstrations.
- **Research Potential**: The framework is extensible for exploring long-horizon tasks and inference optimization, aligning with the INRIA project's goals of generalization and real-time performance.

## Repository Structure
- `environment.py`: Configures the PyBullet simulation environment, captures images, and handles object positioning.
- `vlm.py`: Implements object grounding using the CLIP vision-language model.
- `affordance.py`: Computes and normalizes grasp points for manipulation.
- `main.py`: Orchestrates the manipulation pipeline, integrating all components.
- `requirements.txt`: Specifies required Python dependencies.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd vlm-robotic-manipulation
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the pipeline:
   ```bash
   python main.py
   ```

## Dependencies
- Python 3.8+
- PyTorch
- Transformers (Hugging Face)
- PyBullet
- OpenCV
- Pillow

## Pipeline Description
The pipeline operates as follows:
1. **Environment Initialization**: Sets up a PyBullet simulation with a tabletop and a target cube, visualized via a graphical interface.
2. **Image Acquisition**: Captures an RGB image from a simulated camera.
3. **Object Grounding**: Uses CLIP to compute the probability of the target object (e.g., "a small cube") in the image.
4. **Grasp Point Prediction**: Estimates a grasp point (simplified to the image center as a baseline).
5. **Manipulation Execution**: Repositions the object to simulate a grasp action.

## Future Enhancements
To align with the INRIA project's long-term goals, potential extensions include:
- Incorporating multi-view image processing for accurate 3D pose estimation.
- Fine-tuning CLIP on video demonstration datasets to enhance affordance prediction.
- Optimizing inference speed using quantized models (e.g., TinyVLA).
- Extending to long-horizon tasks via imitation learning from human demonstrations.
- Supporting dexterous manipulation in cluttered environments.

## Author
Ashutosh Dadhich
