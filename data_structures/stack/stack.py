# %% [markdown]
# # Stack
# Stack is a last in first out data structure (LIFO).
# Examples: stack of books, in order to properly take out the book on the bottom, you'll need to move all the top books first.

# %%

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def get_stack(self):
        return self.items
