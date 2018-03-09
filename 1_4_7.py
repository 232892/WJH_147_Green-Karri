import matplotlib.pyplot as plt
import matplotlib.patches as patches


ax1 = fig1.add_subplot(111, aspect='equal')
ax1.add_patch(
    patches.Rectangle(
        (0.1, 0.1),   # (x,y)
        0.5,          # width
        0.5,          # height
    )
)
ax1.savefig('WolfHead.png', dpi=30, bbox_inches='tight')