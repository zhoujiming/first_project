# -*- coding: utf-8 -*-
# Date: 2020/9/24

import pip
from pip._internal.utils.misc import get_installed_distributions
from subprocess import call
import time

for dist in get_installed_distributions():
    print(dist.project_name)

for dist in get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)
