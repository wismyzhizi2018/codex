#!/usr/bin/env python3
"""Generate npm package.json for @cc-claw/codex platform packages."""
import json, sys, os

def make_platform_pkg(out_dir: str, platform: str, arch: str, version: str):
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(f"{out_dir}/bin", exist_ok=True)
    with open(f"{out_dir}/package.json", "w") as f:
        json.dump({
            "name": f"@cc-claw/codex-{platform}-{arch}",
            "version": version,
            "description": f"Codex CLI native binary for {platform}-{arch}",
            "license": "Apache-2.0",
            "os": [platform],
            "cpu": [arch],
            "type": "module",
            "engines": {"node": ">=16"},
            "files": ["bin"],
            "bin": {"codex": "bin/codex"}
        }, f, indent=2)

def make_main_pkg(out_dir: str, version: str):
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(f"{out_dir}/bin", exist_ok=True)
    with open(f"{out_dir}/package.json", "w") as f:
        json.dump({
            "name": "@cc-claw/codex",
            "version": version,
            "description": "Codex CLI - coding agent (cc-claw fork)",
            "license": "Apache-2.0",
            "bin": {"codex": "bin/codex.js"},
            "type": "module",
            "engines": {"node": ">=16"},
            "files": ["bin"],
            "optionalDependencies": {
                "@cc-claw/codex-linux-x64": version,
                "@cc-claw/codex-win32-x64": version
            }
        }, f, indent=2)

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "platform":
        # python3 make-npm-package.py platform <out_dir> <platform> <arch> <version>
        make_platform_pkg(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif cmd == "main":
        # python3 make-npm-package.py main <out_dir> <version>
        make_main_pkg(sys.argv[2], sys.argv[3])
    else:
        print("Usage: python3 make-npm-package.py [platform|main] <args...>")
        sys.exit(1)
