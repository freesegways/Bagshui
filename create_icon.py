import os
from PIL import Image, ImageDraw

def create_stack_icon():
    # WoW icons are typically 64x64
    size = (64, 64)
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Gold color from the screenshot (approximate)
    gold = (255, 204, 0, 255)
    # Darker border/shadow for depth
    dark_gold = (180, 140, 0, 255)
    
    # Draw a "Stack" of items
    # We will draw 3 boxes stacked on top of each other
    
    # Box dimensions
    box_w = 28
    box_h = 10
    spacing = 4
    start_x = (size[0] - box_w) // 2
    start_y = 12

    for i in range(3):
        y = start_y + (i * (box_h + spacing))
        
        # Draw shadow/border
        draw.rectangle([start_x - 2, y - 2, start_x + box_w + 2, y + box_h + 2], fill=None, outline=dark_gold, width=2)
        
        # Draw box body
        draw.rectangle([start_x, y, start_x + box_w, y + box_h], fill=gold)
        
        # Add a little highlight
        draw.line([start_x + 2, y + 2, start_x + box_w - 2, y + 2], fill=(255, 255, 150, 255), width=1)

    # Add a small "arrow" or indicator effectively showing "compress" or "stack"
    # Maybe arrows pointing inward or just the stack itself is enough.
    # Let's add a small 'plus' or sparkles to indicate action? 
    # The user's screenshot shows simple icons. "Restack" usually puts things in order.
    # "Stack Stacks" combines them.
    # Let's just stick to the clean stack for now, maybe with a bracket.
    
    # Draw a bracket on the right to imply they are a group
    bracket_x = start_x + box_w + 8
    bracket_top = start_y
    bracket_bottom = start_y + (2 * (box_h + spacing)) + box_h
    
    # draw.line([bracket_x, bracket_top, bracket_x + 4, bracket_top], fill=gold, width=3)
    # draw.line([bracket_x + 4, bracket_top, bracket_x + 4, bracket_bottom], fill=gold, width=3)
    # draw.line([bracket_x, bracket_bottom, bracket_x + 4, bracket_bottom], fill=gold, width=3)

    # Save
    output_path = r"c:\Program Files (x86)\TurtleWoW\Interface\AddOns\Bagshui\Images\Icons\StackStacks.tga"
    img.save(output_path)
    print(f"Created {output_path}")

try:
    create_stack_icon()
except Exception as e:
    print(f"Error: {e}")
