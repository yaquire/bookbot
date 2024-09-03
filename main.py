print("Hello World :)")

with open("books/frankenstein.txt") as f:
    # ...
    file_contents = f.read()

words = file_contents.split()

# print(len(words))

times_appeared = {}

for item in words:
    lowered_item = item.lower()
    for character in lowered_item:
        try:
            times_appeared[character] += 1
        except KeyError:
            times_appeared[character] = 1


# print(times_appeared)
print("--- Begin report of /books/frankenstein.txt ---")
print(f"{len(words)} words found in the document")
for item in times_appeared:
    print(f"The {item} was found {times_appeared[item]} times")

print("--- End Report ---")
