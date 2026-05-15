import random

print("Generative Text Model Program")

start_words = ["Artificial Intelligence", "Machine Learning", "Deep Learning"]
actions = ["is changing", "is improving", "is helping"]
fields = ["education", "healthcare", "business", "transportation"]
endings = ["by making systems smarter.", "through automation.", "with data-driven decisions."]

sentence = (
    random.choice(start_words) + " " +
    random.choice(actions) + " " +
    random.choice(fields) + " " +
    random.choice(endings)
)

print("Generated Text:")
print(sentence)
