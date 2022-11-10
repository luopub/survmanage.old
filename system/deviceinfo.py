# https://cloud.tencent.com/developer/article/1569912
import os
import platform
import subprocess

# 内存信息 / meminfo
# 返回dict
HOSTINFO_ROOT = os.environ.get('HOSTINFO_ROOT')

PATH_MEMINFO = f'{HOSTINFO_ROOT}/proc/meminfo'
PATH_CPUINFO = f'{HOSTINFO_ROOT}/proc/cpuinfo'
PATH_LOADAVG = f'{HOSTINFO_ROOT}/proc/loadavg'
PATH_UPTIME = f'{HOSTINFO_ROOT}/proc/uptime'
PATH_NETDEV = f'{HOSTINFO_ROOT}/proc/net/dev'
PATH_OS_RELEASE = f'{HOSTINFO_ROOT}/usr/lib/os-release'
PATH_HOSTNAMECTL = f'{HOSTINFO_ROOT}/usr/bin/hostnamectl'  # Not valid in docker
PATH_UNAME = f'{HOSTINFO_ROOT}/bin/uname'


# !/usr/bin/env python
def memory_stat():
    fake_value = {
      "MemTotal": 15622070272.0,
      "MemFree": 237203456.0,
      "MemAvailable": 187793408.0,
      "Buffers": 3772416.0,
      "Cached": 172814336.0,
      "SwapCached": 16445440.0,
      "Active": 2026762240.0,
      "Inactive": 2787012608.0,
      "Active(anon)": 1972977664.0,
      "Inactive(anon)": 2754174976.0,
      "Active(file)": 53784576.0,
      "Inactive(file)": 32837632.0,
      "Unevictable": 18886656.0,
      "Mlocked": 65536.0,
      "SwapTotal": 7811022848.0,
      "SwapFree": 0.0,
      "Dirty": 18427904.0,
      "Writeback": 0.0,
      "AnonPages": 4642041856.0,
      "Mapped": 122478592.0,
      "Shmem": 71208960.0,
      "KReclaimable": 83828736.0,
      "Slab": 267472896.0,
      "SReclaimable": 83828736.0,
      "SUnreclaim": 183644160.0,
      "KernelStack": 16416768.0,
      "PageTables": 109727744.0,
      "NFS_Unstable": 0.0,
      "Bounce": 0.0,
      "WritebackTmp": 0.0,
      "CommitLimit": 15622057984.0,
      "Committed_AS": 40931651584.0,
      "VmallocTotal": 138537122856960.0,
      "VmallocUsed": 68583424.0,
      "VmallocChunk": 0.0,
      "Percpu": 4300800.0,
      "HardwareCorrupted": 0.0,
      "AnonHugePages": 620756992.0,
      "ShmemHugePages": 0.0,
      "ShmemPmdMapped": 0.0,
      "FileHugePages": 0.0,
      "FilePmdMapped": 0.0,
      "CmaTotal": 67108864.0,
      "CmaFree": 1880064.0,
      "HugePages_Total": 0.0,
      "HugePages_Free": 0.0,
      "HugePages_Rsvd": 0.0,
      "HugePages_Surp": 0.0,
      "Hugepagesize": 2097152.0,
      "Hugetlb": 0.0,
      "MemUsed": 15208280064.0
    }
    if platform.system().lower() != 'linux':
        return fake_value
    mem = {}
    f = open(PATH_MEMINFO)
    lines = f.readlines()
    f.close()
    for line in lines:
        if len(line) < 2: continue
        name = line.split(':')[0]
        var = line.split(':')[1].split()[0]
        mem[name] = int(var) * 1024.0
    mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
    return mem


# CPU信息 / cpuinfo
# 返回list，每核心一dict


