from behaviour import *

class BehaviourEngine:
    """
    Processes all behaviours in beh_dict when update() is called
    @author:  James Heslin (PROGRAM_IX)
    """
    def __init__(self, beh_dict={}):
        """
        Construct a new BehaviourEngine with a list of Behaviours 
        
        @type beh_dict: dict (Behaviour)
        @param performer: The list of Behaviours this BehaviourEngine will use
        
        @author: James Heslin (PROGRAM_IX)
        """
        self.beh_dict = beh_dict
        
    def update(self):
        """
        Process all behaviours in beh_dict
        
        @author: James Heslin (PROGRAM_IX)
        """
        for b in self.beh_dict:
            b.process()
                    