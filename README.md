# Roll Tool
A NES ROM that shows inputs with extremely high precision, targeted towards high level competitors in NES Tetris. Created using the wonderful NESFab.

Using the MMC3's scanline counter, this ROM polls the controller 16 times each frame[^1], for a resulting poll rate of around `16*60.0988Hz=961.5808Hz`, which rivals the `1000Hz` rate you might get from a USB adapter.

[^1] Technically 32, since two polls in succession are used as a primitive debouncing mechanic.

## Build Process
This ROM is built using NESFab 0.6, which can be found [here](https://github.com/pubby/nesfab/releases/tag/v0.6). Future versions may still work, but no guarantees are made.

You'll need to do two things with the release. First, make sure that the `nesfab` binary is installed on your path. Second, include its source code as a folder titled `nesfab/` in the root directory. This last step is so we can import the standard library; you're welcome to put this wherever you desire, so long as `roll.cfg` is updated to reflect this.

From there, run `make` in the root directory and you're done!
