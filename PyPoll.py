import csv

with open('Resources_election.csv', newline = '') as f:
    
    csvreader = csv.reader(f, delimiter=',')       
    reader = csv.reader(f)
        
    next(reader)

    conta= 0
  
    for row in csvreader:
        conta += 1
    
    print(f"Total Votes: {conta}")

with open('Resources_election.csv', newline = '') as f:
    
    csvreader = csv.reader(f, delimiter=',')       
    reader = csv.reader(f)
    
    list_row = [row[2] for row in csvreader]
      
    candidate_list = list(set(list_row))
    
    print(f"candidates: {candidate_list}")
