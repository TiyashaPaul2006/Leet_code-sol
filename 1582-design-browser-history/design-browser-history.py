class BrowserHistory:

    def __init__(self, homepage):
        self.history = [homepage]
        self.current = 0

    def visit(self, url):
        # Remove all forward history
        self.history = self.history[:self.current + 1]

        self.history.append(url)
        self.current += 1

    def back(self, steps):
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps):
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]