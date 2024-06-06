import pandas as pd

df = pd.read_csv('Book1.csv') # Use dataset

# Select the "Question" and "Answer" columns
df = df[['question', 'answer']]

# Convert the columns into a format for LLAMA2 Fine-tuning (Basically Prompt = Question and Response = Answer)
formatted_data = []
for index, row in df.iterrows():
    prompt = str(row['question'])
    response = str(row['answer'])
    formatted_data.append(f'<s>[INST] <<SYS>> Answer the Question <</SYS>> {prompt} [/INST] {response} </s>')

df=pd.DataFrame(formatted_data,columns=['text'])
df.to_csv('train2.csv', index=False) # Use this dataset for training