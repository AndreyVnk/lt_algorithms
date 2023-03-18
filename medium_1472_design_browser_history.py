'''
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
'''

class BrowserHistory:

    def __init__(self, homepage: str):
        self.visit = [homepage]
        self.idx = 0
        self.last = 0

    def visit(self, url: str) -> None:
        self.idx += 1
        self.visit = self.visit[:self.idx]
        self.visit.append(url)
        self.last = self.idx

    def back(self, steps: int) -> str:
        self.idx = max(0, self.idx - steps)
        return self.visit[self.idx]

    def forward(self, steps: int) -> str:
        self.idx = min(self.last, self.idx + steps)
        return self.visit[self.idx]

