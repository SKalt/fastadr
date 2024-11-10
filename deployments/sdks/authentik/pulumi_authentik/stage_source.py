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

__all__ = ['StageSourceArgs', 'StageSource']

@pulumi.input_type
class StageSourceArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 resume_timeout: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 stage_source_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StageSource resource.
        :param pulumi.Input[str] resume_timeout: Defaults to `minutes=10`.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resume_timeout is not None:
            pulumi.set(__self__, "resume_timeout", resume_timeout)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if stage_source_id is not None:
            pulumi.set(__self__, "stage_source_id", stage_source_id)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resumeTimeout")
    def resume_timeout(self) -> Optional[pulumi.Input[str]]:
        """
        Defaults to `minutes=10`.
        """
        return pulumi.get(self, "resume_timeout")

    @resume_timeout.setter
    def resume_timeout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resume_timeout", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter(name="stageSourceId")
    def stage_source_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "stage_source_id")

    @stage_source_id.setter
    def stage_source_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stage_source_id", value)


@pulumi.input_type
class _StageSourceState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 resume_timeout: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 stage_source_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering StageSource resources.
        :param pulumi.Input[str] resume_timeout: Defaults to `minutes=10`.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resume_timeout is not None:
            pulumi.set(__self__, "resume_timeout", resume_timeout)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if stage_source_id is not None:
            pulumi.set(__self__, "stage_source_id", stage_source_id)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resumeTimeout")
    def resume_timeout(self) -> Optional[pulumi.Input[str]]:
        """
        Defaults to `minutes=10`.
        """
        return pulumi.get(self, "resume_timeout")

    @resume_timeout.setter
    def resume_timeout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resume_timeout", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter(name="stageSourceId")
    def stage_source_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "stage_source_id")

    @stage_source_id.setter
    def stage_source_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stage_source_id", value)


class StageSource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resume_timeout: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 stage_source_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a StageSource resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resume_timeout: Defaults to `minutes=10`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[StageSourceArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a StageSource resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param StageSourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StageSourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resume_timeout: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 stage_source_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StageSourceArgs.__new__(StageSourceArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["resume_timeout"] = resume_timeout
            __props__.__dict__["source"] = source
            __props__.__dict__["stage_source_id"] = stage_source_id
        super(StageSource, __self__).__init__(
            'authentik:index/stageSource:StageSource',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            resume_timeout: Optional[pulumi.Input[str]] = None,
            source: Optional[pulumi.Input[str]] = None,
            stage_source_id: Optional[pulumi.Input[str]] = None) -> 'StageSource':
        """
        Get an existing StageSource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resume_timeout: Defaults to `minutes=10`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _StageSourceState.__new__(_StageSourceState)

        __props__.__dict__["name"] = name
        __props__.__dict__["resume_timeout"] = resume_timeout
        __props__.__dict__["source"] = source
        __props__.__dict__["stage_source_id"] = stage_source_id
        return StageSource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resumeTimeout")
    def resume_timeout(self) -> pulumi.Output[Optional[str]]:
        """
        Defaults to `minutes=10`.
        """
        return pulumi.get(self, "resume_timeout")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="stageSourceId")
    def stage_source_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "stage_source_id")

