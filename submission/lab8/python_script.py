import json

with open('../../data/schacon.repos.json', 'r') as file:
    data = json.load(file)
    file_out = open("chacon.csv", "w")



    five_repos = data[:5]
    for i in range(0, 5):
        name = five_repos[i]['name']
        url = five_repos[i]['html_url']
        updated = five_repos[i]['updated_at']
        visible = five_repos[i]['visibility']



        line_to_add = name + ',' + url + ',' + updated + ',' + visible
        if(i < 4):
            line_to_add = line_to_add + "\n" 
            
        file_out.write(line_to_add)  