# !/usr/bin/env python
def cpu_stat():
    fake_value = {
        'cpu': [{
            "processor": " 0",
            "model name": " ARMv8 Processor rev 0 (v8l)",
            "BogoMIPS": " 62.50",
            "Features": " fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm dcpop",
            "CPU implementer": " 0x4e",
            "CPU architecture": " 8",
            "CPU variant": " 0x0",
            "CPU part": " 0x004",
            "CPU revision": " 0",
            "MTS version": " 55637613"
        }],
        'usage': '80.5%'
    }
    if platform.system().lower() != 'linux':
        return fake_value
    cpu = []
    cpuinfo = {}
    f = open(PATH_CPUINFO)
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            cpu.append(cpuinfo)
            cpuinfo = {}
        if len(line) < 2: continue
        name = line.split(':')[0].rstrip()
        var = line.split(':')[1]
        cpuinfo[name] = var

    # Add cpu usage
    cmd = "top -bi -n 1 | grep %Cpu"
    resp = subprocess.run(
        f'sh -c "{cmd}"',
        capture_output=True, check=True, text=True, shell=True)
    line = resp.stdout
    user = float(line.split()[1])
    sys = float(line.split()[3])

    return {'cpu': cpu, 'usage': f'{user+sys}%'}


# cpu负载信息 / loadavg
# 返回dict


# !/usr/bin/env python
def load_stat():
    fake_value = {
      "lavg_1": "8.86",
      "lavg_5": "8.66",
      "lavg_15": "8.63",
      "nr": "16/1002",
      "last_pid": "53929"
    }
    if platform.system().lower() != 'linux':
        return fake_value
    loadavg = {}
    f = open(PATH_LOADAVG)
    con = f.read().split()
    f.close()
    loadavg['lavg_1'] = con[0]
    loadavg['lavg_5'] = con[1]
    loadavg['lavg_15'] = con[2]
    loadavg['nr'] = con[3]
    loadavg['last_pid'] = con[4]
    return loadavg


# 运转时间 / Uptime
# 返回dict


# !/usr/bin/env python
def uptime_stat():
    fake_value = {
      "day": 3,
      "hour": 21,
      "minute": 53,
      "second": 9,
      "Free rate": 1.8276147855875597
    }
    if platform.system().lower() != 'linux':
        return fake_value
    uptime = {}
    f = open(PATH_UPTIME)
    con = f.read().split()
    f.close()
    all_sec = float(con[0])
    MINUTE, HOUR, DAY = 60, 3600, 86400
    uptime['day'] = int(all_sec / DAY)
    uptime['hour'] = int((all_sec % DAY) / HOUR)
    uptime['minute'] = int((all_sec % HOUR) / MINUTE)
    uptime['second'] = int(all_sec % MINUTE)
    uptime['Free rate'] = float(con[1]) / float(con[0])
    return uptime


# 获取网卡流量信息 / proc / net / dev
# 返回dict, 单位byte


# !/usr/bin/env python
def net_stat():
    fake_value = [
        {
            "interface": "eth0",
            "ReceiveBytes": 242298980636,
            "ReceivePackets": 180784171,
            "ReceiveErrs": 0,
            "ReceiveDrop": 0,
            "ReceiveFifo": 0,
            "ReceiveFrames": 0,
            "ReceiveCompressed": 0,
            "ReceiveMulticast": 0,
            "TransmitBytes": 3478764092,
            "TransmitPackets": 42529343,
            "TransmitErrs": 0,
            "TransmitDrop": 0,
            "TransmitFifo": 0,
            "TransmitFrames": 0,
            "TransmitCompressed": 0,
            "TransmitMulticast": 0
        },
    ]
    if platform.system().lower() != 'linux':
        return fake_value
    net = []
    f = open(PATH_NETDEV)
    lines = f.readlines()
    f.close()
    for line in lines[2:]:
        con = line.split()
        """ 
        intf = {} 
        intf['interface'] = con[0].lstrip(":") 
        intf['ReceiveBytes'] = int(con[1]) 
        intf['ReceivePackets'] = int(con[2]) 
        intf['ReceiveErrs'] = int(con[3]) 
        intf['ReceiveDrop'] = int(con[4]) 
        intf['ReceiveFifo'] = int(con[5]) 
        intf['ReceiveFrames'] = int(con[6]) 
        intf['ReceiveCompressed'] = int(con[7]) 
        intf['ReceiveMulticast'] = int(con[8]) 
        intf['TransmitBytes'] = int(con[9]) 
        intf['TransmitPackets'] = int(con[10]) 
        intf['TransmitErrs'] = int(con[11]) 
        intf['TransmitDrop'] = int(con[12]) 
        intf['TransmitFifo'] = int(con[13]) 
        intf['TransmitFrames'] = int(con[14]) 
        intf['TransmitCompressed'] = int(con[15]) 
        intf['TransmitMulticast'] = int(con[16]) 
        """
        intf = dict(
            zip(
                ('interface', 'ReceiveBytes', 'ReceivePackets',
                 'ReceiveErrs', 'ReceiveDrop', 'ReceiveFifo',
                 'ReceiveFrames', 'ReceiveCompressed', 'ReceiveMulticast',
                 'TransmitBytes', 'TransmitPackets', 'TransmitErrs',
                 'TransmitDrop', 'TransmitFifo', 'TransmitFrames',
                 'TransmitCompressed', 'TransmitMulticast'),
                (con[0].rstrip(":"), int(con[1]), int(con[2]),
                 int(con[3]), int(con[4]), int(con[5]),
                 int(con[6]), int(con[7]), int(con[8]),
                 int(con[9]), int(con[10]), int(con[11]),
                 int(con[12]), int(con[13]), int(con[14]),
                 int(con[15]), int(con[16]),)
            )
        )
        net.append(intf)
    return net


