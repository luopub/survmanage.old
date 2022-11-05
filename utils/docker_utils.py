import subprocess


def run_host_cmd(cmd):
    # f'nsenter -m -u -i -n -p -t 1 sh -c "{cmd}"',
    resp = subprocess.run(
        f'nsenter -a -t 1 sh -c "{cmd}"',
        capture_output=True, check=True, text=True, shell=True)
    return {'stdout': resp.stdout, 'stderr': resp.stderr}
