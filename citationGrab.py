import requests
from bs4 import BeautifulSoup
import pyperclip as pc

paper = pc.paste()
base_url = "https://scholar.google.de/scholar?hl=de&as_sdt=0%2C5&q=" + paper + "&btnG= "

googleSearch = requests.request("GET", url=base_url)

bs_page = BeautifulSoup(googleSearch.content, "html.parser")
block = bs_page.find("div", {"class": "gs_ri"})
title = block.find("h3")
link = title.find("a")
citation_id = link["id"]

cite_url = "https://scholar.google.de/scholar?hl=de&q=info:" + citation_id + ":scholar.google.com/&output=cite&scirp=0"

findLatex = requests.request("GET", url=cite_url)

citation_view = BeautifulSoup(findLatex.content, "html.parser")
latex_link = citation_view.find("div", {"id": "gs_citi"})

latex_mf = latex_link.findChildren("a")[0]["href"]

result = BeautifulSoup(requests.request("GET", url=latex_mf).content, "html.parser")
citation = result.text
pc.copy(citation)
print(citation)
