#!/usr/bin/env python3

import os
import sys


def generate(in_filename, out_filename):
    with open(out_filename, "w") as out_file:
        with open(in_filename) as f:
            lines = f.readlines()

            for line in lines:
                func_def = line.strip().split(":")[1]

                func_name = func_def.split("(")[0].rsplit(" ", 1)[1]
                ret_type = func_def.split("(")[0].rsplit(" ", 1)[0]

                if func_name[0] == "*":
                    func_name = func_name[1:]
                    ret_type = "(" + ret_type + " *)"
                # print(f"ret_type: {ret_type}, func_name: {func_name}")
                res = "typedef " + ret_type + " (*type_" + func_name + ")("

                args = func_def.split("(")[1][0:-2].split(",")
                for arg in args:
                    arg_type = arg.rsplit(" ", 1)[0]
                    arg_name = None
                    if len(arg.rsplit(" ", 1)) == 2:
                        arg_name = arg.rsplit(" ", 1)[1]

                    res += arg_type

                    if arg_name and arg_name[0] == "*":
                        res += "*"

                    res += ", "

                res = res[:-2] + ");"

                print(res, file=out_file)


if __name__ == "__main__":
    generate(sys.argv[1], sys.argv[2])
