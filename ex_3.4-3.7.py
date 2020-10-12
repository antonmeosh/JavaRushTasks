#3.4
guest = ["Anton", "Rita", "Alisa", "Olivia", "Burton"]
message  = f"{guest[0].title()}, go ko mne!"
print(message)
message  = f"{guest[1].title()}, go ko mne!"
print(message)
message  = f"{guest[2].title()}, go ko mne!"
print(message)
message  = f"{guest[3].title()}, go ko mne!"
print(message)
message  = f"{guest[4].title()}, go ko mne!"
print(message)
#3.5
guest[4] = "Enakin"
message  = f"{guest[4].title()}, go ko mne!"
print(message)
#3.6
guest.insert(0, "Mama")
guest.insert(2, "Papa")
guest.append("Daria")
print(guest)
#3.7
print("na obed tol'ko 2 mogno")
last_guest = guest.pop()
print(f"sori, {last_guest.title()}, ne prihodi.")
last_guest = guest.pop()
print(f"sori, {last_guest.title()}, ne prihodi.")
last_guest = guest.pop()
print(f"sori, {last_guest.title()}, ne prihodi.")
last_guest = guest.pop()
print(f"sori, {last_guest.title()}, ne prihodi.")
last_guest = guest.pop()
print(f"sori, {last_guest.title()}, ne prihodi.")
last_guest = guest.pop()
print(f"sori, {last_guest.title()}, ne prihodi.")
print( f"{guest[0].title()}, go ko mne!")
print( f"{guest[1].title()}, go ko mne!")
del guest[1]
del guest[0]
print(guest)
