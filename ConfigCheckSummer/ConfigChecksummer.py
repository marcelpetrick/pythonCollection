# How to use?
# * adapt the path to the config.xml and the lumi_comm_tqboard_cli tool in the footer of this file
# * run the script
#
# Params to use (for instance):
# configFilePath = "LumiTOP_00000003/LumiTOP_00000003.xml"
# pathToCli = "C:/Repos/LumiSuite/build/CMake/Debug/build/bin/lumi_comm_tqboard_cli.exe"
#
# What does it do?
# It md5-checkums the given configuration file and writes the hash into the corresponding checksum-file.
# All TqBoard-based devices are then discovered and the output is parsed for IP and port (note: undefined behavior
# if several results). Then the two aforementioned files are uploaded to the TqBoard.
#
# Params to use (for instance):
# configFilePath = "LumiTOP_00000003/LumiTOP_00000003.xml"
# pathToCli = "C:/Repos/LumiSuite/build/CMake/Debug/build/bin/lumi_comm_tqboard_cli.exe"

# -------------------------------------------
def md5(filename):
    import hashlib

    # hash blobs of 4096 byte size
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# -------------------------------------------
def rewriteFile(checksumFilePath, newCheckSum):
    import fileinput
    for line in fileinput.input(checksumFilePath, inplace=True):
        if ".xml" in line:
            splittedLine = line.split(" = ")
            line = splittedLine[0] + " = " + str(newCheckSum) + "\n"

        import sys
        #print(line) # creates awkward newlines, so use sys
        sys.stdout.write(line)

# -------------------------------------------
def getIpAndPort(pathToCli):
    # identify used board and find ip and port
    import subprocess
    cli = subprocess.Popen([pathToCli, "detect"],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           shell=True)
    stdout, stderr = cli.communicate()
    # check the return code for errors
    if cli.returncode != 0:
        raise Exception("Path to cli executable not correct or wrong parameters.")
    print("stdout:", stdout.decode('ascii'))
    print("stderr:", stderr.decode('ascii'))

    # result is binary, just using str() to stringify it, results in leading "b"
    splittedOut = stdout.decode('ascii').split(":")
    ip = splittedOut[1].strip()
    port = splittedOut[2].replace("\\r", "").replace("\\n", "").strip() # remove the newline-stuff
    print("ip & port:", ip, ":", port)

    # --- just for testing!!! ---
    # check device info ..
    # does not work, because of space for the argument-string!
    #argString = "\"" + "-a" + str(ip) + " -p" + str(port) + " deviceInfo" + "\""

    argString0 = "-a" + str(ip)
    argString1 = "-p" + str(port)
    argString2 = "deviceInfo"
    print("argString:", argString0, argString1, argString2)
    cli = subprocess.Popen([pathToCli, argString0, argString1, argString2],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           shell=True)
    stdout, stderr = cli.communicate()
    # check the return code for errors
    if cli.returncode != 0:
        raise Exception("Path to cli executable not correct or wrong parameters.")
    print("stdout:", stdout.decode('ascii'))
    print("stderr:", stderr.decode('ascii'))
    # --- just for testing!!! ---

    return ip, port

# -------------------------------------------
def uploadFileTo(pathToCli, ip, port, pathToFile):
    import subprocess

    argString0 = "-a" + str(ip)
    argString1 = "-p" + str(port)
    argString2 = "upload"
    argString3RemoteName = pathToFile.split("/")[1]
    argString4LocalPath = pathToFile

    print("argString:", argString0, argString1, argString2, argString3RemoteName, argString4LocalPath)
    cli = subprocess.Popen([pathToCli, argString0, argString1, argString2, argString3RemoteName, argString4LocalPath],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           shell=True)
    stdout, stderr = cli.communicate()
    # check the return code for errors
    if cli.returncode != 0:
        raise Exception("Path to cli executable not correct or wrong parameters.")
    print("stdout:", stdout.decode('ascii'))
    print("stderr:", stderr.decode('ascii'))

# -------------------------------------------
def uploadToTqBoard(pathToCli, configFilePath):
    import subprocess

    # determine Tq-board
    ip, port = getIpAndPort(pathToCli)
    # upload config file
    uploadFileTo(pathToCli, ip, port, configFilePath)
    # upload checksum file
    checksumFilePath = configFilePath.replace(".xml", ".checksum")
    uploadFileTo(pathToCli, ip, port, checksumFilePath)

# ----------------- main function -----------------
def main():
    import sys

    # get the parameters
    if len(sys.argv) > 3:
        configFilePath = sys.argv[1]
        pathToCli = sys.argv[2]
    else:
        raise Exception("Not enough parameters specified: first must be PathToConfigFile, second PathToCLI-exectuable.")

    # checksum the configuration
    md5sum = md5(configFilePath)
    print("md5 for", configFilePath, ":", md5sum)

    # rewrite to checksum file
    checksumFilePath = configFilePath.replace(".xml", ".checksum")
    print("checksumFilePath:", checksumFilePath)
    rewriteFile(checksumFilePath, md5sum)

    # discover device and upload the two files
    uploadToTqBoard(pathToCli, configFilePath)

# ----------------- execution -----------------
if __name__ == "__main__":
    main()
