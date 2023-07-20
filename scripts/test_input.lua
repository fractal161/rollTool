-- Simulate the following sequence of left button presses
-- order is right, nothing, right, and so on
inputs = { 7, 8 }
subframe_count = inputs[1]
input_index = 1

pads_addr = emu.getLabelAddress("pads@0")

function set_polls()
    if #inputs < input_index then
        return
    end;
    if input_index % 2 == 1 then
        emu.write(pads_addr, 1, emu.memType.cpuDebug)
    else
        emu.write(pads_addr, 0, emu.memType.cpuDebug)
    end
    subframe_count = subframe_count - 1
    if subframe_count == 0 then
        input_index = input_index + 1
        subframe_count = inputs[input_index]
    end
end

emu.addMemoryCallback(set_polls, emu.memCallbackType.cpuWrite, 0x4444)
