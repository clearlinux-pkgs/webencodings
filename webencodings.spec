#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : webencodings
Version  : 0.5.1
Release  : 16
URL      : http://pypi.debian.net/webencodings/webencodings-0.5.1.tar.gz
Source0  : http://pypi.debian.net/webencodings/webencodings-0.5.1.tar.gz
Summary  : Character encoding aliases for legacy web content
Group    : Development/Tools
License  : BSD-3-Clause
Requires: webencodings-python3
Requires: webencodings-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
===================
        
        This is a Python implementation of the `WHATWG Encoding standard

%package python
Summary: python components for the webencodings package.
Group: Default
Requires: webencodings-python3

%description python
python components for the webencodings package.


%package python3
Summary: python3 components for the webencodings package.
Group: Default
Requires: python3-core

%description python3
python3 components for the webencodings package.


%prep
%setup -q -n webencodings-0.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530748024
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
