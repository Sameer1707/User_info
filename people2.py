import github
from github import Github
import json
import requests
import urllib
from urllib.request import urlopen
import csv
import xml.etree.ElementTree as ET
from flask import Flask, jsonify, request
username='satyamsi'
#start='2018-01-01'
#end='2018-01-02'
resp= requests.get("https://github.com/users/"+username+"/contributions")
xmlfile='contri.xml'
file=open('C:\Python36\output.txt','w+')
with open(xmlfile, 'wb') as f:
        f.write(resp.content)
tree=ET.parse(xmlfile)
root=tree.getroot()
file.write("   date"+"        "+"contributions\n")
a=list()
c=list()
dict1={}
dict2={}
start='2018-06-08'
end='2018-06-01'
for child in root:
	for child1 in child:
		for child2 in child1:
			dict1={child2.attrib['data-date']:child2.attrib['data-count']}
			dict2.update(dict1)
			a.append(child2.attrib['data-date'])
a.reverse()
for value in a:
	if a.index(value)>=a.index(start) and a.index(value)<=a.index(end):
		file.write("%s\t\t\t%s\n" %(value,dict2[value]))
		c.append(dict2[value])
print(c)
file.close()
app = Flask(__name__)

# @app.route('/user')
# def get_user():
	# return jsonify(dict2)

# @app.route('/user',methods=['GET'])

# def user_info():
	# print(dict2)

# # if __name__ == '__main__':
    # # app.run(debug=True)