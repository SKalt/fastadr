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

__all__ = ['StageUserWriteArgs', 'StageUserWrite']

@pulumi.input_type
class StageUserWriteArgs:
    def __init__(__self__, *,
                 create_users_as_inactive: Optional[pulumi.Input[bool]] = None,
                 create_users_group: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 stage_user_write_id: Optional[pulumi.Input[str]] = None,
                 user_creation_mode: Optional[pulumi.Input[str]] = None,
                 user_path_template: Optional[pulumi.Input[str]] = None,
                 user_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StageUserWrite resource.
        :param pulumi.Input[bool] create_users_as_inactive: Defaults to `true`.
        :param pulumi.Input[str] user_creation_mode: Allowed values: - `never_create` - `create_when_required` - `always_create` Defaults to `create_when_required`.
        :param pulumi.Input[str] user_path_template: Defaults to ``.
        :param pulumi.Input[str] user_type: Allowed values: - `internal` - `external` - `service_account` Defaults to `external`.
        """
        if create_users_as_inactive is not None:
            pulumi.set(__self__, "create_users_as_inactive", create_users_as_inactive)
        if create_users_group is not None:
            pulumi.set(__self__, "create_users_group", create_users_group)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if stage_user_write_id is not None:
            pulumi.set(__self__, "stage_user_write_id", stage_user_write_id)
        if user_creation_mode is not None:
            pulumi.set(__self__, "user_creation_mode", user_creation_mode)
        if user_path_template is not None:
            pulumi.set(__self__, "user_path_template", user_path_template)
        if user_type is not None:
            pulumi.set(__self__, "user_type", user_type)

    @property
    @pulumi.getter(name="createUsersAsInactive")
    def create_users_as_inactive(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `true`.
        """
        return pulumi.get(self, "create_users_as_inactive")

    @create_users_as_inactive.setter
    def create_users_as_inactive(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "create_users_as_inactive", value)

    @property
    @pulumi.getter(name="createUsersGroup")
    def create_users_group(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "create_users_group")

    @create_users_group.setter
    def create_users_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_users_group", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="stageUserWriteId")
    def stage_user_write_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "stage_user_write_id")

    @stage_user_write_id.setter
    def stage_user_write_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stage_user_write_id", value)

    @property
    @pulumi.getter(name="userCreationMode")
    def user_creation_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Allowed values: - `never_create` - `create_when_required` - `always_create` Defaults to `create_when_required`.
        """
        return pulumi.get(self, "user_creation_mode")

    @user_creation_mode.setter
    def user_creation_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_creation_mode", value)

    @property
    @pulumi.getter(name="userPathTemplate")
    def user_path_template(self) -> Optional[pulumi.Input[str]]:
        """
        Defaults to ``.
        """
        return pulumi.get(self, "user_path_template")

    @user_path_template.setter
    def user_path_template(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_path_template", value)

    @property
    @pulumi.getter(name="userType")
    def user_type(self) -> Optional[pulumi.Input[str]]:
        """
        Allowed values: - `internal` - `external` - `service_account` Defaults to `external`.
        """
        return pulumi.get(self, "user_type")

    @user_type.setter
    def user_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_type", value)


@pulumi.input_type
class _StageUserWriteState:
    def __init__(__self__, *,
                 create_users_as_inactive: Optional[pulumi.Input[bool]] = None,
                 create_users_group: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 stage_user_write_id: Optional[pulumi.Input[str]] = None,
                 user_creation_mode: Optional[pulumi.Input[str]] = None,
                 user_path_template: Optional[pulumi.Input[str]] = None,
                 user_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering StageUserWrite resources.
        :param pulumi.Input[bool] create_users_as_inactive: Defaults to `true`.
        :param pulumi.Input[str] user_creation_mode: Allowed values: - `never_create` - `create_when_required` - `always_create` Defaults to `create_when_required`.
        :param pulumi.Input[str] user_path_template: Defaults to ``.
        :param pulumi.Input[str] user_type: Allowed values: - `internal` - `external` - `service_account` Defaults to `external`.
        """
        if create_users_as_inactive is not None:
            pulumi.set(__self__, "create_users_as_inactive", create_users_as_inactive)
        if create_users_group is not None:
            pulumi.set(__self__, "create_users_group", create_users_group)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if stage_user_write_id is not None:
            pulumi.set(__self__, "stage_user_write_id", stage_user_write_id)
        if user_creation_mode is not None:
            pulumi.set(__self__, "user_creation_mode", user_creation_mode)
        if user_path_template is not None:
            pulumi.set(__self__, "user_path_template", user_path_template)
        if user_type is not None:
            pulumi.set(__self__, "user_type", user_type)

    @property
    @pulumi.getter(name="createUsersAsInactive")
    def create_users_as_inactive(self) -> Optional[pulumi.Input[bool]]:
        """
        Defaults to `true`.
        """
        return pulumi.get(self, "create_users_as_inactive")

    @create_users_as_inactive.setter
    def create_users_as_inactive(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "create_users_as_inactive", value)

    @property
    @pulumi.getter(name="createUsersGroup")
    def create_users_group(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "create_users_group")

    @create_users_group.setter
    def create_users_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_users_group", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="stageUserWriteId")
    def stage_user_write_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "stage_user_write_id")

    @stage_user_write_id.setter
    def stage_user_write_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stage_user_write_id", value)

    @property
    @pulumi.getter(name="userCreationMode")
    def user_creation_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Allowed values: - `never_create` - `create_when_required` - `always_create` Defaults to `create_when_required`.
        """
        return pulumi.get(self, "user_creation_mode")

    @user_creation_mode.setter
    def user_creation_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_creation_mode", value)

    @property
    @pulumi.getter(name="userPathTemplate")
    def user_path_template(self) -> Optional[pulumi.Input[str]]:
        """
        Defaults to ``.
        """
        return pulumi.get(self, "user_path_template")

    @user_path_template.setter
    def user_path_template(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_path_template", value)

    @property
    @pulumi.getter(name="userType")
    def user_type(self) -> Optional[pulumi.Input[str]]:
        """
        Allowed values: - `internal` - `external` - `service_account` Defaults to `external`.
        """
        return pulumi.get(self, "user_type")

    @user_type.setter
    def user_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_type", value)


class StageUserWrite(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_users_as_inactive: Optional[pulumi.Input[bool]] = None,
                 create_users_group: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 stage_user_write_id: Optional[pulumi.Input[str]] = None,
                 user_creation_mode: Optional[pulumi.Input[str]] = None,
                 user_path_template: Optional[pulumi.Input[str]] = None,
                 user_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a StageUserWrite resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] create_users_as_inactive: Defaults to `true`.
        :param pulumi.Input[str] user_creation_mode: Allowed values: - `never_create` - `create_when_required` - `always_create` Defaults to `create_when_required`.
        :param pulumi.Input[str] user_path_template: Defaults to ``.
        :param pulumi.Input[str] user_type: Allowed values: - `internal` - `external` - `service_account` Defaults to `external`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[StageUserWriteArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a StageUserWrite resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param StageUserWriteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StageUserWriteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 create_users_as_inactive: Optional[pulumi.Input[bool]] = None,
                 create_users_group: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 stage_user_write_id: Optional[pulumi.Input[str]] = None,
                 user_creation_mode: Optional[pulumi.Input[str]] = None,
                 user_path_template: Optional[pulumi.Input[str]] = None,
                 user_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StageUserWriteArgs.__new__(StageUserWriteArgs)

            __props__.__dict__["create_users_as_inactive"] = create_users_as_inactive
            __props__.__dict__["create_users_group"] = create_users_group
            __props__.__dict__["name"] = name
            __props__.__dict__["stage_user_write_id"] = stage_user_write_id
            __props__.__dict__["user_creation_mode"] = user_creation_mode
            __props__.__dict__["user_path_template"] = user_path_template
            __props__.__dict__["user_type"] = user_type
        super(StageUserWrite, __self__).__init__(
            'authentik:index/stageUserWrite:StageUserWrite',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_users_as_inactive: Optional[pulumi.Input[bool]] = None,
            create_users_group: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            stage_user_write_id: Optional[pulumi.Input[str]] = None,
            user_creation_mode: Optional[pulumi.Input[str]] = None,
            user_path_template: Optional[pulumi.Input[str]] = None,
            user_type: Optional[pulumi.Input[str]] = None) -> 'StageUserWrite':
        """
        Get an existing StageUserWrite resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] create_users_as_inactive: Defaults to `true`.
        :param pulumi.Input[str] user_creation_mode: Allowed values: - `never_create` - `create_when_required` - `always_create` Defaults to `create_when_required`.
        :param pulumi.Input[str] user_path_template: Defaults to ``.
        :param pulumi.Input[str] user_type: Allowed values: - `internal` - `external` - `service_account` Defaults to `external`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _StageUserWriteState.__new__(_StageUserWriteState)

        __props__.__dict__["create_users_as_inactive"] = create_users_as_inactive
        __props__.__dict__["create_users_group"] = create_users_group
        __props__.__dict__["name"] = name
        __props__.__dict__["stage_user_write_id"] = stage_user_write_id
        __props__.__dict__["user_creation_mode"] = user_creation_mode
        __props__.__dict__["user_path_template"] = user_path_template
        __props__.__dict__["user_type"] = user_type
        return StageUserWrite(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createUsersAsInactive")
    def create_users_as_inactive(self) -> pulumi.Output[Optional[bool]]:
        """
        Defaults to `true`.
        """
        return pulumi.get(self, "create_users_as_inactive")

    @property
    @pulumi.getter(name="createUsersGroup")
    def create_users_group(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "create_users_group")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="stageUserWriteId")
    def stage_user_write_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "stage_user_write_id")

    @property
    @pulumi.getter(name="userCreationMode")
    def user_creation_mode(self) -> pulumi.Output[Optional[str]]:
        """
        Allowed values: - `never_create` - `create_when_required` - `always_create` Defaults to `create_when_required`.
        """
        return pulumi.get(self, "user_creation_mode")

    @property
    @pulumi.getter(name="userPathTemplate")
    def user_path_template(self) -> pulumi.Output[Optional[str]]:
        """
        Defaults to ``.
        """
        return pulumi.get(self, "user_path_template")

    @property
    @pulumi.getter(name="userType")
    def user_type(self) -> pulumi.Output[Optional[str]]:
        """
        Allowed values: - `internal` - `external` - `service_account` Defaults to `external`.
        """
        return pulumi.get(self, "user_type")
