import networkx as nx
import csv


file = "C:\Users\\leahk\Downloads\\fakenews2(1).csv"
lst = []
processed_list = []
with open(file, 'rb') as csv_file:
    next(csv_file)
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        if ''.join(row).strip():
         lst.append(row)
#print lst[0]

G = nx.DiGraph()
for row in lst:
   # print row
    r_id = int(row[1])
    parent_id = int(row[2])
    dic = {}
    dic['campaign_id'] = row[0]
    dic['url'] = row[3]
    dic['main_headline'] = row[4]
    dic['retweet_headline'] = row[5]
    dic['date'] = row[6]
    if len(row)>7:
        dic['mediaurl'] = row[7]
    processed_list.append([parent_id, r_id, dic])

for row in processed_list:
    G.add_weighted_edges_from(processed_list)
#print G.edges()
print list(G.successors(667218202))
#print G.