bottle_count = 99

while bottle_count > 0:
    print(f"{bottle_count} bottles of beer on the wall, {bottle_count} bottles of beer.")
    bottle_count -= 1
    if bottle_count != 0:
        print(f"Take one down and pass it around, {bottle_count} bottles of beer on the wall.")
    else:
        print("Take one down and pass it around, no more bottles of beer on the wall.")

print("No more battles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall")
