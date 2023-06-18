# Roll Tool
A NES ROM that shows inputs with extremely high precision, targeted towards high level competitors in NES Tetris. Created using the wonderful NESFab.

Using the MMC3's scanline counter, this ROM polls the controller 16 times each frame, for a resulting poll rate of around `16*60.0988Hz=961.5808Hz`, which rivals the `1000Hz` rate you might get from a USB adapter.

## Build Process
This ROM is built with a development build of NESFab 0.8, which is included in this repository as a submodule. Use `git clone --recurse-submodules https://github.com/fractal161/rollTool` to install everything with one command. To build the compiler, `cd` into the `nesfab/` directory and run `make release`. If you have already installed NESFab elsewhere and wish to use that, you'll need to configure the `Makefile` to point to your copy of the `nesfab` executable and configure `roll.cfg` to point to the necessary library files. However, this is discouraged, as different versions of the compiler tend to introduce subtle issues (e.g. small amounts of jittering) since some of the logic is sensitive to timing info.

In addition, you'll need some version of `python`, along with `opencv2` if you wish to build `chr/hz.png` yourself (though this isn't necessary since the file is already provided.)

From there, run `make` in the root directory and you're done!
