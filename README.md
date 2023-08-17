# Roll Tool
A NES ROM that shows inputs with extremely high precision, targeted towards high level competitors in NES Tetris. Created using the wonderful NESFab programming language.

Using the MMC3's scanline counter, this ROM polls the controller 16 times each frame, for a resulting poll rate of around `16*60.0988Hz=961.5808Hz`, which rivals the `1000Hz` rate you might get from a USB adapter.

To download the ROM, simply head over to the [release page](https://github.com/fractal161/rollTool/releases) and download the most recent version of `roll.nes`. A discussion of how to use the ROM can be found in the next section.

## Availability

rollTool aims to work on a large variety of platforms. However, due to the precise nature of this project, perfect functionality across a variety of platforms is difficult to coordinate. For example, basically all NES emulators used for actually playing games only poll the OS layer once per frame, so the tool will not work the way it should on any computer[^1].

Instead, the recommended way to use rollTool is with a console+cartridge setup. But even this is not clear-cut, as many alternatives exist for both the console and the cartridge. This can present problems of its own; for example, some clone consoles may not handle [illegal instructions](https://www.masswerk.at/nowgobang/2021/6502-illegal-opcodes) correctly, which NESFab makes heavy use of to generate optimal code.

Since I personally only have regular access to a retroUSB AVS, that's the only platform I can guarantee perfect functionality for. When releasing new versions, I will attempt to contact people with various common setups for additional testing, and this will be reflected in the release notes. The same goes for cartridges; I only have an Everdrive N8, but will attempt to test releases using the Kryzsiocart, as well as on other flash carts that I can contact.

If you aren't able to get rollTool working with your unique setup, check the comments of [this issue](https://github.com/fractal161/rollTool/issues/1), which tracks a working list of such problems.

[^1]: The information will still be correct, but with a greatly reduced level of accuracy.

## Build Process
This ROM is built with a development build of NESFab 0.9, which is included in this repository as a submodule. Use `git clone --recurse-submodules https://github.com/fractal161/rollTool` to install everything with one command. To build the compiler, `cd` into the `nesfab/` directory and run `make release`. If you have already installed NESFab elsewhere and wish to use that, you'll need to configure the `Makefile` to point to your copy of the `nesfab` executable and configure `roll.cfg` to point to the necessary library files. However, this is discouraged, as different versions of the compiler tend to introduce subtle issues (e.g. small amounts of jittering) since some of the logic is sensitive to timing info.

In addition, you'll need some version of `python`, along with `opencv2` if you wish to build `chr/hz.png` yourself (though this isn't necessary since the file is already provided.)

From there, run `make` in the root directory and you're done!
