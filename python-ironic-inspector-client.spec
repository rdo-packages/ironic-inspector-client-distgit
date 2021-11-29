%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
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
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

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
BuildRequires:  python3-stestr

Requires:  python3-cliff >= 2.8.0
Requires:  python3-keystoneauth1 >= 3.4.0
Requires:  python3-pbr >= 2.0.0
Requires:  python3-PyYAML >= 3.13
Requires:  python3-requests >= 2.14.2

%if 0%{?fedora} || 0%{?rhel} > 7
Suggests:  python3-oslo-i18n >= 3.15.3
%endif

Obsoletes: python-ironic-discoverd < 1.1.0-3
Provides:  python-ironic-discoverd = %{upstream_version}

%{?python_provide:%python_provide python3-%{sname}}
Obsoletes: python2-%{sname} < %{version}-%{release}

%description -n python3-%{sname}
%{common_desc}

This package contains Python client and command line tool for Ironic Inspector.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
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
stestr run

%files -n python3-%{sname}
%doc README.rst LICENSE
%{python3_sitelib}/ironic_inspector_client*
%{python3_sitelib}/python_ironic_inspector_client*egg-info

%changelog
