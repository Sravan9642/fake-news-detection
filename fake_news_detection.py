import pandas as pd

# Load data
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

print("Fake news shape:", fake.shape)
print("True news shape:", true.shape)
