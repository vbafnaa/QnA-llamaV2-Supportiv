import pandas as pd

df = pd.read_csv('Book1.csv') # Use dataset

# Select the "Question" and "Answer" columns
df = df[['question', 'answer']]

# Convert the columns into a format for LLAMA2 Fine-tuning (Basically Prompt = Question and Response = Answer)
formatted_data = []
for index, row in df.iterrows():
    prompt = str(row['question'])
    response = str(row['answer'])
    # prompt=prompt.replace("Optimus Prime", "Abhyaan")
    # prompt=prompt.replace("Optimus", "Abhyaan")
    # formatted_data.append(f'<s>[INST] <<SYS>> Answer in Optimus Prime\'s way of speech <</SYS>> {prompt} [/INST] {response} </s>')
    formatted_data.append(f'<s>[INST] <<SYS>> Answer the Question <</SYS>> {prompt} [/INST] {response} </s>')
    # formatted_data.append(f'<s>[INST] <<SYS>> Below Given is an example of how Optimus Prime Talks. Use a similar style to reply. \n### Instruction: {prompt}\n### Response: {response}.')

df=pd.DataFrame(formatted_data,columns=['text'])
df.to_csv('train2.csv', index=False) # Use this dataset for training