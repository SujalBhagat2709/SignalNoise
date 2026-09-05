"""
SignalNoise Studio
==================

Interactive interface for the SignalNoise system.
"""

from signal_noise import SignalNoise


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 60)
    print("SIGNALNOISE STUDIO")
    print("=" * 60)
    print("1. Create Information Source")
    print("2. Add Information")
    print("3. View All Sources")
    print("4. View Source Details")
    print("5. Analyze Source")
    print("6. View Signals")
    print("7. View Noise")
    print("8. View High-Priority Information")
    print("9. Exit")
    print("=" * 60)


def create_source(system):
    """Create an information source."""
    print("\n--- Create Information Source ---")

    source_id = input("Enter source ID: ").strip()
    name = input("Enter source name: ").strip()
    description = input("Describe the source: ").strip()

    success, message = system.create_source(
        source_id,
        name,
        description
    )

    print(f"\n{message}")


def get_rating(label):
    """Get a rating from 1 to 5."""
    while True:
        value = input(f"{label} (1-5): ").strip()

        try:
            value = int(value)

            if 1 <= value <= 5:
                return value

        except ValueError:
            pass

        print("Please enter a number from 1 to 5.")


def add_information(system):
    """Add an information item."""
    print("\n--- Add Information ---")

    source_id = input("Enter source ID: ").strip()

    if not system.get_source(source_id):
        print("\nSource not found.")
        return

    content = input("Enter information: ").strip()
    category = input("Enter category: ").strip()

    print("\nRate the information:")

    relevance = get_rating("Relevance")
    urgency = get_rating("Urgency")
    reliability = get_rating("Reliability")
    impact = get_rating("Impact")

    success, message = system.add_item(
        source_id,
        content,
        relevance,
        urgency,
        reliability,
        impact,
        category
    )

    print(f"\n{message}")


def view_all_sources(system):
    """Display all information sources."""
    print("\n--- All Sources ---")

    sources = system.list_sources()

    if not sources:
        print("No information sources have been created.")
        return

    for source_id, source in sources.items():
        average = system.get_average_signal_score(source_id)
        signal_ratio = system.get_signal_ratio(source_id)

        print(f"\nID: {source_id}")
        print(f"Name: {source['name']}")
        print(f"Information Items: {len(source['items'])}")
        print(f"Average Score: {average}")
        print(f"Signal Ratio: {signal_ratio}%")


def view_source_details(system):
    """Display complete source details."""
    print("\n--- Source Details ---")

    source_id = input("Enter source ID: ").strip()

    if not system.get_source(source_id):
        print("\nSource not found.")
        return

    system.display_source(source_id)


def analyze_source(system):
    """Display a compact source analysis."""
    print("\n--- Analyze Source ---")

    source_id = input("Enter source ID: ").strip()

    analysis = system.analyze_source(source_id)

    if not analysis:
        print("\nSource not found.")
        return

    print("\n" + "=" * 60)
    print("SIGNALNOISE SUMMARY")
    print("=" * 60)

    print(f"Source: {analysis['name']}")
    print(f"Total Information: {analysis['total_items']}")
    print(f"Signal: {analysis['signal_count']}")
    print(f"Noise: {analysis['noise_count']}")
    print(f"Needs Review: {analysis['review_count']}")
    print(f"High Priority: {analysis['high_priority_count']}")
    print(f"Average Score: {analysis['average_score']}")
    print(f"Signal Ratio: {analysis['signal_ratio']}%")

    print("\nRecommendation:")
    print(f"  {analysis['recommendation']}")

    print("=" * 60)


def display_items(title, items):
    """Display a collection of information items."""
    print(f"\n--- {title} ---")

    if not items:
        print("No matching information found.")
        return

    for number, item in enumerate(items, start=1):
        print(f"\n{number}. {item['content']}")
        print(f"   Category: {item['category']}")
        print(f"   Relevance: {item['relevance']}/5")
        print(f"   Urgency: {item['urgency']}/5")
        print(f"   Reliability: {item['reliability']}/5")
        print(f"   Impact: {item['impact']}/5")
        print(f"   Signal Score: {item['signal_score']}")


def view_signals(system):
    """Display signal items."""
    print("\n--- Signals ---")

    source_id = input("Enter source ID: ").strip()

    if not system.get_source(source_id):
        print("\nSource not found.")
        return

    items = system.get_signal_items(source_id)

    display_items("Signal Information", items)


def view_noise(system):
    """Display noise items."""
    print("\n--- Noise ---")

    source_id = input("Enter source ID: ").strip()

    if not system.get_source(source_id):
        print("\nSource not found.")
        return

    items = system.get_noise_items(source_id)

    display_items("Low-Value Information", items)


def view_high_priority(system):
    """Display high-priority information."""
    print("\n--- High-Priority Information ---")

    source_id = input("Enter source ID: ").strip()

    if not system.get_source(source_id):
        print("\nSource not found.")
        return

    items = system.get_high_priority_items(source_id)

    display_items("High-Priority Signals", items)


def main():
    """Run SignalNoise Studio."""
    system = SignalNoise()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_source(system)

        elif choice == "2":
            add_information(system)

        elif choice == "3":
            view_all_sources(system)

        elif choice == "4":
            view_source_details(system)

        elif choice == "5":
            analyze_source(system)

        elif choice == "6":
            view_signals(system)

        elif choice == "7":
            view_noise(system)

        elif choice == "8":
            view_high_priority(system)

        elif choice == "9":
            print("\nThank you for using SignalNoise Studio.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
