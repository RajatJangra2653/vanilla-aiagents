from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
client = SearchClient(endpoint=os.getenv('AZURE_COGNITIVE_SEARCH_ENDPOINT'), index_name="<Your_Index>", credential=AzureKeyCredential(os.getenv('AZURE_COGNITIVE_SEARCH_KEY')))
results = client.search("Azure AI services")
for result in results:
print(result)