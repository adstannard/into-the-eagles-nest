# How to Change Palette Colors - Visual Guide

## Step-by-Step Example: Changing Green to Blue

### 1. Find the Palette Section in the Script

Look for this section near the top of `amstrad_cpc_mode0_converter.py`:

```python
# ============================================================================
# PALETTE CONFIGURATION - MODIFY THESE VALUES
# ============================================================================
PALETTE_COLORS = [
    (0x00, 0x00, 0x00),  # Index 0  - Black
    (0x00, 0x00, 0x80),  # Index 1  - Blue
    # ... more colors ...
    (0x00, 0xFF, 0x00),  # Index 9  - Green  ← THIS ONE!
    # ... more colors ...
]
```

### 2. Understand RGB Format

Each color is defined as: `(Red, Green, Blue)`

```
(0x00, 0xFF, 0x00)
  │     │     │
  │     │     └─── Blue value  (0-255)
  │     └───────── Green value (0-255)
  └─────────────── Red value   (0-255)

0x00 = 0 in decimal
0xFF = 255 in decimal
```

### 3. Change the Values

**BEFORE** (Green):
```python
(0x00, 0xFF, 0x00),  # Index 9  - Green
  ↑     ↑     ↑
  Red=0 Green=255 Blue=0  → Pure green
```

**AFTER** (Blue):
```python
(0x00, 0x00, 0xFF),  # Index 9  - Blue
  ↑     ↑     ↑
  Red=0 Green=0 Blue=255  → Pure blue
```

### 4. Common Color Values

Here are some useful colors you can copy/paste:

```python
# Primary Colors
(0xFF, 0x00, 0x00),  # Red
(0x00, 0xFF, 0x00),  # Green
(0x00, 0x00, 0xFF),  # Blue

# Common Colors
(0x00, 0x00, 0x00),  # Black
(0xFF, 0xFF, 0xFF),  # White
(0x80, 0x80, 0x80),  # Grey
(0xFF, 0xFF, 0x00),  # Yellow
(0xFF, 0x00, 0xFF),  # Magenta
(0x00, 0xFF, 0xFF),  # Cyan

# Darker Versions
(0x00, 0x00, 0x80),  # Dark Blue
(0x00, 0x80, 0x00),  # Dark Green
(0x80, 0x00, 0x00),  # Dark Red

# Lighter Versions
(0x80, 0x80, 0xFF),  # Light Blue
(0x80, 0xFF, 0x80),  # Light Green
(0xFF, 0x80, 0x80),  # Light Red

# Browns/Oranges (for stone tiles)
(0x80, 0x40, 0x00),  # Brown
(0xFF, 0x80, 0x00),  # Orange
(0xA0, 0x60, 0x20),  # Light Brown
```

## Complete Example: Editing Multiple Colors

Let's say your tile uses palette indices 0, 1, 2, and 3, and you want them to be:
- Index 0: Black (background)
- Index 1: Dark Blue
- Index 2: Light Blue
- Index 3: White (highlights)

### Find These Lines:

```python
PALETTE_COLORS = [
    (0x00, 0x00, 0x00),  # Index 0  - Black        ← Keep as is
    (0x00, 0x00, 0x80),  # Index 1  - Blue         ← Keep as is
    (0x00, 0x00, 0xFF),  # Index 2  - Bright Blue  ← Keep as is
    (0xFF, 0x00, 0x00),  # Index 3  - Red          ← CHANGE THIS
    # ... rest unchanged ...
]
```

### Change to:

```python
PALETTE_COLORS = [
    (0x00, 0x00, 0x00),  # Index 0  - Black
    (0x00, 0x00, 0x80),  # Index 1  - Dark Blue
    (0x80, 0x80, 0xFF),  # Index 2  - Light Blue   ← CHANGED!
    (0xFF, 0xFF, 0xFF),  # Index 3  - White        ← CHANGED!
    # ... rest unchanged ...
]
```

## How to Find Which Indices to Change

### Method 1: Look at the Test Output

Run the script and check what it prints:

```
Decoded tile (palette indices):
Row 0: 0 0 0 0 0 0 0 0
Row 1: 4 1 C 3 C 3 0 0
       ↑ ↑ ↑ ↑
       These are the palette indices your tile uses!
```

