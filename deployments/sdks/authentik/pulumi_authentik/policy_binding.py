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

__all__ = ['PolicyBindingArgs', 'PolicyBinding']

@pulumi.input_type
class PolicyBindingArgs:
    def __init__(__self__, *,
                 order: pulumi.Input[float],
                 target: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 failure_result: Optional[pulumi.Input[bool]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 negate: Optional[pulumi.Input[bool]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 policy_binding_id: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[float]] = None,
                 user: Optional[pulumi.Input[float]] = None):
        """
        The set of arguments for constructing a PolicyBinding resource.
        :param pulumi.Input[str] target: ID of the object this binding should apply to
        :param pulumi.Input[bool] enabled: Defaults to `true`.
        :param pulumi.Input[bool] failure_result: Defaults to `false`.
        :param pulumi.Input[str] group: UUID of the group
        :param pulumi.Input[bool] negate: Defaults to `false`.
        :param pulumi.Input[str] policy: UUID of the policy
        :param pulumi.Input[float] timeout: Defaults to `30`.
        :param pulumi.Input[float] user: PK of the user
        """
        pulumi.set(__self__, "order", order)
        pulumi.set(__self__, "target", target)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if failure_result is not None:
            pulumi.set(__self__, "failure_result", failure_result)
        if group is not None:
            pulumi.set(__self__, "group", group)
        if negate is not None:
            pulumi.set(__self__, "negate", negate)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if policy_binding_id is not None:
            pulumi.set(__self__, "policy_binding_id", policy_binding_id)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter
    def order(self) -> pulumi.Input[float]:
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: pulumi.Input[float]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter
    def target(self) -> pulumi.Input[str]:
        """
        ID of the object this binding should apply to
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: pulumi.Input[str]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="failureResult")
    def failure_result(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `false`.
        """
        return pulumi.get(self, "failure_result")

    @failure_result.setter
    def failure_result(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "failure_result", value)

    @property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[str]]:
        """
        UUID of the group
        """
        return pulumi.get(self, "group")

    @group.setter
    def group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group", value)

    @property
    @pulumi.getter
    def negate(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `false`.
        """
        return pulumi.get(self, "negate")

    @negate.setter
    def negate(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "negate", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        """
        UUID of the policy
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="policyBindingId")
    def policy_binding_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "policy_binding_id")

    @policy_binding_id.setter
    def policy_binding_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_binding_id", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[float]]:
        """
        Defaults to `30`.
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "timeout", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[float]]:
        """
        PK of the user
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "user", value)


@pulumi.input_type
class _PolicyBindingState:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 failure_result: Optional[pulumi.Input[bool]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 negate: Optional[pulumi.Input[bool]] = None,
                 order: Optional[pulumi.Input[float]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 policy_binding_id: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[float]] = None,
                 user: Optional[pulumi.Input[float]] = None):
        """
        Input properties used for looking up and filtering PolicyBinding resources.
        :param pulumi.Input[bool] enabled: Defaults to `true`.
        :param pulumi.Input[bool] failure_result: Defaults to `false`.
        :param pulumi.Input[str] group: UUID of the group
        :param pulumi.Input[bool] negate: Defaults to `false`.
        :param pulumi.Input[str] policy: UUID of the policy
        :param pulumi.Input[str] target: ID of the object this binding should apply to
        :param pulumi.Input[float] timeout: Defaults to `30`.
        :param pulumi.Input[float] user: PK of the user
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if failure_result is not None:
            pulumi.set(__self__, "failure_result", failure_result)
        if group is not None:
            pulumi.set(__self__, "group", group)
        if negate is not None:
            pulumi.set(__self__, "negate", negate)
        if order is not None:
            pulumi.set(__self__, "order", order)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if policy_binding_id is not None:
            pulumi.set(__self__, "policy_binding_id", policy_binding_id)
        if target is not None:
            pulumi.set(__self__, "target", target)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="failureResult")
    def failure_result(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `false`.
        """
        return pulumi.get(self, "failure_result")

    @failure_result.setter
    def failure_result(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "failure_result", value)

    @property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[str]]:
        """
        UUID of the group
        """
        return pulumi.get(self, "group")

    @group.setter
    def group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group", value)

    @property
    @pulumi.getter
    def negate(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `false`.
        """
        return pulumi.get(self, "negate")

    @negate.setter
    def negate(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "negate", value)

    @property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        """
        UUID of the policy
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="policyBindingId")
    def policy_binding_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "policy_binding_id")

    @policy_binding_id.setter
    def policy_binding_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_binding_id", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the object this binding should apply to
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[float]]:
        """
        Defaults to `30`.
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "timeout", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[float]]:
        """
        PK of the user
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "user", value)


