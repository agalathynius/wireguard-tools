%global debug_package %{nil}

Name:           wireguard-tools
Version:        0.0.20180514
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
##cd %{_builddir}/WireGuard-%{version}/contrib/examples/dns-hatchet
##./apply.sh
## don't care about resolvconf
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
* Sun May 13 2018 Joe Doss <joe@solidadmin.com> - 0.0.20180513-1
- Update to 0.0.20180513

* Fri Apr 20 2018 Joe Doss <joe@solidadmin.com> - 0.0.20180420-1
- Update to 0.0.20180420

* Sun Apr 15 2018 Joe Doss <joe@solidadmin.com> - 0.0.20180413-1
- Update to 0.0.20180413

* Mon Mar 05 2018 Joe Doss <joe@solidadmin.com> - 0.0.20180304-1
- Update to 0.0.20180304

* Mon Feb 19 2018 Joe Doss <joe@solidadmin.com> - 0.0.20180218-1
- Update to 0.0.20180218

* Sun Feb 04 2018 Joe Doss <joe@solidadmin.com> - 0.0.20180202-1
- Update to 0.0.20180202

* Thu Jan 18 2018 Joe Doss <joe@solidadmin.com> - 0.0.20180118-1
- Update to 0.0.20180118

* Thu Dec 21 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171221-1
- Update to 0.0.20171221

* Tue Dec 12 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171211-1
- Update to 0.0.20171211

* Mon Nov 27 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171127-1
- Update to 0.0.20171127

* Thu Nov 23 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171122-1
- Update to 0.0.20171122

* Sat Nov 11 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171111-1
- Update to 0.0.20171111

* Wed Nov 01 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171101-1
- Update to 0.0.20171101
- Add temporary DNS hatchet to wg-quick

* Thu Oct 26 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171017-1
- Update to 0.0.20171017

* Wed Oct 11 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171011-1
- Update to 0.0.20171011

* Fri Oct 6 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171005-1
- Update to 0.0.20171005
- Update RPM spec URL to www.wireguard.com

* Mon Oct 2 2017 Joe Doss <joe@solidadmin.com> - 0.0.20171001-1
- Update to 0.0.20171001

* Mon Sep 18 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170918-1
- Update to 0.0.20170918
- Drop support for RHEL 7.3, moving on instead to RHEL 7.4.

* Thu Sep 7 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170907-1
- Update to 0.0.20170907

* Wed Aug 9 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170810-1
- Update to 0.0.20170810

* Mon Jul 31 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170726-1
- Update to 0.0.20170726

* Thu Jun 29 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170629-1
- Update to 0.0.20170629

* Tue Jun 13 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170613-1
- Update to 0.0.20170613

* Mon Jun 12 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170612-1
- Update to 0.0.20170612

* Wed May 31 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170531-1
- Update to 0.0.20170531

* Wed May 17 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170517-1
- Update to 0.0.20170517

* Mon Apr 24 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170421-1
- Update to 0.0.20170421

* Mon Apr 10 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170409-1
- Update to 0.0.20170409

* Fri Mar 24 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170324-1
- Update to 0.0.20170324

* Mon Mar 20 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170320.1-1
- Update to 0.0.20170320.1

* Thu Mar 2 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170223-1
- Update to 0.0.20170223

* Thu Feb 16 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170214-1
- Update to 0.0.20170214

* Thu Jan 5 2017 Joe Doss <joe@solidadmin.com> - 0.0.20170105-1
- Update to 0.0.20170105
- Add wg-quick, bash-completion, and systemd service

* Mon Dec 19 2016 Jason A. Donenfeld <jason@zx2c4.com> - 0.0.20161218-1
- Spec adjustments

* Wed Aug 17 2016 Joe Doss <joe@solidadmin.com> - 0.0.20160808-2
- Spec adjustments

* Mon Aug 15 2016 Joe Doss <joe@solidadmin.com> - 0.0.20160808-1
- Initial WireGuard Tools RPM
- Version 0.0.20160808
