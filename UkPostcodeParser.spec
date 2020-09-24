#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : UkPostcodeParser
Version  : 1.1.2
Release  : 10
URL      : https://files.pythonhosted.org/packages/74/90/20124b3329b367fed7972afd1eebc942f0eba28fae6b4a6521ba1c78e4d0/UkPostcodeParser-1.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/74/90/20124b3329b367fed7972afd1eebc942f0eba28fae6b4a6521ba1c78e4d0/UkPostcodeParser-1.1.2.tar.gz
Summary  : UK Postcode parser
Group    : Development/Tools
License  : MIT
Requires: UkPostcodeParser-license = %{version}-%{release}
Requires: UkPostcodeParser-python = %{version}-%{release}
Requires: UkPostcodeParser-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Original code by Simon Brunning <simon@brunningonline.net>
Taken from:
http://www.brunningonline.net/simon/blog/archives/001292.html

%package license
Summary: license components for the UkPostcodeParser package.
Group: Default

%description license
license components for the UkPostcodeParser package.


%package python
Summary: python components for the UkPostcodeParser package.
Group: Default
Requires: UkPostcodeParser-python3 = %{version}-%{release}
Provides: ukpostcodeparser-python

%description python
python components for the UkPostcodeParser package.


%package python3
Summary: python3 components for the UkPostcodeParser package.
Group: Default
Requires: python3-core
Provides: pypi(ukpostcodeparser)

%description python3
python3 components for the UkPostcodeParser package.


%prep
%setup -q -n UkPostcodeParser-1.1.2
cd %{_builddir}/UkPostcodeParser-1.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583523955
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/UkPostcodeParser
cp %{_builddir}/UkPostcodeParser-1.1.2/LICENSE %{buildroot}/usr/share/package-licenses/UkPostcodeParser/2ffd06445702b72be67ead30b9500610df1a5f91
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/UkPostcodeParser/2ffd06445702b72be67ead30b9500610df1a5f91

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
