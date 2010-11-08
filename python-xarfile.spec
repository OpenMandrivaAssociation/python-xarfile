%define oname pyxar
%define name python-xarfile
%define version 0.4
%define release %mkrel 5

Summary: Python bindings for XAR, the eXtensible ARchiver
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{oname}-%{version}.tar.gz
Patch0: pyxar-0.4-fix-build.patch
Url: http://code.google.com/p/xar
License: BSD
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides: pyxar
BuildRequires: libxar-devel
BuildRequires: python-devel
BuildRequires: python-pyrex
Requires: python-base

%description
Python bindings for XAR, the eXtensible ARchiver.

%prep
%setup -qn %{oname}-%{version}
%patch0 -p0

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{py_platsitedir}/*.so
%{py_platsitedir}/*egg-info
