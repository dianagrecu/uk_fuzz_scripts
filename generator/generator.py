#!/usr/bin/env python3

import os
import sys
from jinja2 import Template
from utils import *


def generate(args):
    func_name = args[1]
    gen_dict_entry = gen_prefix + func_name
    # print(gen_dict_entry)
    file_name = func_name + c_extension
    print(args[1:])

    params = []

    for param in args[2:]:
        if param[0:4] == string_prefix:
            param = "\"" + param[4:] + "\""

        params.append(param)

    params = ','.join(params)
    print(params)

    gen_func = gen_dict[gen_dict_entry]

    tm = Template(gen_func)
    msg = tm.render(func_name=func_name, params=params)

    # print generated code to file
    with open(file_name, "w") as text_file:
        print(msg, file=text_file)

    # os.system("cd ~/Documents/licenta/unikraft/apps/helloworld")
    # this still needed to update genericapp.o used in compiling with unikraft so
    os.system(f"make file={file_name}")

    # run as linuxu process
    # os.system("build/helloworld_linuxu-x86_64")

    # run on KVM
    # os.system("./run_kvm")

    os.system(f"{app_unikraft_so}")
    os.system("./app.git_linuxu-x86_64.dbg")


if __name__ == "__main__":
    generate(sys.argv)
