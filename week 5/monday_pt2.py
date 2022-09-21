import pathlib

target = pathlib.Path('data')

print(target.exists(), target.is_dir())

# print(target.glob('*'))
# print(list(target.glob("*")))

# for p in target.glob('*'):
#     print(p)
#     # print(p.read_text())

