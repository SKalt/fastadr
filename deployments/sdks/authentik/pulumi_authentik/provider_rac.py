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

__all__ = ['ProviderRacArgs', 'ProviderRac']

@pulumi.input_type
class ProviderRacArgs:
    def __init__(__self__, *,
                 authorization_flow: pulumi.Input[str],
                 authentication_flow: Optional[pulumi.Input[str]] = None,
                 connection_expiry: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 property_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 provider_rac_id: Optional[pulumi.Input[str]] = None,
                 settings: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ProviderRac resource.
        :param pulumi.Input[str] connection_expiry: Defaults to `seconds=0`.
        :param pulumi.Input[str] settings: JSON format expected. Use jsonencode() to pass objects. Defaults to `{}`.
        """
        pulumi.set(__self__, "authorization_flow", authorization_flow)
        if authentication_flow is not None:
            pulumi.set(__self__, "authentication_flow", authentication_flow)
        if connection_expiry is not None:
            pulumi.set(__self__, "connection_expiry", connection_expiry)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if property_mappings is not None:
            pulumi.set(__self__, "property_mappings", property_mappings)
        if provider_rac_id is not None:
            pulumi.set(__self__, "provider_rac_id", provider_rac_id)
        if settings is not None:
            pulumi.set(__self__, "settings", settings)

    @property
    @pulumi.getter(name="authorizationFlow")
    def authorization_flow(self) -> pulumi.Input[str]:
        return pulumi.get(self, "authorization_flow")

    @authorization_flow.setter
    def authorization_flow(self, value: pulumi.Input[str]):
        pulumi.set(self, "authorization_flow", value)

    @property
    @pulumi.getter(name="authenticationFlow")
    def authentication_flow(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "authentication_flow")

    @authentication_flow.setter
    def authentication_flow(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication_flow", value)

    @property
    @pulumi.getter(name="connectionExpiry")
    def connection_expiry(self) -> Optional[pulumi.Input[str]]:
        """
        Defaults to `seconds=0`.
        """
        return pulumi.get(self, "connection_expiry")

    @connection_expiry.setter
    def connection_expiry(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_expiry", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="propertyMappings")
    def property_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "property_mappings")

    @property_mappings.setter
    def property_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "property_mappings", value)

    @property
    @pulumi.getter(name="providerRacId")
    def provider_rac_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "provider_rac_id")

    @provider_rac_id.setter
    def provider_rac_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_rac_id", value)

    @property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[str]]:
        """
        JSON format expected. Use jsonencode() to pass objects. Defaults to `{}`.
        """
        return pulumi.get(self, "settings")

    @settings.setter
    def settings(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "settings", value)


@pulumi.input_type
class _ProviderRacState:
    def __init__(__self__, *,
                 authentication_flow: Optional[pulumi.Input[str]] = None,
                 authorization_flow: Optional[pulumi.Input[str]] = None,
                 connection_expiry: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 property_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 provider_rac_id: Optional[pulumi.Input[str]] = None,
                 settings: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ProviderRac resources.
        :param pulumi.Input[str] connection_expiry: Defaults to `seconds=0`.
        :param pulumi.Input[str] settings: JSON format expected. Use jsonencode() to pass objects. Defaults to `{}`.
        """
        if authentication_flow is not None:
            pulumi.set(__self__, "authentication_flow", authentication_flow)
        if authorization_flow is not None:
            pulumi.set(__self__, "authorization_flow", authorization_flow)
        if connection_expiry is not None:
            pulumi.set(__self__, "connection_expiry", connection_expiry)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if property_mappings is not None:
            pulumi.set(__self__, "property_mappings", property_mappings)
        if provider_rac_id is not None:
            pulumi.set(__self__, "provider_rac_id", provider_rac_id)
        if settings is not None:
            pulumi.set(__self__, "settings", settings)

    @property
    @pulumi.getter(name="authenticationFlow")
    def authentication_flow(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "authentication_flow")

    @authentication_flow.setter
    def authentication_flow(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication_flow", value)

    @property
    @pulumi.getter(name="authorizationFlow")
    def authorization_flow(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "authorization_flow")

    @authorization_flow.setter
    def authorization_flow(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization_flow", value)

    @property
    @pulumi.getter(name="connectionExpiry")
    def connection_expiry(self) -> Optional[pulumi.Input[str]]:
        """
        Defaults to `seconds=0`.
        """
        return pulumi.get(self, "connection_expiry")

    @connection_expiry.setter
    def connection_expiry(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_expiry", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="propertyMappings")
    def property_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "property_mappings")

    @property_mappings.setter
    def property_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "property_mappings", value)

    @property
    @pulumi.getter(name="providerRacId")
    def provider_rac_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "provider_rac_id")

    @provider_rac_id.setter
    def provider_rac_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_rac_id", value)

    @property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[str]]:
        """
        JSON format expected. Use jsonencode() to pass objects. Defaults to `{}`.
        """
        return pulumi.get(self, "settings")

    @settings.setter
    def settings(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "settings", value)


