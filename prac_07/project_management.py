import datetime
import csv
from project import Project

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    menu = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
    while True:
        print(menu)
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_option = input("Would you like to save to projects.txt? ")
            if save_option.lower() == 'y':
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            return
        else:
            print("Invalid choice. Try again.")

def load_projects(filename="projects.txt"):
    """Load projects from a given file."""
    projects = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file, delimiter='\t')
            next(reader)  # Skip header
            for row in reader:
                projects.append(Project(*row))
        print(f"Loaded {len(projects)} projects from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting fresh.")
    return projects

def save_projects(filename, projects):
    """Save projects to a given file."""
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion"])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'),
                             project.priority, project.cost_estimate, project.completion])
    print(f"Saved {len(projects)} projects to {filename}")

def display_projects(projects):
    """Display projects sorted by priority, grouped by completion status."""
    projects.sort()
    print("Incomplete projects:")
    for project in projects:
        if not project.is_complete():
            print(f"  {project}")
    print("Completed projects:")
    for project in projects:
        if project.is_complete():
            print(f"  {project}")

def filter_projects_by_date(projects):
    """Filter projects that start after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [p for p in projects if p.start_date > filter_date]
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(project)

def add_new_project(projects):
    """Add a new project based on user input."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion))

def update_project(projects):
    """Update an existing project's completion or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    index = int(input("Project choice: "))
    project = projects[index]
    print(project)
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_completion:
        project.completion = int(new_completion)
    if new_priority:
        project.priority = int(new_priority)

main()