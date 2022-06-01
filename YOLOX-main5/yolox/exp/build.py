#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) 2014-2021 Megvii Inc. All rights reserved.

import importlib
import os
import sys


def get_exp_by_file(exp_file):
    try:
        sys.path.append(os.path.dirname(exp_file))

        current_exp = importlib.import_module(os.path.basename(exp_file).split(".")[0])
        print(current_exp)
        exp = current_exp.Exp()
    except Exception:
        raise ImportError("{} doesn't contains class named 'Exp'".format(exp_file))
    return exp


def get_exp_by_name(exp_name):
    import yolox
    # exp = exp_name.replace("-", "_")  # convert string like "yolox-s" to "yolox_s"
    # module_name = ".".join(["yolox", "exp", "default", exp])
    yolox_path = os.path.dirname(os.path.dirname(yolox.__file__))
    # yolox_path='/home/inspur/liudw/YOLOX-main2/yolox/data'
    filedict = {
        "yolox-s": "yolox_s.py",
        # "yolox-m": "yolox_m.py",
        # "yolox-l": "yolox_l.py",
        # "yolox-x": "yolox_x.py",
        # "yolox-tiny": "yolox_tiny.py",
        # "yolox-nano": "nano.py",
        # "yolov3": "yolov3.py",
    }
    filename = filedict[exp_name]
    # exp_object = importlib.import_module(module_name).Exp()
    # return exp_object
    exp_path = os.path.join(yolox_path, "exps", "default", filename)
    return get_exp_by_file(exp_path)

def get_exp(exp_file=None, exp_name=None):
    """
    get Exp object by file or name. If exp_file and exp_name
    are both provided, get Exp by exp_file.

    Args:
        exp_file (str): file path of experiment.
        exp_name (str): name of experiment. "yolo-s",
    """
    assert (
        exp_file is not None or exp_name is not None
    ), "plz provide exp file or exp name."
    if exp_file is not None:
        print(get_exp_by_file(exp_file))
        return get_exp_by_file(exp_file)
    else:
        print(get_exp_by_name(exp_name))
        return get_exp_by_name(exp_name)
