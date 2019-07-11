import urllib.request
import os
import time

path= "D:/ML Using sckit/intraQuarter"

def Check_Yahoo():
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]

    ## Added a counter to call out how many files we've already added
    counter = 0
    for e in stock_list[1:]:

        try:
            ticker = e.split("\\")[1]
            print(ticker)
            e = e.replace("D:/ML Using sckit/intraQuarter/_KeyStats","")
            ## Changed the URL & added the modules
            link = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/"+e.upper()+"?modules=assetProfile,financialData,defaultKeyStatistics,calendarEvents,incomeStatementHistory,cashflowStatementHistory,balanceSheetHistory"
            resp = urllib.request.urlopen(link).read()
            ## We go by Bond. JSON Bond
            save = "forward_json/"+str(e)+".json"
            store = open(save,"w")
            store.write(str(resp))
            store.close()
            ## Print some stuff while working. Communication is key
            counter +=1
            print("Stored "+ e +".json")
            print("We now have "+str(counter)+" JSON files in the directory.")


        except Exception as e:
            
            print(str(e))
            time.sleep(2)
Check_Yahoo()
