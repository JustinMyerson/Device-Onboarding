class mockKeyInjection:
    def __init__(self, key):
        self.key = key

    def injectKey(self, key) -> bool:
        pass

class keyInjector(mockKeyInjection):
    def injectKey(self, key) -> bool:
        return super().injectKey(key)

