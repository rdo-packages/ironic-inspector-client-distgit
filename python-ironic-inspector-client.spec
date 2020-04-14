%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name python-ironic-inspector-client

%global sname ironic-inspector-client

%global common_desc Ironic Inspector is an auxiliary service for discovering hardware properties \
for a node managed by OpenStack Ironic. Hardware introspection or hardware \
properties discovery is a process of getting hardware parameters required for \
scheduling from a bare metal node, given it’s power management credentials \
(e.g. IPMI address, user name and password).


Name:           python-ironic-inspector-client
Version:        XXX
Release:        XXX
Summary:        Python client and CLI tool for Ironic Inspector

License:        ASL 2.0
URL:            https://launchpad.net/python-ironic-inspector-client
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

%description
%{common_desc}

%package -n python3-%{sname}
Summary:        Python client and CLI tool for Ironic Inspector

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
# This all is required to run unit tests in check phase
BuildRequires:  python3-mock
BuildRequires:  python3-osc-lib-tests
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-requests

Requires:  python3-pbr >= 2.0.0
Requires:  python3-cliff >= 2.8.0
Requires:  python3-keystoneauth1 >= 3.4.0
Requires:  python3-requests

Requires:  python3-PyYAML >= 3.10
Suggests:  python3-oslo-i18n >= 3.15.3

Obsoletes: python-ironic-discoverd < 1.1.0-3
Provides:  python-ironic-discoverd = %{upstream_version}

%{?python_provide:%python_provide python3-%{sname}}
Obsoletes: python2-%{sname} < %{version}-%{release}

%description -n python3-%{sname}
%{common_desc}

This package contains Python client and command line tool for Ironic Inspector.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Let RPM handle the dependencies
rm -f {test-,}requirements.txt

%build
%{py3_build}

%install
%{py3_install}


%check
%{__python3} -m unittest discover ironic_inspector_client.test

%files -n python3-%{sname}
%doc README.rst LICENSE
%{python3_sitelib}/ironic_inspector_client*
%{python3_sitelib}/python_ironic_inspector_client*egg-info

%changelog
