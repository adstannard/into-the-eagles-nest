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

**Disk Image t4**  
Basement: 6A70-725F  
Ground: 7260-684F  
Floor1: 6850-704F  
Floor2: 7040-7930  

**BLOCKS**

Block 0x01 - 5BD8 start  ->  Black 0x02 - 5BFC end
Block 0x03 - 5E00 start  ->  Block 0x22 - 5FFC end  
Block 0x23 - 5000 start  ->  Block 0x42 - 51FC end  
Block 0x43 - 5400 start  ->  Block 0x62 - 55FC end  
Block 0x63 - 5830 start  ->  Block 0x7F - 59CC end  
