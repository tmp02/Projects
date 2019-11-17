import requests

class Blog:

    def posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        self.content = response.json()


    def showContent(self):
        text = 'Id: ' + str(self.content[0]['id']) + '\nTitle: ' + self.content[0]['title'] 
        return text
