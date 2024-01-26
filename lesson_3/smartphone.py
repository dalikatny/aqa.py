class Smartphone:
    def __init__(self,brend : str,model : str,number : str) :
        self.brend=brend
        self.model=model
        self.number=number
    
    def print_catalog(self):
        print("Brend: ",self.brend, "Model: ",self.model, "Number: ", self.number)
           
        
        
