NBT
===

.. module:: mncrft.nbt

mncrft implements the Named Binary Tag (NBT) format. The following tag types
are available from the :mod:`mncrft.nbt` module:

.. list-table::
    :header-rows: 1

    - * Class
      * Value type
    - * ``TagByte``
      * ``int``
    - * ``TagShort``
      * ``int``
    - * ``TagInt``
      * ``int``
    - * ``TagLong``
      * ``int``
    - * ``TagFloat``
      * ``float``
    - * ``TagDouble``
      * ``float``
    - * ``TagByteArray``
      * :class:`~mncrft.chunk.PackedArray` with 8-bit sectors
    - * ``TagIntArray``
      * :class:`~mncrft.chunk.PackedArray` with 32-bit sectors
    - * ``TagLongArray``
      * :class:`~mncrft.chunk.PackedArray` with 64-bit sectors
    - * ``TagString``
      * ``str`` (py3) or ``unicode`` (py2)
    - * ``TagList``
      * ``list`` of tags.
    - * ``TagCompound``
      * ``dict`` of names and tags.
    - * ``TagRoot``
      * ``dict`` containing a single name and tag.

.. note::
    Unlike some other NBT libraries, a tag's name is stored by its *parent* -
    either a ``TagRoot`` or a ``TagCompound``. A tag when considered alone is
    always nameless.


Tags
----

All tag types have the following attributes and methods:

.. method:: Tag.__init__(value)

    Creates a tag object from the given value.

.. classmethod:: Tag.from_bytes(bytes)

    Creates a tag object from data at the beginning of the supplied byte
    string.

.. classmethod:: Tag.from_buff(buff)

    Creates a tag object from data at the beginning of the supplied
    :class:`~mncrft.buffer.Buffer` object.

.. method:: Tag.to_obj

    Returns a friendly representation of the tag using only basic Python
    datatypes. This is a lossy operation, as Python has fewer data types than
    NBT.

.. method:: Tag.to_bytes

    Returns a packed version of the tag as a byte string.

.. attribute:: Tag.value

    The value of the tag.


Files
-----

You can open an NBT file using the ``NBTFile`` class.

.. autoclass:: NBTFile
    :members:
    :undoc-members:

You can open Minecraft 1.16+ world files (``.mca``) using the ``RegionFile``
class, which can also function as a context manager. See :doc:`chunks` for
information on loading block and light data.

.. autoclass:: RegionFile
    :members:

Debugging
---------

Call ``repr(tag)`` or ``alt_repr(tag)`` for a human-readable representation of
a tag.

.. autofunction:: alt_repr