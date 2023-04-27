import os                                                                                                                                                                                   
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader                                                                                                                               

os.environ["OPENAI_API_KEY"] = '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'                                                                                                                                         

def tune():
    documents = SimpleDirectoryReader('data').load_data()
    index = GPTSimpleVectorIndex.from_documents(documents)
    index.save_to_disk('index.json')

def ask_ai():
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    while True: 
        query = input("What do you want to ask? ")
        response = index.query(query)
        print('Response:')
        print(response.response)

tune()
ask_ai()