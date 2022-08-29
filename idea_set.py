from idea import Idea


class IdeaSet:
    tag = "HAB"
    start = {}
    bonus = {}

    trigger = {}
    free = True
    ideas = [Idea(), Idea(), Idea(), Idea(), Idea(), Idea(), Idea()]

    def __init__(self, tag, start, bonus, trigger, ideas, free=True):
        self.tag = tag
        self.start = start
        self.bonus = bonus
        self.trigger = trigger
        self.ideas = ideas

        if free is not None:
            self.free = free
