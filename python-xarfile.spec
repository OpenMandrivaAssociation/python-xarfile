%define oname pyxar
%define name python-xarfile
%define version 0.4
%define release 6

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


%changelog
* Mon Nov 08 2010 Funda Wang <fwang@mandriva.org> 0.4-5mdv2011.0
+ Revision: 594942
- rebuild for py 2.7

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 29 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.4-2mdv2008.0
+ Revision: 32636
- force rebuild, as it failed in x86-64
- Import python-xarfile

