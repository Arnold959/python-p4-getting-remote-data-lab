import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        try:
            json_data = json.loads(response_body)
        except ValueError:
            # If the response is not valid JSON
            raise ValueError("Invalid JSON response")

        return json_data


URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
data = GetRequester(URL)
converted_data = data.load_json()

for item in converted_data:
    print(item)