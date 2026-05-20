import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.cluster import KMeans
import requests

url = "https://en.wikipedia.org/wiki/Cinema_of_India"
headers = {"User-Agent": "aryan"}
response = requests.get(url,headers=headers)
# print(response.text)  riceve data in html 
soup = BeautifulSoup(response.text,"html.parser")
print(soup)