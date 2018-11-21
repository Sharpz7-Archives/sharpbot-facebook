import os
from importlib import import_module

names = os.listdir("cogs")
mods = []
for item in names:
    if item[-3:] == ".py" and item != "__init__.py":
        item = item.replace(".py", "")
        mods.append(item)

for item in mods:
    import_module("cogs." + item)
    peint(f"Imported cogs.{item}")
