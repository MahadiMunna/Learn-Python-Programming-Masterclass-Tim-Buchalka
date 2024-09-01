text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""


prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.

text_in_set = set(word for word in text.split())
result = text_in_set.intersection(prepositions)
print(result)