In this example, the tile uses indices: 0, 1, 3, 4, 8, C (12)

### Method 2: Look at Your PNG

1. Run the script once with default palette
2. Look at `test_tile.png`
3. Count how many different colors you see
4. Those are the indices you need to change

## RGB Color Picker Tips

If you want a specific color:

### Using Hex Colors (from a screenshot tool):

If you have a hex color like `#4A7BA7`:

```
#4A7BA7
 ││ ││ ││
 ││ ││ └┴─ Blue  = 0xA7 = 167
 ││ └┴──── Green = 0x7B = 123  
 └┴─────── Red   = 0x4A = 74

In Python:
(0x4A, 0x7B, 0xA7)  or  (74, 123, 167)
```

### Using Decimal RGB:

If you have RGB(74, 123, 167):

```python
(74, 123, 167)  # Can use decimal directly!
```

Both formats work:
```python
(0xFF, 0x80, 0x40)  # Hexadecimal
(255, 128, 64)      # Decimal - same color!
```

## Quick Reference Chart

| What You See | Palette Index | Change This Line |
|--------------|---------------|------------------|
| Background color | Usually 0 | `PALETTE_COLORS[0]` = line 1 |
| First color | Usually 1 | `PALETTE_COLORS[1]` = line 2 |
| Second color | Usually 2 | `PALETTE_COLORS[2]` = line 3 |
| ... | ... | ... |

## After Changing Colors

1. **Save the file** (`amstrad_cpc_mode0_converter.py`)
2. **Run it again**: `python amstrad_cpc_mode0_converter.py`
3. **Check the output**: Look at `test_tile.png`
4. **Repeat** until colors match your reference

## Pro Tip: Test One Tile First

Before processing all 128 tiles, test with just one:

```python
# In the script, temporarily change:
TOTAL_TILES = 1  # Instead of 128

# This creates only tile_00.png - much faster for testing colors!
# Once colors are right, change back to 128
```

## Common Mistakes to Avoid

❌ **Wrong:** Changing the wrong index
```python
# Your tile uses index 2, but you changed index 9
# → No visible change!
```

✓ **Right:** Check which indices your tile actually uses first

❌ **Wrong:** Invalid color values
```python
(0xFF, 0x100, 0x00)  # 0x100 > 255 = ERROR!
```

✓ **Right:** Keep values between 0x00 (0) and 0xFF (255)

❌ **Wrong:** Missing comma
```python
(0xFF, 0x80 0x40),  # Missing comma between values
```

✓ **Right:** Use commas between all three values
```python
(0xFF, 0x80, 0x40),
```

## Example: Your Stone Tile

Based on your test hex showing indices like 0, 1, 2, 3, 4, 8, C (12), you might want:

```python
PALETTE_COLORS = [
    (0x00, 0x00, 0x00),  # 0 - Black (background)
    (0x00, 0x60, 0xC0),  # 1 - Dark Blue
    (0x40, 0xA0, 0xE0),  # 2 - Medium Blue  
    (0x80, 0xC0, 0xFF),  # 3 - Light Blue
    (0x00, 0x40, 0x80),  # 4 - Darker Blue
    (0xFF, 0x00, 0xFF),  # 5 - (unused in your tile)
    (0xFF, 0x80, 0x00),  # 6 - (unused)
    (0xFF, 0x80, 0x80),  # 7 - (unused)
    (0x60, 0xB0, 0xF0),  # 8 - Sky Blue
    (0x00, 0xFF, 0x00),  # 9 - (unused)
    (0x00, 0xFF, 0x80),  # 10 - (unused)
    (0x00, 0xFF, 0xFF),  # 11 - (unused)
    (0xA0, 0xD0, 0xFF),  # C (12) - Very Light Blue
    (0xFF, 0xFF, 0xFF),  # D (13) - White
    (0xFF, 0xFF, 0x80),  # E (14) - (unused)
    (0x80, 0x80, 0x80),  # F (15) - (unused)
]
```

This would give you a blue stone/rock gradient suitable for the pattern in your test data.
