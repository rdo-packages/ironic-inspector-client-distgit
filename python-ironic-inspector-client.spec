%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%{?dlrn: %global tarsources python-ironic-inspector-client}
%{!?dlrn: %global tarsources python_ironic_inspector_client}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order sphinx openstackdocstheme

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

License:        Apache-2.0
URL:            https://launchpad.net/python-ironic-inspector-client
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{tarsources}-%{upstream_version}.tar.gz
# Note: remove this patch once e8128a1817ada8bb01d714cf71f1bf790ae5aba9 is contained in version > 5.3.0
# https://opendev.org/openstack/python-ironic-inspector-client/commit/e8128a1817ada8bb01d714cf71f1bf790ae5aba9
# https://review.opendev.org/q/Iada5fbaab92a8971399ba056bb2734ed832405c3
%if ! %{lua:print(rpm.vercmp(rpm.expand("%{version}"), '5.3.0'));} > 0
Patch0001:      0001-Fix-bare-metal-info-order-in-unit-tests.patch
%endif
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{tarsources}-%{upstream_version}.tar.gz.asc
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
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-osc-lib-tests

Suggests:  python3-oslo-i18n >= 3.15.3

Obsoletes: python-ironic-discoverd < 1.1.0-3
Provides:  python-ironic-discoverd = %{upstream_version}

%description -n python3-%{sname}
%{common_desc}

This package contains Python client and command line tool for Ironic Inspector.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -p1 -n %{tarsources}-%{upstream_version}

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs}; do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv}

%build
%pyproject_wheel

%install
%pyproject_install


%check
%tox -e %{default_toxenv}

%files -n python3-%{sname}
%doc README.rst LICENSE
%{python3_sitelib}/ironic_inspector_client*
%{python3_sitelib}/python_ironic_inspector_client*dist-info

%changelog
# REMOVEME: error caused by commit https://opendev.org/openstack/python-ironic-inspector-client/commit/10ed6342db245766e143e91e382ed2d8d1ff0f7a
