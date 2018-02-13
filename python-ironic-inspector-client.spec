%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name python-ironic-inspector-client

Name:           python-ironic-inspector-client
Version:        3.1.0
Release:        1%{?dist}
Summary:        Python client and CLI tool for Ironic Inspector

License:        ASL 2.0
URL:            https://launchpad.net/python-ironic-inspector-client
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools
# This all is required to run unit tests in check phase
BuildRequires:  python2-mock
BuildRequires:  python2-osc-lib
BuildRequires:  python2-osc-lib-tests
BuildRequires:  python2-oslo-i18n
BuildRequires:  python2-oslo-utils
BuildRequires:  python2-requests
BuildRequires:  python2-six

Requires:  python2-pbr >= 2.0.0
Requires:  python2-keystoneauth1 >= 3.3.0
Requires:  python2-osc-lib >= 1.8.0
Requires:  python2-oslo-i18n >= 3.15.3
Requires:  python2-oslo-utils >= 3.33.0
Requires:  python2-requests
Requires:  python2-six

Obsoletes: python-ironic-discoverd < 1.1.0-3
Provides: python-ironic-discoverd = %{upstream_version}

%description
Ironic Inspector is an auxiliary service for discovering hardware properties
for a node managed by OpenStack Ironic. Hardware introspection or hardware
properties discovery is a process of getting hardware parameters required for
scheduling from a bare metal node, given it’s power management credentials
(e.g. IPMI address, user name and password).

This package contains Python client and command line tool for Ironic Inspector.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Let RPM handle the dependencies
rm -f {test-,}requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
%{__python2} -m unittest discover ironic_inspector_client.test

%files
%doc README.rst LICENSE
%{python2_sitelib}/ironic_inspector_client*
%{python2_sitelib}/python_ironic_inspector_client*egg-info

%changelog
* Tue Feb 13 2018 RDO <dev@lists.rdoproject.org> 3.1.0-1
- Update to 3.1.0

