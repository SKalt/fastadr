# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities

import types

__config__ = pulumi.Config('authentik')


class _ExportableConfig(types.ModuleType):
    @property
    def headers(self) -> Optional[str]:
        """
        Optional HTTP headers sent with every request
        """
        return __config__.get('headers')

    @property
    def insecure(self) -> Optional[bool]:
        """
        Whether to skip TLS verification, can optionally be passed as `AUTHENTIK_INSECURE` environmental variable
        """
        return __config__.get_bool('insecure')

    @property
    def token(self) -> Optional[str]:
        """
        The authentik API token, can optionally be passed as `AUTHENTIK_TOKEN` environmental variable
        """
        return __config__.get('token')

    @property
    def url(self) -> Optional[str]:
        """
        The authentik API endpoint, can optionally be passed as `AUTHENTIK_URL` environmental variable
        """
        return __config__.get('url')

