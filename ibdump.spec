%bcond_with mlnx_libs
%if %{with mlnx_libs}
%define upstream_arg %{nil}
%else
%define upstream_arg UPSTREAM_KERNEL=yes
%endif

%if %{undefined make_build}
%global make_build %{__make} %{?_smp_mflags}
%endif

%define make_opts WITH_MSTFLINT=yes %{upstream_arg} \\\
	MSTFLINT_INCLUDE_DIR=/usr/include/mstflint  \\\
	PREFIX=%{_prefix}

Summary: Mellanox InfiniBand sniffing application
Name: ibdump 
Version: 6.0.0
Release: 1
License: BSD2+GPL2
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Source: %{name}-%{version}.tgz
ExclusiveArch: i386 i486 i586 i686 x86_64 ppc64 ppc64le aarch64
Url: https://github.com/Mellanox/ibdump

%description
InfiniBand sniffer for MellanoX Technologies LTD. ConnectX HCAs

%prep
%setup -n %{name}-%{version}

%build
%make_build %{make_opts}

%install
rm -rf $RPM_BUILD_ROOT
%{make_install} %{make_opts}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/ibdump
%{_bindir}/vpi_tcpdump

%changelog
* Wed Dec 18 2019 Itay Avraham <itayavr@mellanox.com> 6.0.0-1
- Move to Github
* Sun Mar 19 2017 Adrian Chiris <adrianc@mellanox.co.il> 5.0.0
   ConnectX-5 Support
* Mon Nov 12 2012 Oren Kladnitsky <orenk@mellanox.co.il> 1.0.6
   Ethernet capture support, vpi_tcpdump
* Thu Nov 24 2011 Oren Kladnitsky <orenk@mellanox.co.il> 1.0.6
   ConnectX-3 Support
* Mon Feb 28 2010 Oren Kladnitsky <orenk@mellanox.co.il> 1.0.3
   initial creation

