WINDOWS_SYS_FILENAMES = [
    "syspkg.dll",
    "errmsg.dat",
    "warn.conf",
    "userdata.db",
    "package.conf",
    "yarn.lock",
    "libc.dll",
    "systemd.proc",
    ".cmdconfig",
    ".bashrc",
    ".profile",
    "defender.exe",
]

COMMANDS = [
    "Get-Network-Policy",
    "SSHConnectionPool",
    "RDPPortAccess",
    "Port-Scan",
    "net stat user %USER",
]

DISKNAME = "C:/"
FOLDER_NAMES = [
    "System32",
    "Windows",
    "AppData\\Local",
    "AppData\\Roaming",
    "Program Files",
]


WINDOWS_ERROR_CODES = [
    {
        "code": "0x2",
        "title": "ERROR_FILE_NOT_FOUND",
        "text": "The system cannot find the file {}.",
        "type": "path",
    },
    {
        "code": "0x3",
        "title": "ERROR_PATH_NOT_FOUND",
        "text": "The system cannot find the path {}.",
        "type": "path",
    },
    {
        "code": "0x4",
        "title": "ERROR_TOO_MANY_OPEN_FILES",
        "text": "Too many open files",
        "type": "none",
    },
    {
        "code": "0x8",
        "title": "ERROR_NOT_ENOUGH_MEMORY",
        "text": "Not enough memory resources are available to process command {}.",
        "type": "command",
    },
]
