"""
castle1_objects.py
==================
Castle 1 object table extracted from the Amiga ASM (OBJTBL0).

Each entry is 7 bytes in the original:
  Byte 0: runtime X  (0x00 at rest — overwritten from byte 4 on load)
  Byte 1: runtime Y  (0x00 at rest — overwritten from byte 5 on load)
  Byte 2: runtime level (0x00 at rest — overwritten from byte 6 on load)
  Byte 3: flags | type  (bit 7 = collected flag; low nibble = type 0–9)
  Byte 4: spawn X  — tile column (0–95)
  Byte 5: spawn Y  — tile row in Amiga coords (0 = top of map, 167 = bottom)
  Byte 6: level    — which floor this object lives on (0=ground, 1=basement,
                     2=first, 3=second)

The first three bytes are runtime state that the game resets on load.
We only need bytes 3–6 (type, x, y, level).

Object types (low nibble of byte 3):
  0 = Ammo box     tiles: 0x60 (top-left), 0x61 (top-right)
  1 = Painting     tiles: 0x62 (top),      0x63 (bottom)
  2 = Vase         tiles: 0x64 (top),      0x65 (bottom)
  3 = BUG          (unused placeholder — writes no tiles)
  4 = Cold Food    tiles: 0x69 (top),      0x6A (bottom)
  5 = Dynamite     (in crates, never as standalone object)
  6 = First Aid    tiles: 0x6C (top),      0x6D (bottom)
  7 = Pendant      tiles: 0x6E (top),      0x6F (bottom)
  8 = Lift Pass    tile:  0x6B (single)
  9 = Door Key     (placed directly in block map — not via object table)

Note: Keys (type 9) and some ammo are already baked into the .lvl block data.
      Everything else listed here needs patching into the level files.

Source: OBJTBL0 label in __Into_The_Eagle_s_Nest_Amiga.txt
"""

# Raw entries from OBJTBL0 in the ASM.
# Each tuple: (type_nibble, spawn_x, spawn_y, level)
# Bytes 0–2 (runtime state, always 0x00 at rest) are discarded.
# Byte 3 low nibble = type, byte 4 = x, byte 5 = y, byte 6 = level.

