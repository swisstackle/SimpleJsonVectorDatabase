# Simple vector database for LLM's that stores data in json or in memory. With dictionary feature.

<img src="https://i.imgflip.com/9cc4al.jpg" alt="Description of Image">

## from_documents()
Creates a vector store from a basic list of strings

## from_dict_inmemory()
Creates a vector store from a dictionary of list of strings. They can then be searched by the keys of the dictionary.

## from_dict_json()
Creates a vector store from a json string.

## from_dict_json_file()
Creates a vector store from a json file.

## search_strings()
Searches the vector store for strings in case you used from_documents.

## search_dict()
Searches the vector store for strings in case you used from_dict_inmemory or from_dict_json or from_dict_json_file.

## add_memory_string_inmemory()
Adds a new string to the documents list in memory.

## add_memory_dict_inmemory() 
Adds a new key-value pair to the dictionary in memory.

## save_dict_to_json()
Saves the current dictionary data to a JSON file at the specified filepath.

## save_strings_to_json()
Saves the current documents list to a JSON file at the specified filepath.

## delete_by_dict_key()
Deletes an entry from the dictionary using its key.

## delete_by_value()
Deletes entries from both the dictionary and documents list that match the specified value.

