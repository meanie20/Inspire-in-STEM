#lists in dictionaries
mary_fav_food=["ugali","nyama","indomie"]
jane_fav_food=["rice","spaghetti","ice-cream"]
fav_foods={
    "mary":["ugali","nyama","indomie"],
    'jane':["rice","spaghetti","ice-cream"]
}
#for x in fav_foods.keys():
    #print(fav_foods["mary"])
  
for key,value in fav_foods.items():
  print(key, ':', value)
