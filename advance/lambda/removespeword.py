# remove specific words from a given list using lambda.

def func(original_words,remove_words):
    filtered_word = list(filter(lambda word : word not in remove_words,original_words))
    print("after remove",filtered_word)

original_words = ["meow","cat","dog","elephant","tiger"]
remove_words = ["meow"]
print("original list",original_words)
print("removed list",remove_words)
func(original_words,remove_words)
