class mockKeyInjection:
    def __init__(self, key):
        self.key = key

    def injectKey(self, key) -> bool:
        return False

class keyInjector(mockKeyInjection):
    def injectKey(self, key) -> bool:
        return super().injectKey(key)

