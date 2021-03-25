
SAFE_CHARACTERS = {' ': '_',
                   'á': 'a',
                   'é': 'e',
                   'í': 'i',
                   'ó': 'o',
                   'ú': 'u',
                   'ñ': 'ny'
                  }

def get_nice_path(string):
    string = string.lower()
    for character, safe_character in SAFE_CHARACTERS.items():
        string = string.replace(character, safe_character)
    return string
