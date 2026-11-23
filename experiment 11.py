import pandas as pd
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("experiment_11_prompting_techniques.csv")
positive_words = {"quick", "perfectly", "excellent", "helpful", "love", "early", "great"}
negative_words = {"poor", "dull", "stopped", "broken", "slow", "unavailable"}
def sentiment_demo(sentence):
words = set(sentence.lower().replace(".", "").replace(",", "").split())
score = len(words & positive_words) - len(words & negative_words)
return "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"
def construct_prompt(row):
role = row["Role"]
task = row["Task"]
text = row["Input_Text"]
technique = row["Technique"]
if technique == "Zero-Shot":
return f"You are a {role}. {task}: {text}"
if technique == "One-Shot":
return (f"You are a {role}. {task}. Example: "
f"{row['Example_Input']} -> {row['Example_Output']}. New input: {text}")
if technique == "Few-Shot":
return (f"You are a {role}. {task}. Examples: "
"Excellent service -> Positive; Poor quality -> Negative. "
f"New input: {text}")
return f"Act as a {role}. {task}: {text}"
print("----- ROLE-BASED AND EXAMPLE-BASED PROMPTING -----")
for _, row in df.iterrows():
prompt = construct_prompt(row)
if "sentiment" in row["Task"].lower():
response = sentiment_demo(row["Input_Text"])
elif "priority" in row["Task"].lower():
response = "High" if "unavailable" in row["Input_Text"].lower() else "Low"
else:
response = "Suggested rewrite: Please share the project file at your earliest
convenience."
print(f"\nID: {row['Example_ID']} | Technique: {row['Technique']}")
print("Constructed prompt:", prompt)
print("Python demonstration response:", response)
print("\nDemonstration completed. Responses use predefined Python rules, not a live
LLM.")
Output
----- ROLE-BASED AND EXAMPLE-BASED PROMPTING -----
ID: T101 | Technique: Zero-Shot
Constructed prompt: You are a Sentiment analyst. Classify review sentiment: The delivery
was quick and the product works perfectly.
Python demonstration response: Positive
ID: T102 | Technique: One-Shot
Constructed prompt: You are a Customer feedback analyst. Classify review sentiment.
Example: The service was excellent and helpful. -> Positive. New input: The battery
stopped working after one day.
Python demonstration response: Negative
ID: T103 | Technique: Few-Shot
Constructed prompt: You are a Product review analyst. Classify review sentiment.
Examples: Excellent service -> Positive; Poor quality -> Negative. New input: The camera
quality is poor and the screen is dull.
Python demonstration response: Negative
ID: T104 | Technique: Role-Based
Constructed prompt: Act as a Academic writing tutor. Rewrite the sentence professionally:
hey, send me the project file now
Python demonstration response: Suggested rewrite: Please share the project file at your
earliest convenience.
ID: T105 | Technique: Few-Shot
Constructed prompt: You are a Support analyst. Classify ticket priority. Examples:
Excellent service -> Positive; Poor quality -> Negative. New input: The application is
unavailable for every user.
Python demonstration response: High
Demonstration completed. Responses use predefined Python rules, not a live LLM