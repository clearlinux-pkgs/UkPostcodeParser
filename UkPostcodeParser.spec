#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : UkPostcodeParser
Version  : 1.1.2
Release  : 5
URL      : https://files.pythonhosted.org/packages/74/90/20124b3329b367fed7972afd1eebc942f0eba28fae6b4a6521ba1c78e4d0/UkPostcodeParser-1.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/74/90/20124b3329b367fed7972afd1eebc942f0eba28fae6b4a6521ba1c78e4d0/UkPostcodeParser-1.1.2.tar.gz
Summary  : UK Postcode parser
Group    : Development/Tools
License  : MIT
Requires: UkPostcodeParser-python3
Requires: UkPostcodeParser-python
BuildRequires : buildreq-distutils3

%description
Original code by Simon Brunning <simon@brunningonline.net>
Taken from:
http://www.brunningonline.net/simon/blog/archives/001292.html

%package python
Summary: python components for the UkPostcodeParser package.
Group: Default
Requires: UkPostcodeParser-python3
Provides: ukpostcodeparser-python

%description python
python components for the UkPostcodeParser package.


%package python3
Summary: python3 components for the UkPostcodeParser package.
Group: Default
Requires: python3-core

%description python3
python3 components for the UkPostcodeParser package.


%prep
%setup -q -n UkPostcodeParser-1.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536587558
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
