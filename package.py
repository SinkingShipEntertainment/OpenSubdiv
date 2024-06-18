name = "OpenSubdiv"

version = "3.6.0"

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
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
    "clew",
    "glfw",
    "tbb",
]

private_build_requires = [
]

variants = [
    ["python-3.7"],
    ["python-3.9"],
    ["python-3.11"],
]

uuid = "repository.OpenSubdiv"

def pre_build_commands():
    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        command("source /opt/rh/devtoolset-6/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass

def commands():
    env.OPENSUBDIV_ROOT_DIR = "{root}"
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")