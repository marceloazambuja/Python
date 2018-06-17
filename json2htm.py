from json2html import *
import pandas as pd

# using read_html method from Pandas, read a Table from URL
world_cup = pd.read_html("https://www.bbc.com/sport/football/world-cup/schedule/group-stage", header=0)
print(world_cup[0])

jSonTable = world_cup[0].to_json(orient="records", date_format="iso")  # to Json

print(json2html.convert(json = jSonTable))  # JSon to HTML
htmlTable = json2html.convert(json = jSonTable)

fileWrite = open('worldcup.html',"w")       # write HTML file
fileWrite.write(htmlTable)
fileWrite.close()
