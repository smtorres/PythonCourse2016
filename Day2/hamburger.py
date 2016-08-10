class Burger():
    def __init__(self, filling, doneness, size, toppings_ordered, container):
        self.filling = filling
        self.doneness= doneness
        self.size = size
        self.toppings = self.toppings_allowed(toppings_ordered)
        self.containter = container
    
    def toppings_allowed(self, attempted_toppings):
        allowed_toppings = ["cheese", "tomato", "onion", "lettuce", "bacon"]
        toppings=[]
        for topping in attempted_toppings:
            if topping in allowed_toppings:
                toppings.append(topping)
        return toppings
            
    def __str__(self):
        return "I'm a %s %s burger" %(self.doneness,self.filling)
    
    def tastiness(self):
        if "cheese" in self.toppings:
            return "VERY GOOD"
        elif self.doneness == "raw": return "yuck!"
        else: return "meh"
        
    def cook(self):
        time_for_doneness = 0
        if self.doneness == "raw": time_for_doneness = 0
        elif self.doneness == "rare": time_for_doneness =5
        elif self.doneness == "medium": time_for_doneness=6
        elif self.doneness == "well": time_for_doneness=8
        else: return "UNKNOWN"
        
        return self.size * 4 * time_for_doneness
        
rare_burger=Burger("beef","rare",0.25,["cheese"],"bread")

class VeggieBurger(Burger):
    def __init__(self, toppings_ordered, container):
        Burger.__init__(self,"veggie patty", "medium", 0.25, toppings_ordered, container)

    def toppings_allowed(self, attempted_toppings):
        allowed_toppings = ["cheese", "tomato", "onion", "lettuce"]
        toppings=[]
        for topping in attempted_toppings:
            if topping in allowed_toppings:
                toppings.append(topping)
        return toppings

    def cooking_time(self):
        return 6
        
        
veggie_burger = VeggieBurger(["tomato","onion","bacon"],"bread")


rare_burger = Burger("beef", "rare", 0.25, ["cheese"], "bread")
print rare_burger.cooking_time()
print rare_burger.tastiness()
print rare_burger

well_done_burger = Burger("turkey", "well done", 0.33, ["ice cream", "bacon"], "bread")
print well_done_burger.cooking_time()
print well_done_burger.tastiness()
print well_done_burger


veggie_burger = VeggieBurger(["tomato", "bacon"], "bread")
print veggie_burger.cooking_time()
print veggie_burger.tastiness()
print veggie_burger

