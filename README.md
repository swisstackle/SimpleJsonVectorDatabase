# Simple vector database for LLM's that stores data in json or in memory.

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