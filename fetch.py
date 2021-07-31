import requests as req
from loggers import *
from bs4 import BeautifulSoup

with open("amcs.txt",'r') as amc_file:
	for url in amc_file.readlines():
		if url == EMPTY_STRING:
			pass
		html_source = req.get(url).content
		soup = BeautifulSoup(html_source, LXML_PARSER)
		try:
			fund_title = soup.find("h1",attrs={'class':FUND_TITLE_CLASS}).text
			print(f"Fund Name: {fund_title}")
			company_names = []
			holdings_table = soup.find(id=HOLDINGS_TABLE_ID)
			for row in holdings_table.tbody.find_all("tr"):
				#print(row.find("td").find("a",attrs={'target':'_blank'}).text)
				company_names.append(row.find("td").find("a",attrs={'target':TARGET_BLANK}).text)
			no_of_holdings = len(company_names)
			print(f"No. of holdings: {no_of_holdings}")
			with open(f"{FILE_PATH}\\{fund_title} [{no_of_holdings}].txt","w") as writer:
				for i in company_names:
					writer.write(f"{i}\n")
		except:
			print(HOLDINGS_TABLE_NOT_FOUND)
		linespace()
prgm_end()