c = 1
import time 
for i in range(1,2):
    while True:
        if c == 1:
            import distance
            d=distance.distancesensor()
            c = 2
        elif c == 2:
            import load
            w = int(load.loop())
            c = 3
        else:
            import database as db
            if w < 5000 and w > 4000:
                load = "90 %"
                
            elif w < 4000 and w > 3000:
                load = "60 %"
                
            elif w < 3000 and w > 100:
                
                load = "40 %"
            else:
                load = "0 %"
                
            if d > 30:
                distance = "90 %"
                
            elif d < 30 and d >20:
                distance = "60 %"
                
            elif d < 20 and d > 5:
                distance = "40 %"
            else:
                distance = "7 %"
                
                
                
            if load == "90 %" or distance == "90 %":
                m = "Risk Warning: Dumpster poundage getting high, Time to collect :)"
                
            elif load == "60 %" or distance == "60 %":
                
                m ="dumpster is above 60%"
            else :
                m = "         "
                
            db.database(d,w,m,load,distance)
            print("data pushed")
            c = 1
            break 
    

  
  
