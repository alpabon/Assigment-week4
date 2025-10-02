# Pick one question from timed_challenge.txt
# Paste the question as a comment below
"""
14. Navigation System
Simulate a system that supports moving forward and backward through items.
Actions: visit("A"), visit("B"), back(), forward()
Output: "A", "B", "A", "B"
"""
# Set a timer for 30 minutes and complete the question!


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def clear(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0


class NavigationSystem:
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()

    def visit(self, item):
        self.back_stack.push(item)
        self.forward_stack.clear()
        print(f"Visited: {item}")

    def back(self):
        if len(self.back_stack.items) < 2:
            print("No previous item")
            return None

        current = self.back_stack.pop()
        self.forward_stack.push(current)
        previous = self.back_stack.peek()
        print(f"Back to: {previous}")
        return previous

    def forward(self):
        if self.forward_stack.is_empty():
            print("No next item")
            return None
        next_item = self.forward_stack.pop()
        self.back_stack.push(next_item)
        print(f"Forward to: {next_item}")
        return next_item

NavigationSystem = NavigationSystem()

NavigationSystem.visit("A")
NavigationSystem.visit("B")
NavigationSystem.back() 
NavigationSystem.forward()  

NavigationSystem.back()  
NavigationSystem.back()  
NavigationSystem.forward()  
NavigationSystem.forward()  

#What structure you chose and why
#the structure i chose was stack because it follows the LIFO principle which is perfect for this problem, however i needed two stacks to handle both back and forward navigation. which means, that when we go back, we push the current item onto the forward stack, and when we go forward, we pop from the forward stack and push it back onto the back stack.
#How the time limit shaped your decision
#the time limit made me choose a better and more organized version, because at the beggining i wanted to do one stack and use a pointer to track the current position, but that would have made the code more complex and harder to manage within the time limit. so i changed my mind and did a code that is more simple and better in terms of usage
#What trade-offs or compromises you made under time pressure
#the trade off i made was to not implement error handling for invalid inputs or edge cases, because i wanted to focus on the main functionality of the navigation system within the time limit. so i focus more on the code to ensure it works that on handling cases that break the code, if id focus on both i wouldnot make it on time.
