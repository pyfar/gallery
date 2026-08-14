# DISCLAIMER: Code generated with an LLM using pillow 12.3.0
from PIL import Image, ImageDraw, ImageFont

W, H = 200, 150
img = Image.new("RGB", (W, H), (30, 33, 41))  # dark editor bg
draw = ImageDraw.Draw(img)

# Fonts: paths point to DejaVu Sans Mono on Linux.
# Swap in any monospace font if not available, e.g.,
# - macOS: /System/Library/Fonts/Menlo.ttc,
# - Windows: C:/Windows/Fonts/consola.ttf),
# - or use ImageFont.load_default().
mono = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
mono_bold = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

font = ImageFont.truetype(mono, 12)
font_bold = ImageFont.truetype(mono_bold, 12)

# Colors (VS Code "Dark+"-ish palette)
c_bg = (30, 33, 41)
c_linenum = (90, 96, 110)
c_kw = (198, 120, 221)      # purple keyword
c_func = (97, 175, 239)     # blue function
c_str = (152, 195, 121)     # green string
c_num = (209, 154, 102)     # orange number
c_comment = (106, 115, 125)
c_text = (220, 223, 228)
c_module = (224, 108, 117)  # red-ish for pyfar

# top bar like an editor / window chrome
draw.rectangle([0, 0, W, 14], fill=(22, 24, 30))
for i, col in enumerate([(237, 106, 94), (245, 191, 79), (97, 194, 90)]):
    draw.ellipse([6 + i * 12, 4, 12 + i * 12, 10], fill=col)

# code lines: (indent_level, list of (text, color))
lines = [
    (0, [("import ", c_kw), ("pyfar", c_module), (" as ", c_kw), ("pf", c_text)]),
    (0, []),
    (0, [("signal ", c_text), ("= ", c_text), ("pf.", c_text), ("Signal(", c_func)]),
    (1, [("data,", c_text)]),
    (1, [("sampling_rate)", c_text)]),
]

y = 30
line_h = 18
start_x = 8
num_x_w = 16

for idx, (indent, parts) in enumerate(lines, start=1):
    # line number
    draw.text((start_x, y), f"{idx}", font=font, fill=c_linenum)
    x = start_x + num_x_w + indent * 12
    for text, color in parts:
        draw.text((x, y), text, font=font, fill=color)
        bbox = draw.textbbox((0, 0), text, font=font)
        x += (bbox[2] - bbox[0])
    y += line_h

img.save("thumbnail_code.png")
