import subprocess
import json, os

def run_command(cmd):
    process = subprocess.run(cmd, capture_output=True, text=True, check=False, encoding='utf-8', shell=True)

    # change to JSON
    #terminal_markers = '\x1b[2K'
    terminal_markers = ''
    lines = [
        line.strip().strip(terminal_markers)
        for line in (process.stdout + "\n" + process.stderr).split("\n") if line.strip()
        ]
    return lines, process.returncode

def load_json(line):
    try:
        return json.loads(line)
    except Exception:
        return None

list_res, list_code = run_command("docker exec coderd coder template list --token SgZNVKpSle-lzQ708JE4Rr7Lh3cmWwtAH --output json")

#print(load_json("".join(list_res)))
# print("".join(list_res))
# print(load_json("".join(list_res)))

templates = load_json("".join(list_res))

for element in templates:
    template = element["Template"]
    name = template["name"]
    print(name)
    run_command("mkdir -p " + name)
    run_command(f"docker exec coderd coder template pull {name} --token SgZNVKpSle-lzQ708JE4Rr7Lh3cmWwtAH --tar | tar -C {name} -xivf -")

run_command("git add . && git commit -m '$(date)' && git push")

#print(load_json("[]"))
