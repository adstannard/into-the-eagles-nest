# Map Data #

From looking at the Amiga data (Castle 1 of 2) and comparing to the Amstrad CPC (only one castle in game) the structure of the levels:

168 rows x 96 columns of tiles = 16,128 tiles
Each tile is 8x8 pixels in Mode 0

Map data is stored in blocks 42 x 24 with each block representing a (4 x 4) 16 tile area. This allows for map data compression.

The Blocks are then stored in 16 bytes representing each of the tiles.

For example block 0x05 is a solid 4x4 16 tile area of castle wall. That block is made up of tiles 0x01 and 0x02 that are the 2 stone wall blocks:

01  01  01  01  
02  02  02  02  
01  01  01  01  
02  02  02  02  
