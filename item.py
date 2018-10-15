class Item():
  
  def __init__(self, item_name):
    self.name = item_name
    self.description = None 
    
  
  def set_name(self, item_name):
    self.name = item_name
    
  def get_name(self):
    return self.name
    
  def set_description(self, item_description):
    self.description = item_description
    

  def get_description(self):
    return self.description

  def describe(self):
    print("The [" + self.name + "] is here - " + self.description)


  def set_description2(self, item_description2):
    self.description2 = item_description2
    

  def get_description2(self):
    return self.description2

  def describe2(self):
    print(self.description2)
