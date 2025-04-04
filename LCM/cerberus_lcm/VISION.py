"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""


from io import BytesIO
import struct

class VISION(object):

    __slots__ = ["id"]

    __typenames__ = ["int8_t"]

    __dimensions__ = [None]

    def __init__(self):
        self.id = 0
        """ LCM Type: int8_t """

    def encode(self):
        buf = BytesIO()
        buf.write(VISION._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">b", self.id))

    @staticmethod
    def decode(data: bytes):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != VISION._get_packed_fingerprint():
            raise ValueError("Decode error")
        return VISION._decode_one(buf)

    @staticmethod
    def _decode_one(buf):
        self = VISION()
        self.id = struct.unpack(">b", buf.read(1))[0]
        return self

    @staticmethod
    def _get_hash_recursive(parents):
        if VISION in parents: return 0
        tmphash = (0x68dd721286446c8) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _packed_fingerprint = None

    @staticmethod
    def _get_packed_fingerprint():
        if VISION._packed_fingerprint is None:
            VISION._packed_fingerprint = struct.pack(">Q", VISION._get_hash_recursive([]))
        return VISION._packed_fingerprint

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", VISION._get_packed_fingerprint())[0]