class PolicyBinding(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 failure_result: Optional[pulumi.Input[bool]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 negate: Optional[pulumi.Input[bool]] = None,
                 order: Optional[pulumi.Input[float]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 policy_binding_id: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[float]] = None,
                 user: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        """
        Create a PolicyBinding resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: Defaults to `true`.
        :param pulumi.Input[bool] failure_result: Defaults to `false`.
        :param pulumi.Input[str] group: UUID of the group
        :param pulumi.Input[bool] negate: Defaults to `false`.
        :param pulumi.Input[str] policy: UUID of the policy
        :param pulumi.Input[str] target: ID of the object this binding should apply to
        :param pulumi.Input[float] timeout: Defaults to `30`.
        :param pulumi.Input[float] user: PK of the user
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicyBindingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a PolicyBinding resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param PolicyBindingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyBindingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 failure_result: Optional[pulumi.Input[bool]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 negate: Optional[pulumi.Input[bool]] = None,
                 order: Optional[pulumi.Input[float]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 policy_binding_id: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[float]] = None,
                 user: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PolicyBindingArgs.__new__(PolicyBindingArgs)

            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["failure_result"] = failure_result
            __props__.__dict__["group"] = group
            __props__.__dict__["negate"] = negate
            if order is None and not opts.urn:
                raise TypeError("Missing required property 'order'")
            __props__.__dict__["order"] = order
            __props__.__dict__["policy"] = policy
            __props__.__dict__["policy_binding_id"] = policy_binding_id
            if target is None and not opts.urn:
                raise TypeError("Missing required property 'target'")
            __props__.__dict__["target"] = target
            __props__.__dict__["timeout"] = timeout
            __props__.__dict__["user"] = user
        super(PolicyBinding, __self__).__init__(
            'authentik:index/policyBinding:PolicyBinding',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            failure_result: Optional[pulumi.Input[bool]] = None,
            group: Optional[pulumi.Input[str]] = None,
            negate: Optional[pulumi.Input[bool]] = None,
            order: Optional[pulumi.Input[float]] = None,
            policy: Optional[pulumi.Input[str]] = None,
            policy_binding_id: Optional[pulumi.Input[str]] = None,
            target: Optional[pulumi.Input[str]] = None,
            timeout: Optional[pulumi.Input[float]] = None,
            user: Optional[pulumi.Input[float]] = None) -> 'PolicyBinding':
        """
        Get an existing PolicyBinding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: Defaults to `true`.
        :param pulumi.Input[bool] failure_result: Defaults to `false`.
        :param pulumi.Input[str] group: UUID of the group
        :param pulumi.Input[bool] negate: Defaults to `false`.
        :param pulumi.Input[str] policy: UUID of the policy
        :param pulumi.Input[str] target: ID of the object this binding should apply to
        :param pulumi.Input[float] timeout: Defaults to `30`.
        :param pulumi.Input[float] user: PK of the user
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PolicyBindingState.__new__(_PolicyBindingState)

        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["failure_result"] = failure_result
        __props__.__dict__["group"] = group
        __props__.__dict__["negate"] = negate
        __props__.__dict__["order"] = order
        __props__.__dict__["policy"] = policy
        __props__.__dict__["policy_binding_id"] = policy_binding_id
        __props__.__dict__["target"] = target
        __props__.__dict__["timeout"] = timeout
        __props__.__dict__["user"] = user
        return PolicyBinding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="failureResult")
    def failure_result(self) -> pulumi.Output[Optional[bool]]:
        """
        Defaults to `false`.
        """
        return pulumi.get(self, "failure_result")

    @property
    @pulumi.getter
    def group(self) -> pulumi.Output[Optional[str]]:
        """
        UUID of the group
        """
        return pulumi.get(self, "group")

    @property
    @pulumi.getter
    def negate(self) -> pulumi.Output[Optional[bool]]:
        """
        Defaults to `false`.
        """
        return pulumi.get(self, "negate")

    @property
    @pulumi.getter
    def order(self) -> pulumi.Output[float]:
        return pulumi.get(self, "order")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[Optional[str]]:
        """
        UUID of the policy
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="policyBindingId")
    def policy_binding_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "policy_binding_id")

    @property
    @pulumi.getter
    def target(self) -> pulumi.Output[str]:
        """
        ID of the object this binding should apply to
        """
        return pulumi.get(self, "target")

    @property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional[float]]:
        """
        Defaults to `30`.
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter
    def user(self) -> pulumi.Output[Optional[float]]:
        """
        PK of the user
        """
        return pulumi.get(self, "user")

