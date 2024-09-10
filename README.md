# AI Art Generator 🎨
This project utilizes Stable Diffusion to generate unique AI-generated artwork based on text descriptions. It leverages PyTorch and Hugging Face's diffusers to run the model, either locally (if system resources allow) or on a cloud platform like Google Colab for better performance.

## Features
- Text-to-Image Generation: Generate images from descriptive text prompts.
- Stable Diffusion: Uses pre-trained models to produce high-quality, detailed images.
- Cloud and Local Support: Run the model locally (for high-resource systems) or on cloud platforms (for better performance).

## Setup Instructions

### Local Environment (for advanced users)

1. Clone the repository:

```bash 
git clone https://github.com/your-repo-name/ai-art-generator.git
cd ai-art-generator
```

2. Install dependencies:

```bash
poetry install
```

3. Run the AI Art Generator:

```bash
poetry run python ai_art_generator/ai_art_generator.py
```

### Cloud Setup (Recommended)

1. Open Google Colab.
2. Install the required dependencies:

```bash
!pip install torch torchvision diffusers transformers accelerate
```

3. Copy the project code and run the cells to generate your AI artwork.

## Requirements
- Python 3.8+
- PyTorch
- Hugging Face's Diffusers Library

### Notes
Cloud environments like Google Colab are recommended for running this model due to the high memory and processing power required.
