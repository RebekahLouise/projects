import datetime
import calendar

fish_data = {
    "north": {
        "Anchovy": {"months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "times": ["4 AM - 9 PM"], "location": "Sea"},
        "Arapaima": {"months": [6, 7, 8, 9], "times": ["4 PM - 9 AM"], "location": "River"},
        "Arowana": {"months": [6, 7, 8, 9], "times": ["4 PM - 9 AM"], "location": "River"},
        "Barreleye": {"months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "times": ["9 PM - 4 AM"], "location": "Sea"},
        "Barred Knifejaw": {"months": [3, 4, 5, 6, 7, 8, 9, 10, 11], "times": ["All day"], "location": "Sea"},
        "Bitterling": {"months": [11, 12, 1, 2, 3], "times": ["All day"], "location": "River"},
        "Blue Marlin": {"months": [1, 2, 3, 4, 7, 8, 9, 11, 12], "times": ["All day"], "location": "Pier"},
        "Blowfish": {"months": [11, 12, 1, 2], "times": ["9 PM - 4 AM"], "location": "Sea"},
        "Butterfly Fish": {"months": [4, 5, 6, 7, 8, 9], "times": ["All day"], "location": "Sea"},
        "Carp": {"months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "times": ["All day"], "location": "Pond"},
        "Clown Fish": {"months": [4, 5, 6, 7, 8, 9], "times": ["All day"], "location": "Sea"},
        "Coelacanth": {"months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "times": ["All day"], "location": "Sea (Rain)"},
        "Dab": {"months": [1, 2, 3, 4, 10, 11, 12], "times": ["All day"], "location": "Sea"},
        "Dorado": {"months": [6, 7, 8, 9], "times": ["4 AM - 9 PM"], "location": "River"},
        "Football Fish": {"months": [11, 12, 1, 2, 3], "times": ["4 PM - 9 AM"], "location": "Sea"},
        "Gar": {"months": [6, 7, 8, 9], "times": ["4 PM - 9 AM"], "location": "Pond"},
        "Giant Trevally": {"months": [5, 6, 7, 8, 9, 10], "times": ["All day"], "location": "Pier"},
        "Golden Trout": {"months": [3, 4, 5, 9, 10, 11], "times": ["4 PM - 9 AM"], "location": "River (Clifftop)"},
        "Great White Shark": {"months": [6, 7, 8, 9], "times": ["4 PM - 9 AM"], "location": "Sea"},
        "Hammerhead Shark": {"months": [6, 7, 8, 9], "times": ["4 PM - 9 AM"], "location": "Sea"},
        "Horse Mackerel": {"months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "times": ["All day"], "location": "Sea"},
        "Napoleonfish": {"months": [7, 8], "times": ["4 AM - 9 PM"], "location": "Sea"},
        "Olive Flounder": {"months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "times": ["All day"], "location": "Sea"},
        "Pale Chub": {"months": [1, 2, 3, 4, 5, 6, 9, 10, 11, 12], "times": ["9 AM - 4 PM"], "location": "River"},
        "Piranha": {"months": [6, 7, 8, 9], "times": ["9 AM - 4 PM", "9 PM - 4 AM"], "location": "River"},
        "Puffer Fish": {"months": [7, 8, 9], "times": ["All day"], "location": "Sea"},
        "Rainbowfish": {"months": [5, 6, 7, 8, 9, 10], "times": ["9 AM - 4 PM"], "location": "River"},
        "Ray": {"months": [8, 9, 10, 11], "times": ["4 AM - 9 PM"], "location": "Sea"},
        "Red Snapper": {"months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "times": ["All day"], "location": "Sea"},
        "Saddled Bichir": {"months": [6, 7, 8, 9], "times": ["9 PM - 4 AM"], "location": "River"},
        "Saw Shark": {"months": [6, 7, 8, 9], "times": ["4 PM - 9 AM"], "location": "Sea"},
        "Sea Bass": {"months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "times": ["All day"], "location": "Sea"},
        "Sea Butterfly": {"months": [12, 1, 2, 3], "times": ["All day"], "location": "Sea"},
        "Sea Horse": {"months": [4, 5, 6, 7, 8, 9, 10, 11], "times": ["All day"], "location": "Sea"},
        "Squid": {"months": [12, 1, 2, 3, 4, 5, 6, 7, 8], "times": ["All day"], "location": "Sea"},
        "Sturgeon": {"months": [9, 10, 11, 12, 1, 2, 3, 4], "times": ["All day"], "location": "River (Mouth)"},
        "Suckerfish": {"months": [6, 7, 8, 9], "times": ["All day"], "location": "Sea"},
        "Surgeonfish": {"months": [4, 5, 6, 7, 8, 9], "times": ["All day"], "location": "Sea"},
        "Tuna": {"months": [11, 12, 1, 2, 3, 4], "times": ["All day"], "location": "Pier"},
        "Whale Shark": {"months": [6, 7, 8, 9], "times": ["All day"], "location": "Sea"},
        "Zebra Turkeyfish": {"months": [4, 5, 6, 7, 8, 9, 10, 11], "times": ["All day"], "location": "Sea"}
    },
    "south": {
        "Anchovy": {"months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "times": ["4 AM - 9 PM"], "location": "Sea"},
        "Arapaima": {"months": [12, 1, 2, 3], "times": ["4 PM - 9 AM"], "location": "River"},
        "Arowana": {"months": [12, 1, 2, 3], "times": ["4 PM - 9 AM"], "location": "River"},
        "Barreleye": {"months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "times": ["9 PM - 4 AM"], "location": "Sea"},
        "Barred Knifejaw": {"months": [3, 4, 5, 6, 7, 8, 9, 10, 11], "times": ["All day"], "location": "Sea"},
        "Bitterling": {"months": [5, 6, 7, 8, 9], "times": ["All day"], "location": "River"},
        "Blue Marlin": {"months": [1, 2, 3, 5, 6, 7, 8, 9], "times": ["All day"], "location": "Pier"},
        "Blowfish": {"months": [5, 6, 7, 8], "times": ["9 PM - 4 AM"], "location": "Sea"},
        "Butterfly Fish": {"months": [10, 11, 12, 1, 2, 3], "times": ["All day"], "location": "Sea"},
        "Carp": {"months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "times": ["All day"], "location": "Pond"},
        "Clown Fish": {"months": [10, 11, 12, 1, 2, 3], "times": ["All day"], "location": "Sea"},
        "Coelacanth": {"months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "times": ["All day"], "location": "Sea (Rain)"},
        "Dab": {"months": [4, 5, 6, 7, 10, 11, 12, 1, 2, 3], "times": ["All day"], "location": "Sea"},
        "Dorado": {"months": [12, 1, 2, 3], "times": ["4 AM - 9 PM"], "location": "River"},
        "Football Fish": {"months": [5, 6, 7, 8, 9], "times": ["4 PM - 9 AM"], "location": "Sea"},
        "Gar": {"months": [12, 1, 2, 3], "times": ["4 PM - 9 AM"], "location": "Pond"},
        "Giant Trevally": {"months": [11, 12, 1, 2, 3, 4], "times": ["All day"], "location": "Pier"},
        "Golden Trout": {"months": [3, 4, 5, 9, 10, 11], "times": ["4 PM - 9 AM"], "location": "River (Clifftop)"},
        "Great White Shark": {"months": [12, 1, 2, 3], "times": ["4 PM - 9 AM"], "location": "Sea"},
        "Hammerhead Shark": {"months": [12, 1, 2, 3], "times": ["4 PM - 9 AM"], "location": "Sea"},
        "Horse Mackerel": {"months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "times": ["All day"], "location": "Sea"},
        "Napoleonfish": {"months": [1, 2], "times": ["4 AM - 9 PM"], "location": "Sea"},
        "Olive Flounder": {"months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "times": ["All day"], "location": "Sea"},
        "Pale Chub": {"months": [3, 4, 5, 6, 7, 8, 9, 10], "times": ["9 AM - 4 PM"], "location": "River"},
        "Piranha": {"months": [12, 1, 2, 3], "times": ["9 AM - 4 PM", "9 PM - 4 AM"], "location": "River"},
        "Puffer Fish": {"months": [1, 2, 3], "times": ["All day"], "location": "Sea"},
        "Rainbowfish": {"months": [11, 12, 1, 2, 3, 4], "times": ["9 AM - 4 PM"], "location": "River"},
        "Ray": {"months": [2, 3, 4, 5], "times": ["4 AM - 9 PM"], "location": "Sea"},
        "Red Snapper": {"months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "times": ["All day"], "location": "Sea"},
        "Saddled Bichir": {"months": [12, 1, 2, 3], "times": ["9 PM - 4 AM"], "location": "River"},
        "Saw Shark": {"months": [12, 1, 2, 3], "times": ["4 PM - 9 AM"], "location": "Sea"},
        "Sea Bass": {"months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "times": ["All day"], "location": "Sea"},
        "Sea Butterfly": {"months": [6, 7, 8, 9], "times": ["All day"], "location": "Sea"},
        "Sea Horse": {"months": [10, 11, 12, 1, 2, 3, 4, 5], "times": ["All day"], "location": "Sea"},
        "Squid": {"months": [6, 7, 8, 9, 10, 11, 12, 1], "times": ["All day"], "location": "Sea"},
        "Sturgeon": {"months": [3, 4, 5, 6, 9, 10, 11, 12], "times": ["All day"], "location": "River (Mouth)"},
        "Suckerfish": {"months": [12, 1, 2, 3], "times": ["All day"], "location": "Sea"},
        "Surgeonfish": {"months": [10, 11, 12, 1, 2, 3], "times": ["All day"], "location": "Sea"},
        "Tuna": {"months": [5, 6, 7, 8, 9, 10], "times": ["All day"], "location": "Pier"},
        "Whale Shark": {"months": [12, 1, 2, 3], "times": ["All day"], "location": "Sea"},
        "Zebra Turkeyfish": {"months": [10, 11, 12, 1, 2, 3, 4, 5], "times": ["All day"], "location": "Sea"}
    }
}

wanted_fish = []


def get_fish_for_day(hemisphere, date):
    month = date.month
    hour = date.hour
    available_fish = []

    for fish, details in fish_data[hemisphere].items():
        if month in details['months']:
            if "All day" in details['times'] or any(is_time_in_range(time, hour) for time in details['times']):
                available_fish.append((fish, details['times']))

    return available_fish


def is_time_in_range(time_range, hour):
    start, end = time_range.split(" - ")
    start_hour = int(start.split()[0])
    end_hour = int(end.split()[0])

    if "PM" in end and end_hour != 12:
        end_hour += 12
    if "PM" in start and start_hour != 12:
        start_hour += 12

    return start_hour <= hour < end_hour


def print_calendar_with_fish(hemisphere, fish_name):
    print(f"Available months and times for {fish_name} in {hemisphere} hemisphere:")
    months = fish_data[hemisphere][fish_name]['months']
    times = fish_data[hemisphere][fish_name]['times']
    for month in months:
        print(f"- {calendar.month_name[month]}: {', '.join(times)}")


def add_fish_to_wanted_list(fish):
    if fish not in wanted_fish:
        wanted_fish.append(fish)
        print(f"Added {fish} to your wanted list.")
    else:
        print(f"{fish} is already in your wanted list.")


def remove_fish_from_wanted_list(fish):
    if fish in wanted_fish:
        wanted_fish.remove(fish)
        print(f"Removed {fish} from your wanted list.")
    else:
        print(f"{fish} is not in your wanted list.")


def view_wanted_list(hemisphere):
    now = datetime.datetime.now()
    print("\nYour wanted list:")
    for fish in wanted_fish:
        available_months = fish_data[hemisphere][fish]['months']
        if now.month in available_months:
            available_times = fish_data[hemisphere][fish]['times']
            print(f"- {fish} (Available Now: {', '.join(available_times)})")
        else:
            next_month = min([month for month in available_months if month >= now.month], default=min(available_months))
            next_date = datetime.datetime(now.year + (1 if next_month < now.month else 0), next_month, 1)
            days, hours, minutes = get_remaining_time(next_date)
            print(f"- {fish} (Available in: {days}d {hours}h {minutes}m)")


def get_remaining_time(date):
    now = datetime.datetime.now()
    remaining = date - now
    days, seconds = remaining.days, remaining.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return days, hours, minutes


def main():
    print("\nWelcome to the Fish (and other water creatures) Finder!")
    hemisphere_choice = input("\n\nPlease choose your destination\n1. Ruisu Island (north)\n2. Deru Island (south)\nPick a Number from 1-2: ").strip().lower()

    while hemisphere_choice not in ['1', '2']:
        print("\nInvalid choice! Please choose either '1' for Ruisu Island (north) or '2' for Deru Island (south).")
        hemisphere_choice = input("\n\nPlease choose your destination\n1. Ruisu Island (north)\n2. Deru Island (south\nPick a Number from 1-2: ").strip().lower()

    hemisphere = "north" if hemisphere_choice == '1' else "south"

    while True:
        print("\nOptions:")
        print("1. View fish (and other water creatures) available today")
        print("2. View all catchable and viewable fish (and other water creatures)")
        print("3. Select a fish (or other water creature) to view availability")
        print("4. Choose a day and time to view available fish (and other water creatures)")
        print("5. Add a fish (or other water creature) to wanted list")
        print("6. Remove a fish (or other water creature) from wanted list")
        print("7. View wanted list")
        print("8. Show calendar")
        print("9. Exit")

        choice = input("\nPlease choose an option (1-9): ").strip()

        if choice == '1':
            date = datetime.datetime.now()
            available_fish = get_fish_for_day(hemisphere, date)
            print(f"\nFish (and other water creatures) available today ({date.strftime('%Y-%m-%d')}):")
            for fish, times in available_fish:
                print(f"- {fish} (Times: {', '.join(times)})")
        elif choice == '2':
            print(f"\nAll catchable fish (and other water creatures) in {hemisphere}:")
            for fish, details in fish_data[hemisphere].items():
                print(f"- {fish} (Location: {details['location']})")
        elif choice == '3':
            fish_name = input("\nEnter the name of the fish: ").title().strip()
            if fish_name in fish_data[hemisphere]:
                print_calendar_with_fish(hemisphere, fish_name)
            else:
                print("\nFish or Creature not found!")
        elif choice == '4':
            try:
                year = int(input("\nEnter the year (YYYY): "))
                month = int(input("Enter the month (MM): "))
                day = int(input("Enter the day (DD): "))
                hour = int(input("Enter the hour (24-hour format, HH): "))

                date = datetime.datetime(year, month, day, hour)
                available_fish = get_fish_for_day(hemisphere, date)
                print(f"\nFish (and other water creatures) available on {date.strftime('%Y-%m-%d %H:%M')}:")
                for fish, times in available_fish:
                    print(f"- {fish} (Times: {', '.join(times)})")
            except ValueError:
                print("Invalid Input!")
        elif choice == '5':
            fish_name = input("\nEnter the name of the fish (or other water creature): ").title().strip()
            if fish_name in fish_data[hemisphere]:
                add_fish_to_wanted_list(fish_name)
            else:
                print("\nFish or Creature not found!")
        elif choice == '6':
            fish_name = input("\nEnter the name of the fish (or other water creature) to remove: ").title().strip()
            if fish_name in fish_data[hemisphere]:
                remove_fish_from_wanted_list(fish_name)
            else:
                print("\nFish or Creature not found!")
        elif choice == '7':
            view_wanted_list(hemisphere)
        elif choice == '8':
            try:
                year = int(input("\nEnter the year (YYYY): "))
                calendar.setfirstweekday(calendar.SUNDAY)
                print(calendar.calendar(year))
            except ValueError:
                print("Invalid Input!")
        elif choice == '9':
            print("\nFarewell and have a safe trip...")
            break
        else:
            print("\nInvalid choice! Please choose a valid option.")


if __name__ == "__main__":
    main()
