import requests

class Blog:
    def __init__(self,name):
        self.name = name
        self.content = ''
    
    def posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        return response.json()


    def showContent(self,content):
        text = 'Blog Name: '+ self.name + '\nTitle: ' + content[0]['title']
        return text
