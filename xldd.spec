%define _empty_manifest_terminate_build 0

Name:		xldd
Summary:	ldd-like tool that works on all - including crosscompiled - ELF files
Version:	0.3
Release:	3
License:	GPLv3+
Group:		Development/Tools
Url:		https://github.com/OpenMandrivaSoftware/xldd
Source0:	https://github.com/OpenMandrivaSoftware/xldd/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libelf)

%description
ldd-like tool that works on all - including crosscompiled - ELF files

%prep
%autosetup -p1

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
cp xldd %{buildroot}%{_bindir}

%files
%{_bindir}/xldd
