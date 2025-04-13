import wikipedia

def get_wikipedia_info(title):
    """Retrieves and prints the title, summary, and URL of a Wikipedia page.
    Handles DisambiguationError and PageError exceptions.
    """
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(page.title)
        print(wikipedia.summary(title, sentences=2))
        print(page.url)
        return True
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"We need a more specific title. Try one of the following, or a new search:")
        print(e.options[:5] if len(e.options) > 5 else e.options)
        return False
    except wikipedia.exceptions.PageError:
        print(f"Page id \"{title}\" does not match any pages. Try another id!")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def main():
    page_title = input("Enter page title: ").strip()
    if not page_title:
        print("Thank you.")
        return

    if get_wikipedia_info(page_title):
        print()
        main() # Recursive call for the next input
    else:
        print()
        main() # Recursive call for the next input

main()