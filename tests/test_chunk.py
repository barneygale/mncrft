import os.path

import bitstring

from mncrft.chunk import BlockArray
from mncrft.registry import OpaqueRegistry
from mncrft.nbt import TagCompound

TagCompound.preserve_order = True # for testing purposes.

root_path = os.path.dirname(__file__)
chunk_path = os.path.join(root_path, "chunk.bin")


def test_wikivg_example():
    # Example from https://wiki.vg/Chunk_Format#Example
    data = bitstring.BitArray(length=13*4096)
    data[0:64]   = '0b0000000000100000100001100011000101001000010000011000100001000001'
    data[64:128] = '0b0000000100000001100010100111001001100000111101101000110010000111'
    data = data.bytes

    blocks = BlockArray.from_bytes(data, 5, OpaqueRegistry(13), [])
    assert blocks[:24] == [
        1, 2, 2, 3, 4, 4, 5, 6, 6, 4, 8, 0, 7,
        4, 3, 13, 15, 16, 9, 14, 10, 12, 0, 2]


def test_chunk_internals():
    blocks = BlockArray.empty(OpaqueRegistry(13))
    storage = blocks.storage

    # Accumulate blocks
    added = []
    for i in range(300):
        blocks[i] = i
        added.append(i)

        assert blocks[:i+1] == added

        if i < 256:
            assert len(blocks.palette) == i + 1
            if i < 16:
                assert storage.value_width == 4
            elif i < 32:
                assert storage.value_width == 5
            elif i < 64:
                assert storage.value_width == 6
            elif i < 128:
                assert storage.value_width == 7
            else:
                assert storage.value_width == 8
        else:
            assert blocks.palette == []
            assert storage.value_width == 13

    # Zero the first 100 blocks
    for i in range(100):
        blocks[i] = 0
    blocks.repack()
    assert len(blocks.palette) == 201
    assert storage.value_width == 8

    # Zero blocks 100-199
    for i in range(100, 200):
        blocks[i] = 0
    blocks.repack()
    assert len(blocks.palette) == 101
    assert storage.value_width == 7

    # Zero blocks 205 - 300
    for i in range (205, 300):
        blocks[i] = 0
    blocks.repack()
    assert len(blocks.palette) == 6
    assert storage.value_width == 4

    # Check value
    for i in range(4096):
        if 200 <= i < 205:
            assert blocks[i] == i
        else:
            assert blocks[i] == 0
