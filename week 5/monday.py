import pathlib

data_folder = pathlib.Path('data')

# print(data_folder.exists(), data_folder.is_dir())

def make_text(i):
    text = ""
    text += str(i) + "\n"
    text += str(i * 24) + "\n"
    text += (i * 12) * "#"
    return text

for i in range(20):
    label = str(i).zfill(4) + "." + ("ihatezoom" * i)
    f = pathlib.Path(label)
    out = data_folder / f
    out.write_text(make_text(i))
