%global debug_package %{nil}

Name:		xldd
Summary:	ldd-like tool that works on all - including crosscompiled - ELF files
Version:	0.1
Release:	1
License:	GPLv3+
Group:		Development/Tools
Url:		https://github.com/OpenMandrivaSoftware/xldd
Source0:	https://github.com/OpenMandrivaSoftware/xldd/archive/master.tar.gz
# Really llvm-readelf, but that's part of the lld package for now
Requires:	lld

%description
ldd-like tool that works on all - including crosscompiled - ELF files

%prep
%autosetup -p1 -n xldd-master

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
cp xldd %{buildroot}%{_bindir}

%files
%{_bindir}/xldd
