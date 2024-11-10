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

__all__ = ['ServiceConnectionKubernetesArgs', 'ServiceConnectionKubernetes']

@pulumi.input_type
class ServiceConnectionKubernetesArgs:
    def __init__(__self__, *,
                 kubeconfig: Optional[pulumi.Input[str]] = None,
                 local: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_connection_kubernetes_id: Optional[pulumi.Input[str]] = None,
                 verify_ssl: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a ServiceConnectionKubernetes resource.
        :param pulumi.Input[str] kubeconfig: JSON format expected. Use jsonencode() to pass objects. Defaults to `{}`.
        :param pulumi.Input[bool] local: Defaults to `false`.
        :param pulumi.Input[bool] verify_ssl: Defaults to `true`.
        """
        if kubeconfig is not None:
            pulumi.set(__self__, "kubeconfig", kubeconfig)
        if local is not None:
            pulumi.set(__self__, "local", local)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if service_connection_kubernetes_id is not None:
            pulumi.set(__self__, "service_connection_kubernetes_id", service_connection_kubernetes_id)
        if verify_ssl is not None:
            pulumi.set(__self__, "verify_ssl", verify_ssl)

    @property
    @pulumi.getter
    def kubeconfig(self) -> Optional[pulumi.Input[str]]:
        """
        JSON format expected. Use jsonencode() to pass objects. Defaults to `{}`.
        """
        return pulumi.get(self, "kubeconfig")

    @kubeconfig.setter
    def kubeconfig(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubeconfig", value)

    @property
    @pulumi.getter
    def local(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `false`.
        """
        return pulumi.get(self, "local")

    @local.setter
    def local(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "local", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="serviceConnectionKubernetesId")
    def service_connection_kubernetes_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "service_connection_kubernetes_id")

    @service_connection_kubernetes_id.setter
    def service_connection_kubernetes_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_connection_kubernetes_id", value)

    @property
    @pulumi.getter(name="verifySsl")
    def verify_ssl(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `true`.
        """
        return pulumi.get(self, "verify_ssl")

    @verify_ssl.setter
    def verify_ssl(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "verify_ssl", value)


@pulumi.input_type
class _ServiceConnectionKubernetesState:
    def __init__(__self__, *,
                 kubeconfig: Optional[pulumi.Input[str]] = None,
                 local: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_connection_kubernetes_id: Optional[pulumi.Input[str]] = None,
                 verify_ssl: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering ServiceConnectionKubernetes resources.
        :param pulumi.Input[str] kubeconfig: JSON format expected. Use jsonencode() to pass objects. Defaults to `{}`.
        :param pulumi.Input[bool] local: Defaults to `false`.
        :param pulumi.Input[bool] verify_ssl: Defaults to `true`.
        """
        if kubeconfig is not None:
            pulumi.set(__self__, "kubeconfig", kubeconfig)
        if local is not None:
            pulumi.set(__self__, "local", local)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if service_connection_kubernetes_id is not None:
            pulumi.set(__self__, "service_connection_kubernetes_id", service_connection_kubernetes_id)
        if verify_ssl is not None:
            pulumi.set(__self__, "verify_ssl", verify_ssl)

    @property
    @pulumi.getter
    def kubeconfig(self) -> Optional[pulumi.Input[str]]:
        """
        JSON format expected. Use jsonencode() to pass objects. Defaults to `{}`.
        """
        return pulumi.get(self, "kubeconfig")

    @kubeconfig.setter
    def kubeconfig(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubeconfig", value)

    @property
    @pulumi.getter
    def local(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `false`.
        """
        return pulumi.get(self, "local")

    @local.setter
    def local(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "local", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="serviceConnectionKubernetesId")
    def service_connection_kubernetes_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "service_connection_kubernetes_id")

    @service_connection_kubernetes_id.setter
    def service_connection_kubernetes_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_connection_kubernetes_id", value)

    @property
    @pulumi.getter(name="verifySsl")
    def verify_ssl(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `true`.
        """
        return pulumi.get(self, "verify_ssl")

    @verify_ssl.setter
    def verify_ssl(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "verify_ssl", value)


class ServiceConnectionKubernetes(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kubeconfig: Optional[pulumi.Input[str]] = None,
                 local: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_connection_kubernetes_id: Optional[pulumi.Input[str]] = None,
                 verify_ssl: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a ServiceConnectionKubernetes resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] kubeconfig: JSON format expected. Use jsonencode() to pass objects. Defaults to `{}`.
        :param pulumi.Input[bool] local: Defaults to `false`.
        :param pulumi.Input[bool] verify_ssl: Defaults to `true`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ServiceConnectionKubernetesArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ServiceConnectionKubernetes resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ServiceConnectionKubernetesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceConnectionKubernetesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kubeconfig: Optional[pulumi.Input[str]] = None,
                 local: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_connection_kubernetes_id: Optional[pulumi.Input[str]] = None,
                 verify_ssl: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceConnectionKubernetesArgs.__new__(ServiceConnectionKubernetesArgs)

            __props__.__dict__["kubeconfig"] = None if kubeconfig is None else pulumi.Output.secret(kubeconfig)
            __props__.__dict__["local"] = local
            __props__.__dict__["name"] = name
            __props__.__dict__["service_connection_kubernetes_id"] = service_connection_kubernetes_id
            __props__.__dict__["verify_ssl"] = verify_ssl
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["kubeconfig"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(ServiceConnectionKubernetes, __self__).__init__(
            'authentik:index/serviceConnectionKubernetes:ServiceConnectionKubernetes',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            kubeconfig: Optional[pulumi.Input[str]] = None,
            local: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            service_connection_kubernetes_id: Optional[pulumi.Input[str]] = None,
            verify_ssl: Optional[pulumi.Input[bool]] = None) -> 'ServiceConnectionKubernetes':
        """
        Get an existing ServiceConnectionKubernetes resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] kubeconfig: JSON format expected. Use jsonencode() to pass objects. Defaults to `{}`.
        :param pulumi.Input[bool] local: Defaults to `false`.
        :param pulumi.Input[bool] verify_ssl: Defaults to `true`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServiceConnectionKubernetesState.__new__(_ServiceConnectionKubernetesState)

        __props__.__dict__["kubeconfig"] = kubeconfig
        __props__.__dict__["local"] = local
        __props__.__dict__["name"] = name
        __props__.__dict__["service_connection_kubernetes_id"] = service_connection_kubernetes_id
        __props__.__dict__["verify_ssl"] = verify_ssl
        return ServiceConnectionKubernetes(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def kubeconfig(self) -> pulumi.Output[Optional[str]]:
        """
        JSON format expected. Use jsonencode() to pass objects. Defaults to `{}`.
        """
        return pulumi.get(self, "kubeconfig")

    @property
    @pulumi.getter
    def local(self) -> pulumi.Output[Optional[bool]]:
        """
        Defaults to `false`.
        """
        return pulumi.get(self, "local")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serviceConnectionKubernetesId")
    def service_connection_kubernetes_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "service_connection_kubernetes_id")

    @property
    @pulumi.getter(name="verifySsl")
    def verify_ssl(self) -> pulumi.Output[Optional[bool]]:
        """
        Defaults to `true`.
        """
        return pulumi.get(self, "verify_ssl")

