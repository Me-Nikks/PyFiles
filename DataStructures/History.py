class BrowserHistory:
    def __init__(self):
        self.history = []

    def visit_page(self, page):
        self.history.append(page)  # Adding visited page to history stack
        print(f"Visited page: '{page}'")

    def go_back(self):
        if not self.history:
            print("No pages to go back to.")
        else:
            previous_page = self.history.pop()  # Removing the most recent page
            print(f"Going back to: '{previous_page}'")

# Creating an instance of BrowserHistory
browser = BrowserHistory()

# Simulating browsing history
browser.visit_page("Homepage")
browser.visit_page("About Us")
browser.visit_page("Contact Us")

browser.go_back()  # Go back to the previously visited page
browser.go_back()  # Go back again
browser.go_back()  # Go back once more
browser.go_back()  # Trying to go back when no pages are left
