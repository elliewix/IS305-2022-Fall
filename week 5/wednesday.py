import pathlib
import csv

print("being run from", pathlib.Path('.').cwd()) # my current working directory
# target = pathlib.Path('../week 4')
target = pathlib.Path('..')

visible = [p for p in target.glob('*') if not p.name.startswith('.')]
visible_files = []

for visible_folder in visible:
    files = list(visible_folder.rglob('*'))
    for f in files:
        if not f.name.startswith('.'):
            visible_files.append(f)

# print(visible_files)

all_stats = []
for p in visible_files:
    row = [p.name, p.resolve(), p.stat()]
    all_stats.append(row)

headers = ["file_name", "resolved_path", "stats"]

with open(pathlib.Path('filestats.csv'), 'w') as fileout:
    csvout = csv.writer(fileout)
    csvout.writerow(headers)
    csvout.writerows(all_stats)

# for p in visible:
#     print(p)

# print(target.exists())
# print(target.absolute())
# print(list(target.glob('*.*')))
# for p in target.rglob("*"):
#     if p.is_file():
#         # print(type(p.name))
#         if not p.name.startswith('.'):
#             for parent in p.parents:
#                 if (not parent.name.startswith('.')) and parent.name.count('.') == 1:
#                     print(p)
