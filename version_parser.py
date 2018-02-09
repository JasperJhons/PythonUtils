import os
import requests
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    version_list = list()

    def handle_data(self, data):
        if "/" in data and " " not in data:
            self.version_list.append(data[:-1])


request = requests.get('')
parser = MyHTMLParser()
parser.feed(request.text)
version_list = parser.version_list[1:]
version_list.sort(key=lambda s: [int(u) for u in s.split('.')])

current_path = os.path.abspath(os.path.dirname(__file__))
current_version_file = open(current_path + '/current_version', 'w')
current_version_file.write('buildVersion=' + version_list[-1])
current_version_file.close()
print(version_list[-1])
