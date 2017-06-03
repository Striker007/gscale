import requests

from fabric.api import *
from fabric.network import *


la_high = 20.0
path_script_trigger = "./env/bin/python ./cloud_bay/main.py --only-price"
path_script_iptables = "./env/bin/python ./cloud_bay/main.py --only-price"

# web workers white IP
hosts_wan_ip = ["192.168.0.1"]

env.skip_bad_hosts = True  # ignore hosts in DOWN state, we also should ignore when create upstreams
env.user = "ci"
env.key_filename = "~/.ssh/id_rsa"
env.colorize_errors = True
env.la = []
env.roledefs = {
    "proxy": hosts
}


@task
def check_LA():
    env.la.append(execute(get_la_by_web).values())
    disconnect_all()
    env.la = env.la[0][0] # TODO one return format get_la_by_web AND get_la_by_ssh
    la = la_sum()

    if la_high <= la:
        print("high LA {0}, limit {1}".format(la, la_high))
        local(path_script_trigger)
    else:
        print("low LA {0}, limit {1}".format(la, la_high))


@task
def get_la_by_web():
    la_all = []
    for host in hosts_wan_ip:
        try:
            r = requests.get("http://" + host + "/ops-loadaverage", timeout=1)
            print host
            print (r.text)
            la = r.text.split(" ")
            """ get load average for 15 min """
            la = float(la[2])
        except:
            """ think about high LA limit  - like add some value insted 0.0 from downed node """
            print(".")
            print(host)
            la = 0.0
        la_all.append(la)
    return la_all


@task
@roles("proxy")
def get_la_by_ssh():
    with settings(warn_only=True):
        with hide("stdout", ):
            """ get load average for 15 min """
            try:
                la = run("python -c 'import os; print(os.getloadavg())[2]'")
                la = float(la)
                return la
            except:
                """ think about high LA limit  - like add some value insted 0.0 from downed node """
                return 0.0


def la_sum():
    return sum(env.la)
