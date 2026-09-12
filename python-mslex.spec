Name:		python-mslex
Version:	1.3.0
Release:	1
Summary:	shlex-style command line splitting for Windows
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/smoofra/mslex
Source0:	https://files.pythonhosted.org/packages/source/m/mslex/mslex-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

%description
mslex implements Windows command-line splitting and quoting. oslex
imports it even on POSIX.

%install -a
if [ -f %{buildroot}%{_bindir}/mslex-split ]; then
	sed -i '1s|^#!/usr/bin/env python3|#!/usr/bin/python|' \
		%{buildroot}%{_bindir}/mslex-split
	sed -i '1s|^#!/usr/bin/python3|#!/usr/bin/python|' \
		%{buildroot}%{_bindir}/mslex-split
fi

%files
%doc README.rst
%license LICENSE
%{_bindir}/mslex-split
%{py_sitedir}/mslex
%{py_sitedir}/mslex-*.*-info
