# Run on Google colab

from diffusers import StableDiffusionPipeline
import torch

# Load pre-trained stable diffusion model
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float16  # Using float16 for GPU optimization
)

# Move the model to GPU
pipe.to("cuda")

# Example text prompt
prompt = "A futuristic lexus LC500 in the style of Eagle eye on the mars"

# Generate image
image = pipe(prompt, clean_up_tokenization_spaces=False).images[0]

# Save the image
image.save("generated_image.png")

# Display the image
image
