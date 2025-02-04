%global debug_package %{nil}

Name:     moreutils
Version:  0.69
Release:  1
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
%{_bindir}/*
%{_mandir}/man1/*.1*

# This will instal README in the correct loaction
%doc README
# And this the license
%license COPYING
