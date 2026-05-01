class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.cur_pnt = 0
        self.size = 1

    def visit(self, url: str) -> None:
        self.cur_pnt += 1
        if self.cur_pnt == len(self.stack):
            self.stack.append(url)
        else:
            self.stack[self.cur_pnt] = url
        self.size = self.cur_pnt

    def back(self, steps: int) -> str:
        self.cur_pnt = max(0, self.cur_pnt - steps)
        return self.stack[self.cur_pnt]

    def forward(self, steps: int) -> str:
        self.cur_pnt = min(self.size, self.cur_pnt + steps)
        return self.stack[self.cur_pnt]


if __name__ == '__main__':
    browserHistory = BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")
    browserHistory.visit("facebook.com")
    browserHistory.visit("youtube.com")
    assert browserHistory.back(1) == "facebook.com"
    assert browserHistory.back(1) == "google.com"
    assert browserHistory.forward(1) == "facebook.com"
    browserHistory.visit("linkedin.com")
    assert browserHistory.forward(2) == "linkedin.com"
    assert browserHistory.back(2) == "google.com"
    assert browserHistory.back(7) == "leetcode.com"

    browserHistory2 = BrowserHistory("momn.com")
    browserHistory2.visit("bx.com")
    browserHistory2.visit("bjyfmln.com")
    browserHistory2.back(3)
    browserHistory2.visit("ijtrqk.com")
    browserHistory2.visit("dft.com")
    browserHistory2.back(10)
    assert browserHistory2.forward(10) == "dft.com"
