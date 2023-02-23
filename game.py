class Item:
  def __init__(self, name, description, effect):
    self.name = name
    self.description = description
    self.effect = effect
    
  def BuildJson(self):
    data = {
      "name": self.name,
      "description": self.description,
      "effect": self.effect,
    }
    return data

class Player:
  def __init__(self, name, inventory):
    self.name = name
    self.inventory = inventory
    self.inventory_max_slots = 8
    
  def AddInventoryItem(self, item):
    if len(self.inventory) < self.inventory_max_slots:
      self.inventory.append(item)