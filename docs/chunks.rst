Blocks and Chunks
=================

.. currentmodule:: mncrft.chunk

Minecraft uses tightly-packed arrays to store data like light levels,
heightmaps and block data. mncrft can read and write these formats in both
`Chunk Data`_  packets and ``.mca`` files. Two classes are available for
working with this data:

.. autoclass:: PackedArray
    :members:

.. autoclass:: BlockArray
    :members:


Regions
-------

mncrft can load and save data from the ``.mca`` format via the
:class:`~mncrft.nbt.RegionFile` class. NBT tags such as ``"BlockStates"``,
``"BlockLight"``, ``"SkyLight"`` and heightmaps such as ``"MOTION_BLOCKING"``
make their values available as :class:`PackedArray` objects.

Use :meth:`BlockArray.from_nbt` with a
:class:`~mncrft.registry.LookupRegistry` to create a block array backed
by NBT data. Modifications to the block array will automatically be reflected
in the NBT data, and vice versa.

Putting these pieces together, the following function could be used to set a
block in an existing region file::

    import os.path

    from mncrft.nbt import RegionFile
    from mncrft.chunk import BlockArray
    from mncrft.registry import LookupRegistry

    server_path = "/path/to/server"
    region_path = os.path.join(server_path, "world", "region")
    jar_path = os.path.join(server_path, "minecraft_server.jar")
    registry = LookupRegistry.from_jar(jar_path)

    def set_block(x, y, z, block):
        rx, x = divmod(x, 512)
        rz, z = divmod(z, 512)
        cx, x = divmod(x, 16)
        cy, y = divmod(y, 16)
        cz, z = divmod(z, 16)

        region_name = "r.%d.%d.mca" % (rx, rz)
        with RegionFile(os.path.join(region_path, region_name)) as region:
            chunk, section = region.load_chunk_section(cx, cy, cz)
            blocks = BlockArray.from_nbt(section, registry)
            blocks[256 * y + 16 * z + x] = block
            region.save_chunk(chunk)


    set_block(10, 80, 40, {'name': 'minecraft:bedrock'})

.. _Chunk Data: http://wiki.vg/Protocol#Chunk_Data
