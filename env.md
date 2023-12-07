Programming Environment Requirements
====================================

Laptops are required for all CPSC courses and should be available in the classroom each day.

Unless otherwise specified, programming assignments for this course have been tested to work in an environment similar to the following:

- Linux kernel version: 5.10
- Architecture: [x64](https://en.wikipedia.org/wiki/X86-64)
- `python` version: 3.9
- `gcc` version: 10.2
- `make` version: 4.3

While assignments are generally designed to work in a wide variety of environments, it is strongly recommended to have an environment as close to the one described above as possible. If you do not run x64 Linux natively on your machine, a virtualized environment can be used via tools such as [QEMU](https://www.qemu.org/), [virt-manager](https://virt-manager.org/), or [VirtualBox](https://www.virtualbox.org/).

It is recommended to install a Debian-based distribution such as Debian itself, Ubuntu, or Kali. You can either download the install media and run through the installation process yourself or you can download a pre-installed image from a provider such as [Linux VM Images](https://www.linuxvmimages.com/)  or [OSBoxes](https://www.osboxes.org/).

The following are explicitly unsupported:

- Python versions prior to 3.7, as these are [no longer officially supported](https://devguide.python.org/versions/).
- Any compiled programs for architectures other than x64. If you are using a machine with a different architecture, you will need a virtualized x64 environment.

Setup Notes
===========

Hosted Environments
-------------------

You may choose to run Linux in the cloud rather than on your own machine if desired. There are many providers that offer virtual Linux servers for a low cost or even for free. Here are a few that offer free or discounted Linux virtual servers.

- [Google Cloud Platform](https://cloud.google.com/) (Free e2-micro instance)
- [Amazon Web Services](https://aws.amazon.com/) (Free for first year)
- [Microsoft Azure](https://azure.microsoft.com/) (Free for first year)
- [Oracle Cloud](https://www.oracle.com/cloud/) (Free ARM instance)

ARM Mac Setup
-------------

M1 and M2 Macs may be especially challenging due to not all software being ported to the architecture yet. The following should work to run an x64 VM using QEMU.

1. Install Homebrew (`brew`) if you have not already done so by running the following command:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Full instructions are available on the [Homebrew site](https://brew.sh/).

2. Install QEMU using `brew`

```
brew install qemu
```

3. Pick or create a directory for your VM and `cd` into it. For example:

```sh
mkdir ~/debian
cd ~/debian
```

4. Create a disk image for the VM. Something like the following should be sufficient:

```
qemu-img create -f qcow2 disk.qcow2 16G
```

This creates a new 16 GB disk image called `disk.qcow2` in the current directory.

5. Download install media for the OS of your choosing. Once downloaded, move the file to your VM directory and name it `install.iso`.

6. Open a text editor and create a startup script named `run` with the following contents:

```sh
#!/bin/bash

sudo qemu-system-x86_64 \
  -device virtio-net,netdev=net0 -netdev user,id=net0 \
  -m 4192M \
  -monitor stdio \
  -hda disk.qcow2 \
  -cdrom install.iso
```

7. Ensure the `run` file is executable:

```
chmod 755 run
```

8. Start the VM and complete the install process. Note that this is also how you will run the VM going forward:

```
./run
```

Or from anywhere on the system:

```
~/debian/run
```
