from StoryboardCode import *


class BasicLogic:
    def __init__(self, logicsymbol, trigger):
        if not isinstance(trigger, Trigger):
            raise RuntimeError('Type of Trigger is wrong.')
        self.logicSymbol = logicsymbol
        self.trigger = trigger
