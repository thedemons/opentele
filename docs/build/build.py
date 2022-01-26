import os, sys


def getsitepackages():
    import subprocess, re

    command = "pip show mkdocs-material"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output = process.communicate()[0].decode("utf-8").replace("\\", "\\\\")

    search = re.search(r"Location: (?P<location>.+)", output)
    if search == None:
        return None

    return os.path.abspath(search.group("location"))


def pre_build():
    print("Running build.py pre_build")

    sitepackages_path = getsitepackages()
    assert sitepackages_path

    pymdownx_dir = os.path.join(sitepackages_path, "pymdownx")
    assert os.path.isdir(pymdownx_dir)

    highlight_py = os.path.join(pymdownx_dir, "highlight.py")
    highlight_bk_py = os.path.join(pymdownx_dir, "highlight_bk.py")
    assert os.path.isfile(highlight_py)

    os.rename(highlight_py, highlight_bk_py)
    assert os.path.isfile(highlight_bk_py)

    build_dir = os.path.join(os.path.abspath(os.path.curdir), "docs", "build")
    assert os.path.isdir(build_dir)

    moves = ["highlight.py", "highlight_resolver.py", "vspythonlexer.py"]
    for file in moves:
        mv_from = os.path.join(build_dir, file)
        mv_to = os.path.join(pymdownx_dir, file)

        print("Renaming {} to {}".format(mv_from, mv_to))

        assert os.path.isfile(mv_from)
        os.rename(mv_from, mv_to)
        assert os.path.isfile(mv_to)


def post_build():
    print("Running build.py post_build")
    # we don't need to check for errors because if something's wrong, it's already raised in pre_build
    pymdownx_dir = os.path.join(getsitepackages(), "pymdownx")
    build_dir = os.path.join(os.path.abspath(os.path.curdir), "docs", "build")

    moves = ["highlight.py", "highlight_resolver.py", "vspythonlexer.py"]
    for file in moves:
        mv_from = os.path.join(pymdownx_dir, file)
        mv_to = os.path.join(build_dir, file)

        print("Renaming {} to {}".format(mv_from, mv_to))
        os.rename(mv_from, mv_to)

    highlight_py = os.path.join(pymdownx_dir, "highlight.py")
    highlight_bk_py = os.path.join(pymdownx_dir, "highlight_bk.py")

    os.rename(highlight_bk_py, highlight_py)


def main():
    assert len(sys.argv) == 2
    if sys.argv[1] == "pre":
        pre_build()
    elif sys.argv[1] == "post":
        post_build()
    else:
        raise Exception("Invalid arguments")


if __name__ == "__main__":
    main()
