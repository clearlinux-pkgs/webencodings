#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : webencodings
Version  : 0.5.1
Release  : 26
URL      : http://pypi.debian.net/webencodings/webencodings-0.5.1.tar.gz
Source0  : http://pypi.debian.net/webencodings/webencodings-0.5.1.tar.gz
Summary  : Character encoding aliases for legacy web content
Group    : Development/Tools
License  : BSD-3-Clause
Requires: webencodings-python = %{version}-%{release}
Requires: webencodings-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
===================
        
        This is a Python implementation of the `WHATWG Encoding standard

%package python
Summary: python components for the webencodings package.
Group: Default
Requires: webencodings-python3 = %{version}-%{release}

%description python
python components for the webencodings package.


%package python3
Summary: python3 components for the webencodings package.
Group: Default
Requires: python3-core
Provides: pypi(webencodings)

%description python3
python3 components for the webencodings package.


%prep
%setup -q -n webencodings-0.5.1
cd %{_builddir}/webencodings-0.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603407563
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
