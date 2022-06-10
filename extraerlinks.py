import urllib.request
from bs4 import BeautifulSoup
from numpy import append
import pandas as pd
import requests
import time
import csv
from random import randint


theurl = "https://convecta.cl/clientes.aspx"
thepage = urllib.request.urlopen(theurl)

soup = BeautifulSoup(thepage)

project_href = [i['href'] for i in soup.find_all('a', href=True)]

print(project_href)


project_href = pd.DataFrame(project_href)

project_href.to_excel("Sitioweb2.xlsx")