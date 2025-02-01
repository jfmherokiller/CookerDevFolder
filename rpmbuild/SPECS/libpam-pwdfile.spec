Name:     libpam-pwdfile
Version:  1.0
Release:  1%{?dist}
Summary:  PAM module to authenticate against a password file

License:  GPLv2+
URL:      https://github.com/tiwe-de/libpam-pwdfile
Source0:  https://github.com/tiwe-de/libpam-pwdfile/archive/v%{version}/libpam-pwdfile-%{version}.tar.gz

BuildRequires:  pam-devel
BuildRequires:  glibc-devel
Patch: libpam-pwdfile-patch.patch
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
%{_libdir}/security/pam_pwdfile.so