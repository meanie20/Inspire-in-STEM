#no method used
class vehicle:
    def __init__(self,type,model,max_speed,mileage):
        self.type = type
        self.model = model
        self.max_speed = max_speed
        self.mileage = mileage
    
vehicle_001 =vehicle('Toyota','Hatchback',str(120),str(300))
print("This is a",vehicle_001.type,vehicle_001.model,".The maximum speed is",vehicle_001.max_speed,"km/hr and the mileage is",vehicle_001.mileage ,"km")