class ProviderRac(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_flow: Optional[pulumi.Input[str]] = None,
                 authorization_flow: Optional[pulumi.Input[str]] = None,
                 connection_expiry: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 property_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 provider_rac_id: Optional[pulumi.Input[str]] = None,
                 settings: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ProviderRac resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connection_expiry: Defaults to `seconds=0`.
        :param pulumi.Input[str] settings: JSON format expected. Use jsonencode() to pass objects. Defaults to `{}`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderRacArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ProviderRac resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ProviderRacArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderRacArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_flow: Optional[pulumi.Input[str]] = None,
                 authorization_flow: Optional[pulumi.Input[str]] = None,
                 connection_expiry: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 property_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 provider_rac_id: Optional[pulumi.Input[str]] = None,
                 settings: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderRacArgs.__new__(ProviderRacArgs)

            __props__.__dict__["authentication_flow"] = authentication_flow
            if authorization_flow is None and not opts.urn:
                raise TypeError("Missing required property 'authorization_flow'")
            __props__.__dict__["authorization_flow"] = authorization_flow
            __props__.__dict__["connection_expiry"] = connection_expiry
            __props__.__dict__["name"] = name
            __props__.__dict__["property_mappings"] = property_mappings
            __props__.__dict__["provider_rac_id"] = provider_rac_id
            __props__.__dict__["settings"] = settings
        super(ProviderRac, __self__).__init__(
            'authentik:index/providerRac:ProviderRac',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authentication_flow: Optional[pulumi.Input[str]] = None,
            authorization_flow: Optional[pulumi.Input[str]] = None,
            connection_expiry: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            property_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            provider_rac_id: Optional[pulumi.Input[str]] = None,
            settings: Optional[pulumi.Input[str]] = None) -> 'ProviderRac':
        """
        Get an existing ProviderRac resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connection_expiry: Defaults to `seconds=0`.
        :param pulumi.Input[str] settings: JSON format expected. Use jsonencode() to pass objects. Defaults to `{}`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProviderRacState.__new__(_ProviderRacState)

        __props__.__dict__["authentication_flow"] = authentication_flow
        __props__.__dict__["authorization_flow"] = authorization_flow
        __props__.__dict__["connection_expiry"] = connection_expiry
        __props__.__dict__["name"] = name
        __props__.__dict__["property_mappings"] = property_mappings
        __props__.__dict__["provider_rac_id"] = provider_rac_id
        __props__.__dict__["settings"] = settings
        return ProviderRac(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authenticationFlow")
    def authentication_flow(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "authentication_flow")

    @property
    @pulumi.getter(name="authorizationFlow")
    def authorization_flow(self) -> pulumi.Output[str]:
        return pulumi.get(self, "authorization_flow")

    @property
    @pulumi.getter(name="connectionExpiry")
    def connection_expiry(self) -> pulumi.Output[Optional[str]]:
        """
        Defaults to `seconds=0`.
        """
        return pulumi.get(self, "connection_expiry")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="propertyMappings")
    def property_mappings(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "property_mappings")

    @property
    @pulumi.getter(name="providerRacId")
    def provider_rac_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "provider_rac_id")

    @property
    @pulumi.getter
    def settings(self) -> pulumi.Output[Optional[str]]:
        """
        JSON format expected. Use jsonencode() to pass objects. Defaults to `{}`.
        """
        return pulumi.get(self, "settings")

