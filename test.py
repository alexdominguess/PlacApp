from cloudant import Cloudant
from cloudant.result import Result
import json

client = Cloudant.iam("e75ee703-7ad3-46f2-91cd-f77a6a0d2094-bluemix", "vb5tLFvKQ_fpWBiSG-5lbKnU2XaMp2VeOryqTXTll7wn")
client.connect()

my_db = client['maindb']


sample_data = [
   [1, "one two three", "boiling", 100],
   [2, "two", "hot", 40],
   [3, "three", "warm", 20],
   [4, "four", "cold", 10],
   [5, "five", "freezing", 0]
 ]

documents_list = []
for document in sample_data:
      
  number = document[0]
  name = document[1]
  description = document[2]
  temperature = document[3]

  json_document = {
    "numberField": number,
    "nameField": name,
    "descriptionField": description,
    "temperatureField": temperature
  }

  documents_list.append(json_document)
my_db.bulk_docs(documents_list)

# result_collection = Result(my_db.all_docs, include_docs=True)
# for doc in result_collection:
#     print(doc)

selector = {"temperatureField":{"$lt": 100}}
result = my_db.get_query_result(selector, fields=['temperatureField'])
print(result.all())