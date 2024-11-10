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

__all__ = ['StagePromptArgs', 'StagePrompt']

@pulumi.input_type
class StagePromptArgs:
    def __init__(__self__, *,
                 fields: pulumi.Input[Sequence[pulumi.Input[str]]],
                 name: Optional[pulumi.Input[str]] = None,
                 stage_prompt_id: Optional[pulumi.Input[str]] = None,
                 validation_policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a StagePrompt resource.
        """
        pulumi.set(__self__, "fields", fields)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if stage_prompt_id is not None:
            pulumi.set(__self__, "stage_prompt_id", stage_prompt_id)
        if validation_policies is not None:
            pulumi.set(__self__, "validation_policies", validation_policies)

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="stagePromptId")
    def stage_prompt_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "stage_prompt_id")

    @stage_prompt_id.setter
    def stage_prompt_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stage_prompt_id", value)

    @property
    @pulumi.getter(name="validationPolicies")
    def validation_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "validation_policies")

    @validation_policies.setter
    def validation_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "validation_policies", value)


@pulumi.input_type
class _StagePromptState:
    def __init__(__self__, *,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 stage_prompt_id: Optional[pulumi.Input[str]] = None,
                 validation_policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering StagePrompt resources.
        """
        if fields is not None:
            pulumi.set(__self__, "fields", fields)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if stage_prompt_id is not None:
            pulumi.set(__self__, "stage_prompt_id", stage_prompt_id)
        if validation_policies is not None:
            pulumi.set(__self__, "validation_policies", validation_policies)

    @property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="stagePromptId")
    def stage_prompt_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "stage_prompt_id")

    @stage_prompt_id.setter
    def stage_prompt_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stage_prompt_id", value)

    @property
    @pulumi.getter(name="validationPolicies")
    def validation_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "validation_policies")

    @validation_policies.setter
    def validation_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "validation_policies", value)


class StagePrompt(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 stage_prompt_id: Optional[pulumi.Input[str]] = None,
                 validation_policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a StagePrompt resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StagePromptArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a StagePrompt resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param StagePromptArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StagePromptArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 stage_prompt_id: Optional[pulumi.Input[str]] = None,
                 validation_policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StagePromptArgs.__new__(StagePromptArgs)

            if fields is None and not opts.urn:
                raise TypeError("Missing required property 'fields'")
            __props__.__dict__["fields"] = fields
            __props__.__dict__["name"] = name
            __props__.__dict__["stage_prompt_id"] = stage_prompt_id
            __props__.__dict__["validation_policies"] = validation_policies
        super(StagePrompt, __self__).__init__(
            'authentik:index/stagePrompt:StagePrompt',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            stage_prompt_id: Optional[pulumi.Input[str]] = None,
            validation_policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'StagePrompt':
        """
        Get an existing StagePrompt resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _StagePromptState.__new__(_StagePromptState)

        __props__.__dict__["fields"] = fields
        __props__.__dict__["name"] = name
        __props__.__dict__["stage_prompt_id"] = stage_prompt_id
        __props__.__dict__["validation_policies"] = validation_policies
        return StagePrompt(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="stagePromptId")
    def stage_prompt_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "stage_prompt_id")

    @property
    @pulumi.getter(name="validationPolicies")
    def validation_policies(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "validation_policies")

