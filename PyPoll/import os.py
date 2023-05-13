import os
import csv


def file_reader(file_address):
    """"Loads the file and returns file content."""
    data = []
    with open(file_address, encoding="UTF-8") as file:
        reader = csv.reader(file, delimiter= ",")
        header = next(file, None)
        data = [row[2] for row in reader]
    return data

address= os.path.join(".", "resources", "election_data.csv")
data_list = file_reader(address)

# Introduce a dictionary of candidates and their total vote.
data_dict = {}
for candid in data_list:
    if candid in data_dict.keys():
        data_dict[candid] += 1
    else:
        data_dict[candid] = 1

candid_list = data_dict.keys()
total = len(data)
data_percentage = {}        
for candid in data_dict.keys():
    data_percentage[candid] = (data_dict[candid]/total)*100

# Turn itteratable but not subscriptable output of .keya() to a list.
# Use one member of that list as defualt to find the winner.
keys = list(data_dict.keys())
winner = keys[0]
for candid in data_dict.keys():
    if data_dict[candid] > data_dict[winner]:
        winner = candid

print("Election Results")
print("------------------------------------------------")
print(f"Total Votes: {total}")
print("------------------------------------------------")
for candid in data_dict.keys():
    print(f"{candid}: {data_percentage[candid]:.3f}% ({data_dict[candid]})")
print("------------------------------------------------")
print(f"Winner: {winner}")
print("------------------------------------------------")

with open("PyPoll.txt", "a") as f:
    f.write("Election Results \n")
    f.write("------------------------------------------------ \n")
    f.write(f"Total Votes: {total}\n")
    f.write("------------------------------------------------\n")
    for candid in data_dict.keys():
        f.write(f"{candid}: {data_percentage[candid]:.3f}% ({data_dict[candid]})\n")
    f.write("------------------------------------------------\n")
    f.write(f"Winner: {winner}")
