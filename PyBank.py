import csv

with open('budget_data.csv', newline = '') as f:
    
    csvreader = csv.reader(f, delimiter=',')       
    reader = csv.reader(f)
    listr = open('budget_data.csv')
    
    next(reader)

    conta= 0
    sum_conta = 0
    for row in csvreader:
        conta += 1

       
    print(f"Total Months: {conta}")

with open('budget_data.csv', newline = '') as f:
    
    csvreader = csv.reader(f, delimiter=',')       
    reader = csv.reader(f)
    
    #calular Total: $38382578 
    next(reader)
        
    review_row = [int(row[1]) for row in csvreader]

    max_profit_date = max(review_row)
    min_profit_date = min(review_row)
    
    print (f"Total:${sum(review_row)}")
    
    
with open('budget_data.csv', newline = '') as f:
    
    csvreader = csv.reader(f, delimiter=',')       
    reader = csv.reader(f)     
    
    next(reader)

    list_row = [int(row[1]) for row in csvreader]
    #print(list_row) 
   
    ant = 0
    sumatoria =0
    antmax = 1
    antmin = 1
    list_row 
    for i in list_row:
       if ant != 0:
          dif = i - ant
        
          #print(f"{i} - {ant} =  {dif}")      
          sumatoria+=dif     
              
          if i == max_profit_date:
            antmax = ant
                      
          if i == min_profit_date:
            antmin = ant    
               
       ant=i
        
    ave_change = sumatoria /(conta - 1) 
    
    #print(f"average change: {sumatoria} / {row_count}${ round(ave_change,2)}")
    print(f"average change:${round(ave_change,2)}")
    #print(f"{max_profit_date}-{antmax} ={max_profit_date-antmax}")
  
    
with open('budget_data.csv', newline = '') as f:
    
    csvreader = csv.reader(f, delimiter=',')       
    reader = csv.reader(f)     
    
    next(reader)

    for row in csvreader:
     
        if row[1] == str(max_profit_date):
            print("Greatest increase profits:"+ row[0] + " " + "$" +  str(max_profit_date - antmax))
                                   
        if row[1] == str(min_profit_date):
               
            print("Greatest decrease profits:"+ row[0] + " " + "$" +str(min_profit_date - antmin))
        
  
             
            
            

