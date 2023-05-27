# Copyright 2023 BentoML Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
OpenLLM client.

To start interact with the server, you can do the following:

>>> import openllm
>>> client = openllm.client.HTTPClient("http://0.0.0.0:3000")
>>> client.query("What is the meaning of life?")
"""
from __future__ import annotations

import typing as t

import openllm_client as _


def __dir__():
    return dir(_)


def __getattr__(value: t.Any) -> t.Any:
    return getattr(_, value)