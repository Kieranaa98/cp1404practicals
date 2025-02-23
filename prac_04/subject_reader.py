FILENAME = "subject_data.txt"


def main():
    """Read subject data and print"""
    subjects = load_subjects()
    display_subjects(subjects)


def load_subjects():
    """Load data from the file """
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject.append(parts)
    input_file.close()
    return subject


def display_subjects(subjects):
    """Display the data"""
    for subject in subjects:
        print("{} is taught by {:12} and has {:3} students".format(*subject))


main()