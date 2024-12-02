# Simple vector database for LLM's that stores data in json or in memory. With dictionary feature.

<img src="https://i.imgflip.com/9cc4al.jpg" alt="Description of Image">

## from_documents(documents)
Creates a vector store from a basic list of strings

```
documents = ["First value", "Second Value"]
vector_store = VectorStore.from_documents(documents)
```

## from_dict_inmemory()
Creates a vector store from a dictionary of any type of value. They can then be searched by the keys of the dictionary.

```
dictionary = {"key1" : "value1", "key2" : 5}
vector_store = VectorStore.from_dict_inmemory(dictionary)
```

## from_dict_json()
Creates a vector store from a json string.

## from_dict_json_file()
Creates a vector store from a json file.

```
vector_store = VectorStore.from_dict_json_file("memories.json")
```

## search_strings()
Searches the vector store for strings in case you used `from_documents`. It searches by the strings in the list of strings (`self.documents`)
```
documents = ["First value", "Second Value"]
vector_store = VectorStore.from_documents(documents)

results = vector_store.search("First") # It should return "First Value" as having the highest relevancy.

```


## search_dict()
Searches the vector store for strings in case you used `from_dict_inmemory` or `from_dict_json` or `from_dict_json_file`. It searches by the keys of the dictionary.

```
dictionary = {"key1" : "value1", "key2" : 5}
vector_store = VectorStore.from_dict_inmemory(dictionary)

results = vector_store.search("1") # It should return "value1" as having the highest relevancy.

```

## add_memory_string_inmemory()
Adds a new string to the documents list in memory.


```
vector_store = VectorStore.from_dict_inmemory(dictionary)

results = vector_store.add_memory_string_inmemory("NewMemory")
vetor_store.save_strings_to_json("memories.json")

```

## add_memory_dict_inmemory() 
Adds a new key-value pair to the dictionary in memory.

```
vector_store = VectorStore.from_dict_inmemory(dictionary)

results = vector_store.add_memory_string_inmemory("NewMemory")
vetor_store.save_strings_to_json("memories.json")

```

## save_dict_to_json()
Saves the current dictionary data to a JSON file at the specified filepath.

## save_strings_to_json()
Saves the current documents list to a JSON file at the specified filepath.

## delete_by_dict_key()
Deletes an entry from the dictionary using its key.

## delete_by_value()
Deletes entries from both the dictionary and documents list that match the specified value.


