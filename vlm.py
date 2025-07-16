import torch
from transformers import CLIPProcessor, CLIPModel

class VisionLanguageProcessor:
    """Class for processing vision-language inputs using a pre-trained CLIP model.

    Implements object grounding by computing similarity between an image and a text prompt,
    supporting the INRIA project's goal of using VLMs for object identification in robotic tasks.
    """
    def __init__(self, model_name="openai/clip-vit-base-patch32"):
        """Initialize the CLIP model and processor.

        Args:
            model_name (str): Pre-trained CLIP model identifier (default: openai/clip-vit-base-patch32).
        """
        self.model = CLIPModel.from_pretrained(model_name)  # Load pre-trained CLIP model
        self.processor = CLIPProcessor.from_pretrained(model_name)  # Load corresponding processor

    def ground_object(self, image, text_prompt):
        """Ground an object in the image using a text prompt.

        Computes the probability that the image contains the object described by the text prompt,
        leveraging CLIP's vision-language alignment.

        Args:
            image (PIL.Image): Input image from the simulation.
            text_prompt (str): Text description of the target object (e.g., 'a small cube').

        Returns:
            float: Probability score indicating object presence.
        """
        inputs = self.processor(text=[text_prompt], images=image, return_tensors="pt", padding=True)
        with torch.no_grad():  # Disable gradient computation for inference
            outputs = self.model(**inputs)
        logits_per_image = outputs.logits_per_image
        probs = logits_per_image.softmax(dim=1)  # Convert logits to probabilities
        return probs.item()