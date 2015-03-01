def bag_of_words(text):
  """Returns bag-of-words representation of the input text.

  Args:
    text: A string containing the text.

  Returns:
    A dictionary of strings to integers.
  """
  bag = {}
  for word in text.lower().split():
    bag[word] = bag.get(word, 0) + 1
  return bag
