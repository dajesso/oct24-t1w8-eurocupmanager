from file_operations import load_matches, save_matches
from match_operations import display_matches

spam = load_matches("matches.json")

spam[0]['Score A'] = 42

save_matches('debug.json', spam)

display_matches(spam)