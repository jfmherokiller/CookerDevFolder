%global debug_package %{nil}

Name:     moreutils
Version:  0.69
Release:  1%{?dist}
Summary:  Additional Unix utilities
License:  GPLv2+

URL:      https://joeyh.name/code/moreutils/
Source0:  http://deb.debian.org/debian/pool/main/m/moreutils/moreutils_%{version}.orig.tar.xz

Requires: perl(TimeDate)
Requires: perl(Time::Duration)
BuildRequires: libxml2-utils
BuildRequires: xsltproc
BuildRequires: docbook-style-xsl

Patch: moreutils-fixes.patch

Group: Faker
%description
%{summary}

%prep
%autosetup -p1

%build
%make_build

%install
%make_install

%files
%{_bindir}/isutf8
%{_bindir}/ifdata 
%{_bindir}/ifne 
%{_bindir}/pee 
%{_bindir}/sponge 
%{_bindir}/mispipe 
%{_bindir}/lckdo 
%{_bindir}/parallel 
%{_bindir}/errno
%{_bindir}/vidir 
%{_bindir}/vipe 
%{_bindir}/ts 
%{_bindir}/combine 
%{_bindir}/zrun 
%{_bindir}/chronic

%{_mandir}/man1/sponge.1*
%{_mandir}/man1/vidir.1*
%{_mandir}/man1/vipe.1*
%{_mandir}/man1/isutf8.1*
%{_mandir}/man1/ts.1*
%{_mandir}/man1/combine.1*
%{_mandir}/man1/ifdata.1*
%{_mandir}/man1/ifne.1* 
%{_mandir}/man1/pee.1*
%{_mandir}/man1/zrun.1* 
%{_mandir}/man1/chronic.1* 
%{_mandir}/man1/mispipe.1* 
%{_mandir}/man1/lckdo.1*
%{_mandir}/man1/parallel.1*
%{_mandir}/man1/errno.1*