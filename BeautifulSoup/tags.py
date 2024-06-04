from bs4 import BeautifulSoup
import requests

with open('Source.html','r') as f:
    htmlDoc = f.read()
soup = BeautifulSoup(htmlDoc, 'html.parser');
# print(soup.title.string, type(soup.title), soup.title.name)
# print(type(soup.find_all('div')[0]))
# for link in soup.find_all('a'):
#     print(link.get('href'))
#     print(link.get_text())
# print(soup.select('div.DataScraping')[0])
# s = soup.find(id='link3')
# print(s.get('href'))
# print(soup.span.get('class'))
# print(soup.find(class_='DataScraping'))
# a = 0
# for child in soup.find(class_='container').children:
    # print(child)
#     a=child
# print(type(a))
# i = 0
# for parent in a.parents:
#     i+=1
#     print(parent)
#     if(i==2):
#         break
cont = soup.find(class_ = 'container')
# print(cont)
# cont.name = 'span'
# cont["class"] = 'My_class class2'
# cont.string = 'I am a string'
# print(cont)

# ul = soup.new_tag('ul')
# li = soup.new_tag('li')
# li.string = 'Trying to create a new tag'
# ul.append(li)
# li = soup.new_tag('li')
# li.string = 'Testing the creation of a new tag'
# ul.append(li)
# soup.html.body.insert(0 , ul)
# with open('Modified_Source.html', 'w') as f:
#     f.write(str(soup))
# print(cont.has_attr('class'))
def classandid(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
results = soup.find_all(classandid)
for result in results:
    print(result, "\n\n")


