# deep learnihgn lib
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch.nn.functional as F

#functional
import pandas as pd
import tqdm
import numpy as np
import matplotlib.pyplot as plt
from transformers import pipeline


DATA_DIR = "./data/product_review.csv"


#data reading
df = pd.read_csv(DATA_DIR)

#data preprocessing
df = df.drop("product" , axis=1)
df = df.drop("title" , axis=1)
df["date"] = [i[33:] for i in df["date"]]
df["date"] = [i[3:] if "on " in i else i for i in df["date"]]
df["date"] = pd.to_datetime(df["date"])
df = df.dropna()

# to remove non integer data 
def remove_non_string_data(df):
    df = df[df['body'].apply(lambda x: isinstance(x, str))]
    return df

# MODEL
sentiment_analysis = pipeline("sentiment-analysis",model="siebert/sentiment-roberta-large-english")
model_name = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


# sentiment functionalities 
def analyze_sentiment(text):
    '''function to return sentiments mapping to given text'''
    inputs = tokenizer(text , return_tensors="pt")
    
    outputs = model(**inputs)
    probs = F.softmax(outputs.logits , dim=1)
    sentiment = torch.argmax(probs , dim=-1).item()
    sentiment_map = {0 : "negative" , 1 : "neutral" , 2  :"positive"}
    return sentiment_map[sentiment]

def senti_score(dataset):
    '''adding labels column in the dataframe for the respective text'''
    sentiment_mapper = {"positive" : 1 , "neutral" : 0 , "negative" : -1}
    list_of_senti = []

    for i in tqdm.tqdm(range(len(df['body']))):
        try:
            text = dataset["body"][i]
        except KeyError:
            pass
    
        if((len(text)) >= 514):
            text = text[:514]
        sentiment = analyze_sentiment(text=text)
        senti_value = sentiment_mapper[sentiment]
        list_of_senti.append(senti_value)
    
    return list_of_senti

# creating sentiment lables 
df["labels"] = senti_score(dataset=df)

#resulting values from rating and lables rating * labels = final value
df["values"] = df["rating"] * df["labels"]

# extracting imp feature from the original dataset 
df.sort_values(by="date" , inplace=True)
df_grp = df.groupby('date')['values'].sum().reset_index()
df_grp_json = df_grp.to_json()

# jsonify the data and return the json
json_file_path = 'amazon_review.json'

with open(json_file_path , 'w') as json_file:
    json_file.write(df_grp_json)

