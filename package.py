name = "OpenSubdiv"

version = "3.4.4"

authors = [
    "Pixar Animation Studio"
]

description = \
    """
    OpenSubdiv is a set of open source libraries that implement high performance
    subdivision surface (subdiv) evaluation on massively parallel
    CPU and GPU architectures.
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7", "!ptex"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "ptex-2.1.33"],
]

uuid = "repository.OpenSubdiv"

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.OPENSUBDIV_ROOT_DIR = "{root}"
    env.PATH.prepend("{root}/bin")
