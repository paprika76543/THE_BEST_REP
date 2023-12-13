from transformers import pipeline

discrim = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")

target_phrase = input('\n[+] Введите фразу для оценки  >>> ')

discrim(target_phrase)

print(discrim(target_phrase))