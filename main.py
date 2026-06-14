from colorama import Fore, Style, init

from hash_identifier import identify_hash
from hash_generator import generate_hashes
from history_manager import (
    save_to_history,
    view_history,
    clear_history
)

init(autoreset=True)

identify_count = 0
generate_count = 0

while True:

    print(Fore.CYAN + "\n" + "=" * 40)
    print(Fore.CYAN + "HASH IDENTIFIER TOOL")
    print(Fore.CYAN + "=" * 40)

    print(Fore.YELLOW + "\n1. Identify Hash")
    print(Fore.YELLOW + "2. Generate Hash")
    print(Fore.YELLOW + "3. View History")
    print(Fore.YELLOW + "4. Clear History")
    print(Fore.YELLOW + "5. Exit")

    print(
        Fore.MAGENTA +
        f"\nIdentified: {identify_count} | Generated: {generate_count}"
    )

    choice = input("\nSelect Option: ")

    if choice == "1":

        hash_value = input("\nEnter Hash: ")

        possible_types, security = identify_hash(hash_value)

        if possible_types is None:
            print(Fore.RED + "Invalid Hash Format")
            continue

        if not possible_types:
            print(Fore.RED + "Unknown Hash Type")
            continue

        identify_count += 1

        print(Fore.GREEN + "\nPossible Hash Types:")

        for i, h in enumerate(possible_types, start=1):
            print(Fore.YELLOW + f"{i}. {h}")

        print(Fore.GREEN + "\nSecurity Analysis:")

        for h, level in security:
            print(Fore.MAGENTA + f"{h} --> {level}")

        save_to_history(
            "Hash Identification",
            f"{hash_value}"
        )

    elif choice == "2":

        text = input("\nEnter Text: ")

        hashes = generate_hashes(text)

        generate_count += 1

        print(Fore.GREEN + "\nGenerated Hashes:\n")

        for algo, value in hashes.items():
            print(Fore.YELLOW + f"{algo}: {value}")

        save_to_history(
            "Hash Generation",
            text
        )

    elif choice == "3":
        view_history()

    elif choice == "4":
        clear_history()
        print(Fore.GREEN + "History Cleared")

    elif choice == "5":
        print(Fore.RED + "Goodbye!")
        break

    else:
        print(Fore.RED + "Invalid Option")