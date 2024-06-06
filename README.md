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

## Example Interactions:

- **Prompt 1:**  How to treat Glaucoma?
- **Answer:**  The goal of treatment is to reduce pressure in the eye to a level that will prevent damage to the optic nerve and vision loss. Treatment may include medicines, laser surgery, conventional surgery, or a combination of these treatments. The type of treatment that is best for you will depend on the type of glaucoma you have, how severe it is, and whether you have other eye diseases. Your ophthalmologist will work with you to determine the best treatment for your condition.    Medicines - Medicines used to treat glaucoma work by either reducing the amount of fluid in the eye or by improving the flow through the drainage angle. These medicines are taken by mouth or applied directly to the eye.    Laser surgery - Laser surgery is used to

- **Prompt 2:** What is Osteoporosis?
- **Answer:**  Osteoporosis is a disease that causes bones to become weak and brittle. It is a silent disease because there are no symptoms. Osteoporosis is called the "silent disease" because it is not detected until a bone breaks. Osteoporosis is a major health problem in the United States. It affects 10 million Americans, including 1 million men. It is most common in women over age 50. Osteoporosis is a major cause of broken bones in older people. It is also a major cause of disability in older people. Osteoporosis is a major cause of broken bones in older people. It is also a major cause of disability in older people. Osteoporosis is a major cause of broken bones in

- **Prompt 3:** What is Osteoporosis?
- **Answer:** Signs and symptoms of lung cancer include       -  A cough that doesn't go away or gets worse over time    -  Chest pain    -  Shortness of breath    -  Wheezing    -  Hoarseness    -  Trouble swallowing    -  Weight loss for no known reason    -  Loss of appetite    -  Fatigue    -  Coughing up blood    -  Chest infections that keep coming back       Lung cancer can cause other signs and symptoms. Other conditions can cause the same signs and symptoms. It's important to see your doctor if you have any of these problems. Only a doctor can make a diagnosis.    NIH: National Cancer Institute    NIH: National Institute of Environmental
