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

__all__ = ['PropertyMappingProviderMicrosoftEntraArgs', 'PropertyMappingProviderMicrosoftEntra']

@pulumi.input_type
class PropertyMappingProviderMicrosoftEntraArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 property_mapping_provider_microsoft_entra_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PropertyMappingProviderMicrosoftEntra resource.
        """
        pulumi.set(__self__, "expression", expression)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if property_mapping_provider_microsoft_entra_id is not None:
            pulumi.set(__self__, "property_mapping_provider_microsoft_entra_id", property_mapping_provider_microsoft_entra_id)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="propertyMappingProviderMicrosoftEntraId")
    def property_mapping_provider_microsoft_entra_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "property_mapping_provider_microsoft_entra_id")

    @property_mapping_provider_microsoft_entra_id.setter
    def property_mapping_provider_microsoft_entra_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "property_mapping_provider_microsoft_entra_id", value)


@pulumi.input_type
class _PropertyMappingProviderMicrosoftEntraState:
    def __init__(__self__, *,
                 expression: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 property_mapping_provider_microsoft_entra_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PropertyMappingProviderMicrosoftEntra resources.
        """
        if expression is not None:
            pulumi.set(__self__, "expression", expression)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if property_mapping_provider_microsoft_entra_id is not None:
            pulumi.set(__self__, "property_mapping_provider_microsoft_entra_id", property_mapping_provider_microsoft_entra_id)

    @property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="propertyMappingProviderMicrosoftEntraId")
    def property_mapping_provider_microsoft_entra_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "property_mapping_provider_microsoft_entra_id")

    @property_mapping_provider_microsoft_entra_id.setter
    def property_mapping_provider_microsoft_entra_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "property_mapping_provider_microsoft_entra_id", value)


class PropertyMappingProviderMicrosoftEntra(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 expression: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 property_mapping_provider_microsoft_entra_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a PropertyMappingProviderMicrosoftEntra resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PropertyMappingProviderMicrosoftEntraArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a PropertyMappingProviderMicrosoftEntra resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param PropertyMappingProviderMicrosoftEntraArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PropertyMappingProviderMicrosoftEntraArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 expression: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 property_mapping_provider_microsoft_entra_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PropertyMappingProviderMicrosoftEntraArgs.__new__(PropertyMappingProviderMicrosoftEntraArgs)

            if expression is None and not opts.urn:
                raise TypeError("Missing required property 'expression'")
            __props__.__dict__["expression"] = expression
            __props__.__dict__["name"] = name
            __props__.__dict__["property_mapping_provider_microsoft_entra_id"] = property_mapping_provider_microsoft_entra_id
        super(PropertyMappingProviderMicrosoftEntra, __self__).__init__(
            'authentik:index/propertyMappingProviderMicrosoftEntra:PropertyMappingProviderMicrosoftEntra',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            expression: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            property_mapping_provider_microsoft_entra_id: Optional[pulumi.Input[str]] = None) -> 'PropertyMappingProviderMicrosoftEntra':
        """
        Get an existing PropertyMappingProviderMicrosoftEntra resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PropertyMappingProviderMicrosoftEntraState.__new__(_PropertyMappingProviderMicrosoftEntraState)

        __props__.__dict__["expression"] = expression
        __props__.__dict__["name"] = name
        __props__.__dict__["property_mapping_provider_microsoft_entra_id"] = property_mapping_provider_microsoft_entra_id
        return PropertyMappingProviderMicrosoftEntra(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Output[str]:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="propertyMappingProviderMicrosoftEntraId")
    def property_mapping_provider_microsoft_entra_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "property_mapping_provider_microsoft_entra_id")

