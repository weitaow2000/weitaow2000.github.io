
from pathlib import Path
from PIL import Image, ImageOps

source = Path("images/life")
output = source / "preview"

output.mkdir(parents=True, exist_ok=True)

MAX_SIZE = 1200
QUALITY = 78

for file in source.iterdir():

    if not file.is_file():
        continue

    if file.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
        continue

    name = file.name.split(".")[0]
    target = output / f"{name}.webp"

    with Image.open(file) as img:
        img = ImageOps.exif_transpose(img)
        img = img.convert("RGB")
        img.thumbnail(
            (MAX_SIZE, MAX_SIZE),
            Image.Resampling.LANCZOS
        )
        img.save(
            target,
            "WEBP",
            quality=QUALITY,
            method=6
        )

    original_kb = file.stat().st_size / 1024
    compressed_kb = target.stat().st_size / 1024

    print(
        f"{file.name}: "
        f"{original_kb:.0f} KB -> "
        f"{compressed_kb:.0f} KB"
    )

print("All images compressed successfully!")
