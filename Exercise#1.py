import argparse

def greet(name, role=None):
    """Greet a filmmaker by name, optionally including their role."""
    if role:
        return "Hello " + name + "! Welcome to filmmakers.io. You're the " + role + "."
    return "Hello " + name + "! Welcome to filmmakers.io."

def days_until_production(days_left):
    """Tell the filmmaker how many days remain until production."""
    if days_left == 0:
        return "Today is the big day! Break a leg!"
    if days_left == 1:
        return "You have 1 day until your next production day. Start prepping!"
    return "You have " + str(days_left) + " days until your next production day. Start prepping!"




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Greet a filmmaker and count down to production day."
    )

    parser.add_argument("--name", required=True, help="The filmmaker's name")
    parser.add_argument("--days", required=True, type=int, help="Days until production")
    parser.add_argument("--role", required=False, help="Filmmaker's role (e.g. Director, DP, Editor)")
    args = parser.parse_args()

    print(greet(args.name, args.role))
    print(days_until_production(args.days))

