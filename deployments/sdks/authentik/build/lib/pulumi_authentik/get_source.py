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
from . import _utilities

__all__ = [
    'GetSourceResult',
    'AwaitableGetSourceResult',
    'get_source',
    'get_source_output',
]

@pulumi.output_type
class GetSourceResult:
    """
    A collection of values returned by getSource.
    """
    def __init__(__self__, id=None, managed=None, name=None, slug=None, uuid=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed and not isinstance(managed, str):
            raise TypeError("Expected argument 'managed' to be a str")
        pulumi.set(__self__, "managed", managed)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if slug and not isinstance(slug, str):
            raise TypeError("Expected argument 'slug' to be a str")
        pulumi.set(__self__, "slug", slug)
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def managed(self) -> str:
        return pulumi.get(self, "managed")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def slug(self) -> str:
        return pulumi.get(self, "slug")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        return pulumi.get(self, "uuid")


class AwaitableGetSourceResult(GetSourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSourceResult(
            id=self.id,
            managed=self.managed,
            name=self.name,
            slug=self.slug,
            uuid=self.uuid)


def get_source(id: Optional[str] = None,
               managed: Optional[str] = None,
               slug: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSourceResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['managed'] = managed
    __args__['slug'] = slug
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('authentik:index/getSource:getSource', __args__, opts=opts, typ=GetSourceResult, package_ref=_utilities.get_package()).value

    return AwaitableGetSourceResult(
        id=pulumi.get(__ret__, 'id'),
        managed=pulumi.get(__ret__, 'managed'),
        name=pulumi.get(__ret__, 'name'),
        slug=pulumi.get(__ret__, 'slug'),
        uuid=pulumi.get(__ret__, 'uuid'))
def get_source_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                      managed: Optional[pulumi.Input[Optional[str]]] = None,
                      slug: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSourceResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['managed'] = managed
    __args__['slug'] = slug
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('authentik:index/getSource:getSource', __args__, opts=opts, typ=GetSourceResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetSourceResult(
        id=pulumi.get(__response__, 'id'),
        managed=pulumi.get(__response__, 'managed'),
        name=pulumi.get(__response__, 'name'),
        slug=pulumi.get(__response__, 'slug'),
        uuid=pulumi.get(__response__, 'uuid')))
