import psutil as ps, platform as pf, os, subprocess as sproc, cpuinfo as ci, socket

KERNEL = (pf.system()) + ' ' + (pf.uname().release if pf.uname().release != '' else "undeterminable")
NAME = (pf.freedesktop_os_release()['PRETTY_NAME'] if pf.freedesktop_os_release()['PRETTY_NAME'] != '' else "undeterminable") + ' ' + pf.machine()
CPU = (ci.get_cpu_info()['brand_raw'] + ' ' + '(x'+str(ps.cpu_count(logical=True))+')') 
HOSTNAME = socket.gethostname()
USER = os.getlogin()
MEM = ps.virtual_memory()
MEM_MAX = round((MEM.total) / (1024 ** 3), 2)
MEM_FREE = round((MEM.available) / (1024 ** 3), 2)
MEM_USED = round((MEM_MAX - MEM_FREE), 2) #reason for not using MEM.used instead is because that is not how 'htop' or 'free' calculate used memory, they include cached memory aswell
MEM_PER = round((MEM_USED/MEM_MAX) * 100)
DISK = ps.disk_usage('/')
DISK_MAX = round((DISK.total) / (1024 ** 3), 2)
DISK_USED = round((DISK.used) / (1024 ** 3), 2)
DISK_PER = round((DISK_USED/DISK_MAX) * 100)

SWAP = ps.swap_memory()
SWAP_MAX = round((SWAP.total) / (1024 ** 3), 2)
SWAP_FREE = round((SWAP.free) / (1024 ** 3), 2)
SWAP_USED = round((SWAP_MAX - SWAP_FREE), 2)
SWAP_PER = round((SWAP_USED/SWAP_MAX) * 100)
def pacman():
    try:
        result = sproc.run(['pacman', '-Q'], stdout=sproc.PIPE, text=True, check=True)
        package_count = len(result.stdout.splitlines())
        return str(package_count)
    except sproc.CalledProcessError:
        return "Error fetching package count"

PACKAGES = pacman()
TERM = os.getenv("TERM")
SHELL = os.getenv("SHELL")

def lip():
    try:
        hostname = "8.8.8.8"  # Google Public DNS
        port = 80
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect((hostname, port))
            local_ip = s.getsockname()[0]
        return local_ip
    except Exception as e:
        return f"Error fetching local IP: {e}"

IP = lip()
COL = {
    'd': "\033[0m",
    'p': "\033[38;2;138;43;226m",
    'pb': "\033[1;38;2;138;43;226m"
}
MNAME = f"{COL['d']}{NAME}{COL['pb']}"
NKERNEL = f"Kernel: {COL['d']}{KERNEL}{COL['pb']}"
NPKG = f"Packages: {COL['d']}{PACKAGES}{COL['pb']}"
NCPU = f"CPU: {COL['d']}{CPU}{COL['pb']}"
NMEM = f"Memory: {COL['d']}{MEM_USED}GiB / {MEM_MAX}GiB ({MEM_PER}%){COL['pb']}"
NTERM = f"Terminal: {COL['d']}{TERM}{COL['pb']}"
NDISK = f"Disk (/): {COL['d']}{DISK_USED}GiB / {DISK_MAX}GiB ({DISK_PER}%){COL['pb']}"
NHNUN = f"{COL['d']}{USER}{COL['pb']}@{COL['d']}{HOSTNAME}{COL['pb']}"
NSHELL = f"Shell: {COL['d']}{SHELL}{COL['pb']}"
NLIP = f"Local IP: {COL['d']}{IP}{COL['pb']}"
NSWAP = f"Swap: {COL['d']}{SWAP_USED}GiB / {SWAP_MAX}GiB ({SWAP_PER}%){COL['pb']}"


def exc():
    print(f"""{COL['pb']}
                                                  .=*=          {MNAME} 
                                        +=-::-=+#@@@-               
                                        #@@@@@@@@@%.            {NKERNEL}
                                        @@@@@@@@@%.             {NPKG} 
                                       +@@@@@@@@@-              {NCPU} 
                                      +@@@@@@@#*=               {NMEM} 
                               .     +@@@@@@+                   {NSWAP} 
            .+.            -  .*#  .#@@@@@@+                    {NDISK}
           .%@@#-          %@@@@@%*@@@@@@@@                     {NSHELL}
          +@@@@@@@#=:.     *@@@@@@@@@@@@@@@                     {NTERM}
        =@@@@@@@@@@@@@@%###@@@@@@@@@@@@@@@%.                    {NLIP} 
     -*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*.                       
    :::-=+#@@@@@@@@@@@@@@@@@@@@@@@@@@*.                         {NHNUN} 
           .*#+:    -%@@@@@##*#%@@@@+                            
                      #@*:      .-#%                            VampFetch <3  

     {COL['d']}""")

