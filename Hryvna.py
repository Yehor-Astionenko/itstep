from typing import List


import requests


response = requests.get("https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D0%B0+%D0%B4%D0%BE+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D1%96&sca_esv=581526710&rlz=1C1GCEU_ukUA1034UA1034&sxsrf=AM9HkKl8HrJvwnmXDndOJGWKpHGbhKW33g%3A1699716121915&ei=GZxPZeO2N87gkgXWtrCoDQ&oq=rehc+usd&gs_lp=Egxnd3Mtd2l6LXNlcnAiCHJlaGMgdXNkKgIIATIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwA0jVEFAAWABwAngAkAEAmAFfoAFfqgEBMbgBAcgBAOIDBBgAIEGIBgGQBgg&sclient=gws-wiz-serp")


response_text = response.text


response_parse = response_text.split("<span>")


hryvnas = []


for item in response_parse:
  if item.startswith("35"):
      for hryvna_item in item.split ("</span>"):
          if hryvna_item.startswith("35") and hryvna_item[1].isdigit():
              hryvnas.append(hryvna_item)
bit = int(input("How much hryvnas do you have?  "))
value = hryvnas[0][1:]
bit_rate = float(value.replace(",", ""))
print (value)
print("You have", bit, "bitcoins")
print("You have ", bit / bit_rate)
print(hryvnas)
print("Coin excange rate -", hryvnas[0])



