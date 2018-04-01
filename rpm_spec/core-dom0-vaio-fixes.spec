%{!?version: %define version %(cat version_vaio_fixes)}

Name:		qubes-core-dom0-vaio-fixes
Version:	%{version}
Release:	1%{?dist}
Summary:    Additional scripts for supporting suspend on Vaio Z laptops
Requires:   alsa-utils

Group:		Qubes
Vendor:		Invisible Things Lab
License:	GPL
URL:		http://www.qubes-os.org

%description
Additional scripts for supporting suspend on Vaio Z laptops.

Due to broken Linux GPU drivers we need to do some additional actions during
suspend/resume.

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib64/pm-utils/sleep.d
cp vaio-fixes/00sony-vaio-audio $RPM_BUILD_ROOT/usr/lib64/pm-utils/sleep.d/
cp vaio-fixes/99sony-vaio-audio $RPM_BUILD_ROOT/usr/lib64/pm-utils/sleep.d/
mkdir -p $RPM_BUILD_ROOT/etc/modprobe.d/
cp vaio-fixes/snd-hda-intel-sony-vaio.conf $RPM_BUILD_ROOT/etc/modprobe.d/

%files
/usr/lib64/pm-utils/sleep.d/00sony-vaio-audio
/usr/lib64/pm-utils/sleep.d/99sony-vaio-audio
/etc/modprobe.d/snd-hda-intel-sony-vaio.conf
