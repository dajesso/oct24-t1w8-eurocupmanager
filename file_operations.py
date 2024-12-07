import json



def load_matches(path):
    """
    Load matches from JSON File

    parameters: 
        path: Path to the JSON file
    return:
        List of matches or a empty list if a error occurs
    """
    try:
        with open(path) as file:
            matches = json.load(file)

        return matches
    
    except FileNotFoundError:
        print(f'Error: The file "matches "{path}" does not exist')
        return []
    
    except json.decoder.JSONDecodeError:
        print(f'Error: the file "{path}" is not valid json')

    except Exception as e:
        print('fAn unexpected error occured: {e}')
        return []


def save_matches(path, matches_list):
    try:
        with open(path, 'w') as file:
            json.dump(matches_list, file)

        print(f'Matches successfully saved to {path}')


    except PermissionError:
        print(f'Error: Premission denied to write to {path}')
    except Exception as e:
        print(f'An unexpected error occured: {e}')
        