%global debug_package %{nil}

Name:           wireguard-tools
Version:        0.0.20161218
Release:        1%{?dist}
Epoch:          1
URL:            https://www.wireguard.io/
Summary:        Fast, modern, secure VPN tunnel
License:        GPLv2
Group:          Applications/Internet

Source0:        https://git.zx2c4.com/WireGuard/snapshot/WireGuard-%{version}.tar.xz

BuildRequires:  pkgconfig(libmnl)

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
%attr(0644, root, root) %{_mandir}/man8/wg.8*
%{_defaultdocdir}/%{name}/examples

%doc README.md
%license COPYING
%{!?_licensedir:%global license %doc}

%changelog
* Mon Dec 19 2016 Jason A. Donenfeld <jason@zx2c4.com> - 0.0.20161218-1
- Spec adjustments

* Wed Aug 17 2016 Joe Doss <joe@solidadmin.com> - 0.0.20160808-2
- Spec adjustments

* Mon Aug 15 2016 Joe Doss <joe@solidadmin.com> - 0.0.20160808-1
- Initial WireGuard Tools RPM
- Version 0.0.20160808
