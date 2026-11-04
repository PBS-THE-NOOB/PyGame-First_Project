import json

class Dialogue():

    def __init__(self):
        self.first_game = 'Dialogue/first_game.json'
        self.Dialogue_index = 0
        
    def give_dialogue(self,topic : str):
            dialogue_list = self.retrive_dialogue(topic)
            if (self.Dialogue_index >= len(dialogue_list)) : return False
            dialogue_value = dialogue_list [self.Dialogue_index]
            self.Dialogue_index += 1
            return dialogue_value
            
    def retrive_dialogue(self,topic : str):
        with open(f'{self.first_game}','r') as file :
            dialogues = json.load(file)
            dialogue_list = dialogues [topic]
            return dialogue_list 
