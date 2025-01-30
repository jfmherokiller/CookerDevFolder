Name:     libpam-pwdfile
Version:  1.1
Release:  1%{?dist}
Summary:  PAM module to authenticate against a password file

License:  GPLv2+
URL:      https://github.com/tiwe-de/libpam-pwdfile
Source0:  https://github.com/tiwe-de/libpam-pwdfile/archive/v%{version}/libpam-pwdfile-%{version}.tar.gz

BuildRequires:  pam-devel

%description
%{summary}

%prep
%autosetup -n %{name}-%{version}

%build
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%{_libdir}/security/pam_pwdfile.so