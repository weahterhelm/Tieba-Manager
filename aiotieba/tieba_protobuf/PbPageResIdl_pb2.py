# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PbPageResIdl.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import SimpleForum_pb2 as SimpleForum__pb2
from . import Page_pb2 as Page__pb2
from . import Post_pb2 as Post__pb2
from . import ThreadInfo_pb2 as ThreadInfo__pb2
from . import User_pb2 as User__pb2
from . import SubPostList_pb2 as SubPostList__pb2
from . import Error_pb2 as Error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12PbPageResIdl.proto\x1a\x11SimpleForum.proto\x1a\nPage.proto\x1a\nPost.proto\x1a\x10ThreadInfo.proto\x1a\nUser.proto\x1a\x11SubPostList.proto\x1a\x0b\x45rror.proto\"\x94\x02\n\x0cPbPageResIdl\x12\x15\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x06.Error\x12#\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x15.PbPageResIdl.DataRes\x1a\xc7\x01\n\x07\x44\x61taRes\x12\x1b\n\x05\x66orum\x18\x02 \x01(\x0b\x32\x0c.SimpleForum\x12\x13\n\x04page\x18\x03 \x01(\x0b\x32\x05.Page\x12\x18\n\tpost_list\x18\x06 \x03(\x0b\x32\x05.Post\x12\x1b\n\x06thread\x18\x08 \x01(\x0b\x32\x0b.ThreadInfo\x12\x18\n\tuser_list\x18\r \x03(\x0b\x32\x05.User\x12\x1f\n\rsub_post_list\x18\x0f \x01(\x0b\x32\x08.SubPost\x12\x18\n\x10has_fold_comment\x18\x44 \x01(\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PbPageResIdl_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PBPAGERESIDL._serialized_start=128
  _PBPAGERESIDL._serialized_end=404
  _PBPAGERESIDL_DATARES._serialized_start=205
  _PBPAGERESIDL_DATARES._serialized_end=404
# @@protoc_insertion_point(module_scope)
