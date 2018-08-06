%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?fedora}
%global with_python3 1
%endif

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

%package -n python2-%{sname}
Summary:        Python client and CLI tool for Ironic Inspector

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
Requires:  python2-keystoneauth1 >= 3.4.0
Requires:  python2-osc-lib >= 1.10.0
Requires:  python2-oslo-i18n >= 3.15.3
Requires:  python2-oslo-utils >= 3.33.0
Requires:  python2-requests
Requires:  python2-six

Obsoletes: python-ironic-discoverd < 1.1.0-3
Provides: python-ironic-discoverd = %{upstream_version}

%{?python_provide:%python_provide python2-%{sname}}

%description -n python2-%{sname}
%{common_desc}

This package contains Python client and command line tool for Ironic Inspector.

%if 0%{?with_python3}
%package -n python3-%{sname}
Summary:        Python client and CLI tool for Ironic Inspector

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
# This all is required to run unit tests in check phase
BuildRequires:  python3-mock
BuildRequires:  python3-osc-lib
BuildRequires:  python3-osc-lib-tests
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-requests
BuildRequires:  python3-six

Requires:  python3-pbr >= 2.0.0
Requires:  python3-keystoneauth1 >= 3.4.0
Requires:  python3-osc-lib >= 1.10.0
Requires:  python3-oslo-i18n >= 3.15.3
Requires:  python3-oslo-utils >= 3.33.0
Requires:  python3-requests
Requires:  python3-six

%{?python_provide:%python_provide python3-%{sname}}

%description -n python3-%{sname}
%{common_desc}
%endif

%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Let RPM handle the dependencies
rm -f {test-,}requirements.txt

%build
%{__python2} setup.py build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif


%check
%{__python2} -m unittest discover ironic_inspector_client.test
%if 0%{?with_python3}
%{__python3} -m unittest discover ironic_inspector_client.test
%endif

%files -n python2-%{sname}
%doc README.rst LICENSE
%{python2_sitelib}/ironic_inspector_client*
%{python2_sitelib}/python_ironic_inspector_client*egg-info

%if 0%{?with_python3}
%files -n python3-%{sname}
%doc README.rst LICENSE
%{python3_sitelib}/ironic_inspector_client*
%{python3_sitelib}/python_ironic_inspector_client*egg-info
%endif

%changelog
