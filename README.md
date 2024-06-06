# QnA-llamaV2-Supportiv

## Description

This project involves fine-tuning the LLaMA model (`abhishek/llama-2-7b-hf-small-shards`) using QLoRA for high-quality text generation. The model is trained on the dataset to generate answers for medical-related questions.

## Assumptions

- The original dataset consisted of 16k rows and 2 columns, however I have coverted it to be compatible with the model. Hence the dataset used for training now has 5k rows and a single column named 'text'.
- Assumed that the input text data is clean and requires minimal preprocessing.

## Approach

1. **Model Selection**: Used the `abhishek/llama-2-7b-hf-small-shards` model from the Hugging Face hub.
2. **Quantization**: Employed QLoRA with 4-bit quantization to fit the model within the GPU memory constraint.
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
  - Capable of generating contextually relevant answers to user's medical questions.

- **Weaknesses**: 
  - Limited to short text generation tasks due to the model size and GPU constraints.
  - Performance may degrade for more complex or lengthy queries due to the reduced precision of quantization.

## Potential Improvements

- **Longer Training**: Increasing the number of training epochs could potentially improve model performance.
- **Data Augmentation**: Adding more diverse and comprehensive datasets can enhance the model's ability to generalize.
- **Enhanced Quantization Techniques**: Investigating advanced quantization methods to balance memory efficiency and model performance.

