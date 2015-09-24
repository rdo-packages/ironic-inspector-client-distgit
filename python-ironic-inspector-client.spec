%global base_name ironic-inspector-client
%global pypi_name python-%{base_name}

Name:           %{pypi_name}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Python client and CLI tool for Ironic Inspector
# TODO(divius): add Python 3 packaging once oslo.utils and openstackclient are
# packaged for Python 3 in Fedora.

License:        ASL 2.0
URL:            https://launchpad.net/%{pypi_name}
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-pbr
# This set of packages is required to run tests
BuildRequires:  python-cliff
BuildRequires:  python-mock
BuildRequires:  python-oslo-i18n
BuildRequires:  python-oslo-utils
BuildRequires:  python-openstackclient
BuildRequires:  python-requests
BuildRequires:  python-six

%description
Ironic Inspector is an auxiliary service for discovering hardware properties
for a node managed by OpenStack Ironic. Hardware introspection or hardware
properties discovery is a process of getting hardware parameters required for
scheduling from a bare metal node, given it’s power management credentials
(e.g. IPMI address, user name and password).

This package contains Python client and command line tool for Ironic Inspector.

%package -n python2-%{base_name}
Summary:        Python client and CLI tool for Ironic Inspector
%{?python_provide:%python_provide python2-%{base_name}}

Requires:  python-cliff
Requires:  python-oslo-i18n
Requires:  python-oslo-utils
Requires:  python-openstackclient
Requires:  python-requests
Requires:  python-six

# Conflict due to ironic-discoverd also providing a CLI tool
Conflicts: python-ironic-discoverd

%description -n python2-%{base_name}
Ironic Inspector is an auxiliary service for discovering hardware properties
for a node managed by OpenStack Ironic. Hardware introspection or hardware
properties discovery is a process of getting hardware parameters required for
scheduling from a bare metal node, given it’s power management credentials
(e.g. IPMI address, user name and password).

This package contains Python client and command line tool for Ironic Inspector.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Let RPM handle the dependencies
rm -f {test-,}requirements.txt

%build
%py2_build

%install
%py2_install

%check
%{__python2} -m unittest discover ironic_inspector_client.test

%files -n python2-%{base_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/ironic_inspector_client*
%{python2_sitelib}/python_ironic_inspector_client*egg-info

%changelog
* Thu Sep 24 2015 Dmitry Tantsur <divius.inside@gmail.com> - 1.2.0-1
- New upstream release 1.2.0

* Tue Jul 14 2015 Dmitry Tantsur <divius.inside@gmail.com> - 1.0.1-1
- Initial package.
