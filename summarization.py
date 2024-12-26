from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = "Artificial intelligence (AI) is a wide-ranging tool that enables people to rethink how we integrate information, analyze data, and use the resulting insights to improve decision making—and already it is transforming every walk of life. In this report, Darrell West and John Allen discuss AI’s application across a variety of sectors, address issues in its development, and offer recommendations for getting the most out of AI while still protecting important human values."


print(summarizer(ARTICLE, max_length=50, min_length=0, do_sample=False))