CASTLE1_OBJECTS = [
    # --- Level 0 (basement) ---
    # (type, x,    y,    level)  — name for reference
    (8, 0x57, 0x8E, 0),   # Lift Pass
    (4, 0x04, 0x0F, 0),   # Cold Food
    (7, 0x3A, 0x81, 0),   # Pendant
    (7, 0x2A, 0x81, 0),   # Pendant
    (7, 0x4C, 0x9A, 0),   # Pendant
    (6, 0x52, 0xA1, 0),   # First Aid
    (6, 0x16, 0xA2, 0),   # First Aid
    (1, 0x35, 0x9A, 0),   # Painting
    (1, 0x45, 0x85, 0),   # Painting
    (1, 0x05, 0x8E, 0),   # Painting
    (1, 0x06, 0x5E, 0),   # Painting
    (1, 0x08, 0x5E, 0),   # Painting
    (1, 0x0A, 0x5E, 0),   # Painting
    (1, 0x0C, 0x5E, 0),   # Painting
    (1, 0x07, 0x51, 0),   # Painting
    (1, 0x25, 0x0C, 0),   # Painting
    (1, 0x35, 0x05, 0),   # Painting
    (7, 0x24, 0x08, 0),   # Pendant
    (7, 0x1E, 0x05, 0),   # Pendant
    (7, 0x3D, 0x11, 0),   # Pendant
    (7, 0x4E, 0x05, 0),   # Pendant
    (7, 0x37, 0x3D, 0),   # Pendant
    # --- Level 1 (ground floor) ---
    (7, 0x1A, 0x29, 1),   # Pendant
    (7, 0x12, 0x15, 1),   # Pendant
    (7, 0x3E, 0x06, 1),   # Pendant
    (7, 0x4D, 0x07, 1),   # Pendant
    (7, 0x12, 0x15, 1),   # Pendant (duplicate coords — both in original)
    (7, 0x3E, 0x06, 1),   # Pendant (duplicate coords)
    (7, 0x4D, 0x07, 1),   # Pendant (duplicate coords)
    (7, 0x1A, 0x8D, 1),   # Pendant
    (7, 0x21, 0x8C, 1),   # Pendant
    (4, 0x2D, 0x76, 1),   # Cold Food
    (7, 0x43, 0x58, 1),   # Pendant
    (6, 0x25, 0x86, 1),   # First Aid
    (8, 0x22, 0x8F, 1),   # Lift Pass
    (6, 0x11, 0x74, 1),   # First Aid
    (6, 0x09, 0x7A, 1),   # First Aid
    (6, 0x41, 0x58, 1),   # First Aid
    (1, 0x49, 0x25, 1),   # Painting
    (2, 0x49, 0x1F, 1),   # Vase
    (6, 0x5A, 0x64, 1),   # First Aid
    (4, 0x2B, 0x3B, 1),   # Cold Food
    (4, 0x32, 0x4B, 1),   # Cold Food
    (4, 0x49, 0x22, 1),   # Cold Food
    (4, 0x5A, 0x0C, 1),   # Cold Food
    (4, 0x51, 0x6C, 1),   # Cold Food
    (7, 0x1E, 0x47, 1),   # Pendant
    (4, 0x07, 0x43, 1),   # Cold Food
    (7, 0x0D, 0x3D, 1),   # Pendant
    (7, 0x0D, 0x45, 1),   # Pendant
    (7, 0x08, 0x45, 1),   # Pendant
    (7, 0x0D, 0x56, 1),   # Pendant
    (2, 0x21, 0x4A, 1),   # Vase
    (6, 0x35, 0x4B, 1),   # First Aid
    (6, 0x3D, 0x18, 1),   # First Aid
    (6, 0x5A, 0x42, 1),   # First Aid
    (6, 0x59, 0x9F, 1),   # First Aid
    (6, 0x41, 0x58, 1),   # First Aid (duplicate coords with above)
    (7, 0x12, 0x1C, 1),   # Pendant
    (7, 0x3A, 0x05, 1),   # Pendant
    # --- Level 2 (first floor) ---
    (1, 0x3A, 0x24, 2),   # Painting
    (3, 0x02, 0x36, 2),   # BUG (writes no tiles — placeholder)
    (6, 0x4D, 0x12, 2),   # First Aid
    (7, 0x4D, 0x38, 2),   # Pendant
    (8, 0x33, 0x04, 2),   # Lift Pass
    (4, 0x05, 0x39, 2),   # Cold Food
    (4, 0x08, 0x1C, 2),   # Cold Food
    (4, 0x49, 0x11, 2),   # Cold Food
    (4, 0x4A, 0x14, 2),   # Cold Food
    (4, 0x09, 0x50, 2),   # Cold Food
    (4, 0x56, 0x25, 2),   # Cold Food
    (4, 0x36, 0x79, 2),   # Cold Food
    (6, 0x38, 0xA2, 2),   # First Aid
    (6, 0x55, 0xA2, 2),   # First Aid
    (1, 0x15, 0x51, 2),   # Painting
    (1, 0x42, 0x64, 2),   # Painting
    (2, 0x5A, 0x60, 2),   # Vase
    (7, 0x42, 0x74, 2),   # Pendant
    (7, 0x40, 0x38, 2),   # Pendant
    (7, 0x11, 0x71, 2),   # Pendant
    (7, 0x14, 0x54, 2),   # Pendant
    (7, 0x0A, 0x69, 2),   # Pendant
    (7, 0x27, 0x3D, 2),   # Pendant
    (7, 0x4C, 0x28, 2),   # Pendant
    (7, 0x16, 0x08, 2),   # Pendant
    (1, 0x02, 0x5D, 2),   # Painting
    (1, 0x1D, 0x59, 2),   # Painting
    (1, 0x2E, 0x38, 2),   # Painting
    (1, 0x59, 0x3D, 2),   # Painting
    (1, 0x57, 0x75, 2),   # Painting
    # --- Level 3 (second floor) ---
    (8, 0x06, 0x08, 3),   # Lift Pass
    (1, 0x24, 0x7D, 3),   # Painting
    (1, 0x52, 0x05, 3),   # Painting
    (1, 0x5A, 0x3D, 3),   # Painting
    (2, 0x1E, 0x05, 3),   # Vase
    (2, 0x19, 0x05, 3),   # Vase
    (2, 0x07, 0x1D, 3),   # Vase
    (7, 0x47, 0x8A, 3),   # Pendant
    (7, 0x46, 0x71, 3),   # Pendant
    (7, 0x46, 0x90, 3),   # Pendant
    (7, 0x3D, 0x98, 3),   # Pendant
    (4, 0x5A, 0x0C, 3),   # Cold Food
    (4, 0x5A, 0x29, 3),   # Cold Food
    (4, 0x5A, 0x84, 3),   # Cold Food
    (7, 0x23, 0xA1, 3),   # Pendant
    (7, 0x27, 0xA1, 3),   # Pendant
    (7, 0x2B, 0xA1, 3),   # Pendant
    (7, 0x1E, 0x13, 3),   # Pendant
    (7, 0x20, 0x12, 3),   # Pendant
    (7, 0x1D, 0x0F, 3),   # Pendant
    (7, 0x4D, 0x32, 3),   # Pendant
    (1, 0x49, 0x05, 3),   # Painting
]

# Human-readable names for each type number
TYPE_NAMES = {
    0: "Ammo",
    1: "Painting",
    2: "Vase",
    3: "BUG",
    4: "ColdFood",
    5: "Dynamite",
    6: "FirstAid",
    7: "Pendant",
    8: "LiftPass",
    9: "Key",
}

# Level file names in order (index = level number)
LEVEL_FILES = ["basement.lvl", "ground.lvl", "first.lvl", "second.lvl"]
LEVEL_NAMES = ["Basement", "Ground Floor", "First Floor", "Second Floor"]
