Registry
========

.. currentmodule:: mncrft.buffer

mncrft can be told to encode/decode block, item and other information by
setting the :attr:`~Buffer.registry` attribute on the in-use buffer.

- :meth:`~Buffer.unpack_slot()` and :meth:`~Buffer.pack_slot()`
- :meth:`~Buffer.unpack_block()` and :meth:`~Buffer.pack_block()`
- :meth:`~Buffer.unpack_entity_metadata()` and
  :meth:`~Buffer.pack_entity_metadata()`
- :meth:`~Buffer.unpack_chunk_section()` and
  :meth:`~Buffer.pack_chunk_section()`
- :meth:`~Buffer.unpack_villager()` and :meth:`~Buffer.pack_villager()`
- :meth:`~Buffer.unpack_particle()` and :meth:`~Buffer.pack_particle()`

.. module:: mncrft.registry

All registry objects have the following methods:

.. automethod:: Registry.encode
.. automethod:: Registry.decode
.. automethod:: Registry.encode_block
.. automethod:: Registry.decode_block
.. automethod:: Registry.is_air_block

mncrft supports the following registry types:

.. autoclass:: OpaqueRegistry
.. autoclass:: BitShiftRegistry
.. autoclass:: LookupRegistry
    :members: from_jar, from_json
