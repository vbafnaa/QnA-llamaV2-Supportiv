# QnA-llamaV2-Supportiv

## Description

This project involves fine-tuning the LLaMA model (`abhishek/llama-2-7b-hf-small-shards`) using QLoRA for efficient and high-quality text generation. The model is trained on a custom dataset to generate answers for medical-related questions.

## Assumptions

- The dataset used for training consists of 5000 rows with a single column named 'text'.
- The model training is performed on a GPU with 13GB of memory.
- We assume that the input text data is clean and requires minimal preprocessing.

## Approach

1. **Model Selection**: We use the `abhishek/llama-2-7b-hf-small-shards` model from the Hugging Face hub.
2. **Quantization**: Employ QLoRA with 4-bit quantization to fit the model within the 13GB GPU memory constraint.
3. **Training Configuration**: 
   - Batch size of 2
   - Gradient accumulation steps set to 4
   - Gradient checkpointing enabled
   - Learning rate of 2e-4
   - Constant learning rate schedule

4. **Training**: The model is fine-tuned for 1 epoch due to memory constraints, with checkpoints and logs saved every 75 steps.

## Model Performance

- **Strengths**: 
  - Efficient use of GPU memory due to 4-bit quantization.
  - Capable of generating coherent and contextually relevant answers to medical questions.

- **Weaknesses**: 
  - Limited to short text generation tasks due to the model size and GPU constraints.
  - Performance may degrade for more complex or lengthy queries due to the reduced precision of quantization.

## Potential Improvements

- **Longer Training**: Increasing the number of training epochs could potentially improve model performance.
- **Data Augmentation**: Adding more diverse and comprehensive datasets can enhance the model's ability to generalize.
- **Model Architecture**: Experimenting with different model architectures or fine-tuning larger models on more powerful hardware.
- **Enhanced Quantization Techniques**: Investigating advanced quantization methods to balance memory efficiency and model performance.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/vbafnaa/QnA-llamaV2-Supportiv.git
   cd QnA-llamaV2-Supportiv
