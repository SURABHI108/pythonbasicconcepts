import re
 
sentance = '''hi how are you?? how can i help you. 
whre are you?? where i pick up you.'''

sentence_pattern = re.compile(r'(.*?\.)(\s|$)', re.DOTALL)
matches = sentence_pattern.findall(sentance)
sentences = [match[0] for match in matches]
print(sentences)

word_pattern = re.compile(r"([\w\-']+)([\s,.])?")
for sentence in sentences:
    matches_word = word_pattern.findall(sentence)
    words = [match[0] for match in matches_word]
    print(words)