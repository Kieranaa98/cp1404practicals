import datetime

class Project:
    """Class to represent a project with attributes for management."""

    def __init__(self, name, start_date, priority, cost_estimate, completion):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion = int(completion)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion}%")

    def __lt__(self, other):
        """Sorting projects by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Check if the project is complete."""
        return self.completion == 100
