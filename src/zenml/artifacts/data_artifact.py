#  Copyright (c) ZenML GmbH 2021. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.

from tfx.types.artifact import Property, PropertyType

from zenml.artifacts.base_artifact import BaseArtifact

SPLIT_NAMES_PROPERTY = Property(type=PropertyType.STRING)  # type: ignore[no-untyped-call] # noqa


class DataArtifact(BaseArtifact):
    """Base class for any ZenML data artifact

    The custom properties include a property to hold split names
    """

    TYPE_NAME = "data_artifact"

    PROPERTIES = {"split_names": SPLIT_NAMES_PROPERTY}
