class Player:
    def __init__(self, username, current_scene="start", items = None, health = 10):
        self.username = username
        self.items = items if items is not None else []
        self.current_scene = current_scene
        self.health = health
