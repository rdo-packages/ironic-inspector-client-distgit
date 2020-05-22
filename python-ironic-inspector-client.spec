# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name python-ironic-inspector-client

%global sname ironic-inspector-client

%global common_desc Ironic Inspector is an auxiliary service for discovering hardware properties \
for a node managed by OpenStack Ironic. Hardware introspection or hardware \
properties discovery is a process of getting hardware parameters required for \
scheduling from a bare metal node, given it’s power management credentials \
(e.g. IPMI address, user name and password).


Name:           python-ironic-inspector-client
Version:        3.7.1
Release:        1%{?dist}
Summary:        Python client and CLI tool for Ironic Inspector

License:        ASL 2.0
URL:            https://launchpad.net/python-ironic-inspector-client
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

%description
%{common_desc}

%package -n python%{pyver}-%{sname}
Summary:        Python client and CLI tool for Ironic Inspector

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-setuptools
# This all is required to run unit tests in check phase
BuildRequires:  python%{pyver}-mock
BuildRequires:  python%{pyver}-osc-lib
BuildRequires:  python%{pyver}-osc-lib-tests
BuildRequires:  python%{pyver}-oslo-i18n
BuildRequires:  python%{pyver}-oslo-utils
BuildRequires:  python%{pyver}-requests
BuildRequires:  python%{pyver}-six

Requires:  python%{pyver}-pbr >= 2.0.0
Requires:  python%{pyver}-keystoneauth1 >= 3.4.0
Requires:  python%{pyver}-osc-lib >= 1.10.0
Requires:  python%{pyver}-oslo-i18n >= 3.15.3
Requires:  python%{pyver}-oslo-utils >= 3.33.0
Requires:  python%{pyver}-requests
Requires:  python%{pyver}-six

# Handle python2 exception
%if %{pyver} == 2
Requires:       PyYAML >= 3.10
%else
Requires:       python%{pyver}-PyYAML >= 3.10
%endif

Obsoletes: python-ironic-discoverd < 1.1.0-3
Provides: python-ironic-discoverd = %{upstream_version}

%{?python_provide:%python_provide python%{pyver}-%{sname}}
%if %{pyver} == 3
Obsoletes: python2-%{sname} < %{version}-%{release}
%endif

%description -n python%{pyver}-%{sname}
%{common_desc}

This package contains Python client and command line tool for Ironic Inspector.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Let RPM handle the dependencies
rm -f {test-,}requirements.txt

%build
%{pyver_build}

%install
%{pyver_install}


%check
%{pyver_bin} -m unittest discover ironic_inspector_client.test

%files -n python%{pyver}-%{sname}
%doc README.rst LICENSE
%{pyver_sitelib}/ironic_inspector_client*
%{pyver_sitelib}/python_ironic_inspector_client*egg-info

%changelog
* Fri May 22 2020 RDO <dev@lists.rdoproject.org> 3.7.1-1
- Update to 3.7.1

* Mon Sep 23 2019 RDO <dev@lists.rdoproject.org> 3.7.0-1
- Update to 3.7.0

