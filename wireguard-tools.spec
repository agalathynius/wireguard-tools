%global debug_package %{nil}

Name:           wireguard-tools
<<<<<<< HEAD
Version:        0.0.20180731
=======
Version:        0.0.20180708
>>>>>>> 09749b847a01e1070e9f7451fb56e72da14b0c40
Release:        1%{?dist}
Epoch:          1
URL:            https://www.wireguard.com/
Summary:        Fast, modern, secure VPN tunnel
License:        GPLv2
Group:          Applications/Internet

Source0:        https://git.zx2c4.com/WireGuard/snapshot/WireGuard-%{version}.tar.xz

%{?systemd_requires}
BuildRequires:  systemd
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  sed

Provides:       wireguard-tools = %{epoch}:%{version}-%{release}
Requires:       wireguard-dkms

%description
WireGuard is a novel VPN that runs inside the Linux Kernel and uses
state-of-the-art cryptography (the "Noise" protocol). It aims to be
faster, simpler, leaner, and more useful than IPSec, while avoiding
the massive headache. It intends to be considerably more performant
than OpenVPN. WireGuard is designed as a general purpose VPN for
running on embedded interfaces and super computers alike, fit for
many different circumstances. It runs over UDP.

This package provides the wg binary for controling WireGuard.

%prep
%setup -q -n WireGuard-%{version}

%build
## Start DNS Hatchet
cd %{_builddir}/WireGuard-%{version}/contrib/examples/dns-hatchet
./apply.sh

## End DNS Hatchet
cd %{_builddir}/WireGuard-%{version}/src
make tools

%install
mkdir -p %{buildroot}%{_bindir}
cd %{_builddir}/WireGuard-%{version}/src/tools
DESTDIR=%{buildroot} BINDIR=%{_bindir} MANDIR=%{_mandir} RUNSTATEDIR=/run \
    make install
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}/examples/
cp -fr %{_builddir}/WireGuard-%{version}/contrib/examples/* \
    %{buildroot}%{_defaultdocdir}/%{name}/examples/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(0755, root, root) %{_bindir}/wg
%attr(0755, root, root) %{_bindir}/wg-quick
%attr(0644, root, root) %{_datarootdir}/bash-completion/completions/wg
%attr(0644, root, root) %{_datarootdir}/bash-completion/completions/wg-quick
%attr(0644, root, root) %{_unitdir}/wg-quick@.service
%attr(0644, root, root) %{_mandir}/man8/wg.8*
%attr(0644, root, root) %{_mandir}/man8/wg-quick.8*
%{_defaultdocdir}/%{name}/examples

%doc README.md
%license COPYING
%{!?_licensedir:%global license %doc}

%changelog