# 磁盘空间使用
# 使用内置python内置函数，返回dict, 单位byte


# !/usr/bin/env python
def disk_stat():
    fake_value = {
      "available": 823484755968,
      "capacity": 920235909120,
      "used": 49934331904
    }
    if platform.system().lower() != 'linux':
        return fake_value
    hd = {}
    disk = os.statvfs("/")
    hd['available'] = disk.f_bsize * disk.f_bavail
    hd['capacity'] = disk.f_bsize * disk.f_blocks
    hd['used'] = disk.f_bsize * (disk.f_blocks - disk.f_bavail)
    return hd


# 版本信息
def release_stat():
    fake_value = {
      "NAME": "Ubuntu",
      "VERSION": "20.04.4 LTS (Focal Fossa)",
      "ID": "ubuntu",
      "ID_LIKE": "debian",
      "PRETTY_NAME": "Ubuntu 20.04.4 LTS",
      "VERSION_ID": "20.04",
      "HOME_URL": "https://www.ubuntu.com/",
      "SUPPORT_URL": "https://help.ubuntu.com/",
      "BUG_REPORT_URL": "https://bugs.launchpad.net/ubuntu/",
      "PRIVACY_POLICY_URL": "https://www.ubuntu.com/legal/terms-and-policies/privacy-policy",
      "VERSION_CODENAME": "focal",
      "UBUNTU_CODENAME": "focal"
    }
    if platform.system().lower() != 'linux':
        return fake_value
    f = open(PATH_OS_RELEASE)
    lines = f.readlines()
    f.close()
    release = {}
    for line in lines:
        name, value = line.strip().split('=')
        if value.startswith('"'):
            value = value[1:-1]
        release[name] = value
    return release


# 硬件及host, docker里面没有hostnamectl命令！！！
def host_stat():
    fake_value = {
      "Static hostname": "ubuntu",
      "Icon name": "computer",
      "Machine ID": "dbfef1aa0b064bcf9d30ec3ad0886edb",
      "Boot ID": "23148f40433d4c5abc9d282deb6ae09f",
      "Operating System": "Ubuntu 20.04.4 LTS",
      "Kernel": "Linux 5.10.104-tegra",
      "Architecture": "arm64"
    }
    if platform.system().lower() != 'linux':
        return fake_value
    r = os.popen(PATH_HOSTNAMECTL)
    lines = r.read().split('\n')
    host = {}
    for line in lines:
        if not ':' in line:
            continue
        name, value = line.strip().split(':')
        host[name] = value.strip()
    return host


# 硬件及host, docker里面没有hostnamectl命令！！！
def uname_stat():
    # "uname -a": Linux d1726ddea902 5.10.104-tegra #1 SMP PREEMPT Wed Aug 10 20:17:07 PDT 2022 aarch64 GNU/Linux
    fake_value = {
        "Operating System": "Linux",
        "Kernel": "5.10.104-tegra",
        "Architecture": "aarch64"
    }
    if platform.system().lower() != 'linux':
        return fake_value

    r = os.popen(f'{PATH_UNAME} -a')
    items = r.read().strip().split(' ')
    uname = {
        "Operating System": items[0],
        "Kernel": items[2],
        "Architecture": items[-2]
    }
    return uname
