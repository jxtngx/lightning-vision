# Copyright Justin R. Goheen.
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

import os
from pathlib import Path

import torch

from visionlab import LabDataModule


def test_module_not_abstract():
    _ = LabDataModule()


def test_prepare_data():
    data_module = LabDataModule()
    data_module.prepare_data()
    networkpath = Path(__file__).parent
    projectpath = networkpath.parents[0]
    datapath = os.path.join(projectpath, "data", "cache")
    assert "LabDataset" in os.listdir(datapath)


def test_setup():
    data_module = LabDataModule()
    data_module.prepare_data()
    data_module.setup()
    data_keys = ["train_data", "test_data", "val_data"]
    assert all(key in dir(data_module) for key in data_keys)


def test_trainloader():
    data_module = LabDataModule()
    data_module.prepare_data()
    data_module.setup()
    loader = data_module.train_dataloader()
    sample = loader.dataset[0][0]
    assert isinstance(sample, torch.Tensor)


def test_testloader():
    data_module = LabDataModule()
    data_module.prepare_data()
    data_module.setup()
    loader = data_module.test_dataloader()
    sample = loader.dataset[0][0]
    assert isinstance(sample, torch.Tensor)


def test_valloader():
    data_module = LabDataModule()
    data_module.prepare_data()
    data_module.setup()
    loader = data_module.val_dataloader()
    sample = loader.dataset[0][0]
    assert isinstance(sample, torch.Tensor)
