# Task
# Set the release version to the corresponding files.
# Right now `03_SourceCode\hmi\doc\Doxyfile` and `03_SourceCode\hmi\src\cpp\version.h` need to be modified.
# The script is dumb and does hard replacement. Any typos in the input result in faulty output.

# Usage
# `python3 setReleaseVersion.py 1.11.7`

# ----------------- commit changes  -----------------
def commit(versionToUse):
    from git import Repo # run`pip install gitpython` and make sure git is in PATH or found otherwise

    path = '../../.git' # has to point to the real git-repo-path
    repo = Repo.init(path).git
    index = Repo.init(path).index

    repo.add("03_SourceCode/hmi/doc/Doxyfile")
    repo.add("03_SourceCode/hmi/src/cpp/version.h")
    index.commit(f"v{versionToUse}: adapted for the release")

# ----------------- edit files -----------------
def editFiles(versionToUse):
    # set first the Doxyfile
    import fileinput
    for line in fileinput.input("../../03_SourceCode/hmi/doc/Doxyfile", inplace=True):
        if not line.startswith("PROJECT_NUMBER"):
            print(line, end='')
        else:
            print(f"PROJECT_NUMBER         = v{versionToUse}\n", end='')

    # fix now the version.h
    for line in fileinput.input("../../03_SourceCode/hmi/src/cpp/version.h", inplace=True):
        major, minor, patch = versionToUse.split('.')
        if line.startswith("#define VERSION_MAJOR"):
            print(f"#define VERSION_MAJOR       {major}\n", end='')
        elif line.startswith("#define VERSION_MINOR"):
            print(f"#define VERSION_MINOR       {minor}\n", end='')
        elif line.startswith("#define VERSION_PATCH"):
            print(f"#define VERSION_PATCH       {patch}\n", end='')
        else:
            print(line, end='')

# ----------------- main function -----------------
def main():
    import sys

    # get the parameters
    if len(sys.argv) == 2:
        versionToUse = sys.argv[1]
        print("Version to use:", versionToUse)
    else:
        raise Exception("Exactly one parameter needed: call `python3 setReleaseVersion.py 1.11.7`.")

    editFiles(versionToUse)
    commit(versionToUse)

#---------------------------------------------------
main()
