#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-xvfbwrapper
Version  : 0.2.9
Release  : 26
URL      : https://files.pythonhosted.org/packages/57/b6/4920eabda9b49630dea58745e79f9919aba6408d460afe758bf6e9b21a04/xvfbwrapper-0.2.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/57/b6/4920eabda9b49630dea58745e79f9919aba6408d460afe758bf6e9b21a04/xvfbwrapper-0.2.9.tar.gz
Summary  : run headless display inside X virtual framebuffer (Xvfb)
Group    : Development/Tools
License  : MIT
Requires: pypi-xvfbwrapper-license = %{version}-%{release}
Requires: pypi-xvfbwrapper-python = %{version}-%{release}
Requires: pypi-xvfbwrapper-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
===============
            xvfbwrapper
        ===============
        
        
        **Manage headless displays with Xvfb (X virtual framebuffer)**

%package license
Summary: license components for the pypi-xvfbwrapper package.
Group: Default

%description license
license components for the pypi-xvfbwrapper package.


%package python
Summary: python components for the pypi-xvfbwrapper package.
Group: Default
Requires: pypi-xvfbwrapper-python3 = %{version}-%{release}

%description python
python components for the pypi-xvfbwrapper package.


%package python3
Summary: python3 components for the pypi-xvfbwrapper package.
Group: Default
Requires: python3-core
Provides: pypi(xvfbwrapper)

%description python3
python3 components for the pypi-xvfbwrapper package.


%prep
%setup -q -n xvfbwrapper-0.2.9
cd %{_builddir}/xvfbwrapper-0.2.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649797447
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-xvfbwrapper
cp %{_builddir}/xvfbwrapper-0.2.9/LICENSE %{buildroot}/usr/share/package-licenses/pypi-xvfbwrapper/75517766e0e203357a38e226bce750c7723cfbd8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-xvfbwrapper/75517766e0e203357a38e226bce750c7723cfbd8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*