#!/usr/bin/env python3
import os
import sys
import subprocess
import json


TF_CMD = "C:\\HashiCorp\\Terraform\\terraform.exe"
TIMEOUT = 3 * 60


def run_cmd(*args):
    output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=TIMEOUT)
    if output is None:
        return
    return output.decode("utf-8")


def update_provider(provider, upgrade=False, schema=False):
    print("Provider:", provider)
    cwd = os.getcwd()
    os.chdir(provider)
    if upgrade:
        output = run_cmd(TF_CMD, "init", "-upgrade")
    else:
        output = run_cmd(TF_CMD, "init")
    print("Init:", output)
    output = run_cmd(TF_CMD, "version")
    print("Version:", output)
    with open("version.md", "w") as f:
        f.write(output)
    if schema:
        output = run_cmd(TF_CMD, "providers", "schema", "-json")
        print("Schema:", len(output))
        schema = json.loads(output)
        with open("schema.json", "w") as f:
            json.dump(schema, f, indent=2)
    os.chdir(cwd)


def update_all(upgrade=False, schema=False):
    if upgrade:
        output = run_cmd(TF_CMD, "init", "-upgrade")
    else:
        output = run_cmd(TF_CMD, "init")
    output = run_cmd(TF_CMD, "version")
    print("Version:", output)
    with open("versions.md", "w") as f:
        f.write(output)
    for provider in list(os.listdir(".")):
        if not os.path.isdir(provider):
            continue
        if provider.startswith("."):
            continue
        update_provider(provider, upgrade, schema)


if __name__ == "__main__":
    print("%s [1 [2]]" % os.path.basename(sys.argv[0]))
    if len(sys.argv) > 1:
        update_all(True)
    else:
        update_all()
