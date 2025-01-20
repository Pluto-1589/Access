class Fridge:

    def __init__(self) -> None:
        self.in_the_fidge = []

    def store(self, item):
        self.in_the_fidge.append(item)

    def take(self, item: tuple):
        # Items can be taken out of the fridge by providing their names and eat-by dates. Such an invocation should remove and return the first matching item in the fridge. A Warning should be raised if no matching item can be found.
        if item not in self.in_the_fidge:
            raise Warning("No matching item can be found")
        else:
            self.in_the_fidge.remove(item)
            return item

    def find(self, name):
        # takes a name and searches for the item tuple with the same name and the earliest eat-by date.

        # If it should be removed as well, an additional call to take is required, with the item as argument. If no matching item can be found, None should be returned. As a metaphor, think about a person that wants to know whether there is still milk in the fridge, e.g., while writing a grocery shopping list, this person would not take the item out.
        all_with_name = [tup for tup in self.in_the_fidge if tup[1] == name]

        if all_with_name:
            return min(all_with_name)
        else:
            return None

    def take_before(self, date):
        # identify and remove all items from the fridge for which the eat-by date is before the provided date and return them in a list.
        # Return an empty list if no items match.
        expired = []

        for tup in self.in_the_fidge:
            if date > tup[0]:
                expired.append(tup)

        for item in expired:
            self.in_the_fidge.remove(item)

        return expired

    def __iter__(self):
        return iter(sorted(self.in_the_fidge))

    def __len__(self):
        return len(self.in_the_fidge)


f = Fridge()
f.store((191127, "Butter"))
f.store((191117, "Milk"))


# f.take((191127, "Butter"))  # ok
# f.take((191207, "Bread"))  # fails

# # print(f)

# print("Items in the fridge:")
# for i in f:
#     print(f"- {i[1]} ({i[0]})")
