Summary:	Distributed hash table storage
Name:		elliptics
Version:	2.26.11.0
Release:	1%{?dist}

License:	GPLv2+
URL:		http://www.ioremap.net/projects/elliptics
Source0:	http://repo.reverbrain.com/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		elliptics-2.26.11.0-gcc6.patch
Patch1:		elliptics-2.26.11.0-interpreter-fix.patch
Patch2:		elliptics-2.26.11.0-fix-man-comments.patch

BuildRequires:	blackhole-devel = 0.2.4
BuildRequires:	boost-devel
BuildRequires:	cmake
%if 0%{?rhel} < 8
BuildRequires:	msgpack-devel
%else
BuildRequires:	compat-msgpack-devel
%endif
BuildRequires:	eblob-devel >= 0.23.11
BuildRequires:	handystats-devel >= 1.10.2
BuildRequires:	libev-devel
BuildRequires:	libtool-ltdl-devel
BuildRequires:	python-devel
BuildRequires:	python-msgpack
BuildRequires:	python-virtualenv

ExclusiveArch:	x86_64

%description
Elliptics network is a fault tolerant distributed hash table
object storage.


%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}


%description devel
Elliptics network is a fault tolerant distributed hash table
object storage.

This package contains libraries, header files and developer documentation
needed for developing software which uses the cairo graphics library.

%package client
Summary:	Elliptics client library (C++/Python bindings)
Group:		Development/Libraries


%description client
Elliptics client library (C++/Python bindings)


%package client-devel
Summary:	Elliptics library C++ binding development headers and libraries
Requires:	%{name}-client%{?_isa} = %{version}-%{release}


%description client-devel
Elliptics client library (C++/Python bindings), devel files

%prep
%autosetup -p 1

%build
# this export is needed for python installation
export DESTDIR="%{buildroot}"
%{cmake} -DWITH_COCAINE=off .
%{make_build}


%install
%{make_install}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post client -p /sbin/ldconfig
%postun client -p /sbin/ldconfig

%files
%license LICENSE
%doc README
%{_bindir}/dnet_ioserv
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/dnet_ioserv.1*


%files devel
%doc README
%{_bindir}/dnet_run_servers
%{_libdir}/lib%{name}.so


%files client
%doc README
%{_bindir}/dnet_iterate
%{_bindir}/dnet_iterate_move
%{_bindir}/dnet_find
%{_bindir}/dnet_ioclient
%{_bindir}/dnet_index
%{_bindir}/dnet_notify
%{_bindir}/dnet_ids
%{_bindir}/dnet_balancer
%{_bindir}/dnet_recovery
%{_bindir}/dnet_client
%{_libdir}/libelliptics_client.so.*
%{_libdir}/libelliptics_cpp.so.*
%{python_sitelib}/elliptics_recovery/*
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}*.egg-info
%{_mandir}/man1/dnet_find.1*
%{_mandir}/man1/dnet_ioclient.1*
%{_mandir}/man1/dnet_recovery.1*


%files client-devel
%doc README
%{_includedir}/%{name}
%{_libdir}/lib%{name}_client.so
%{_libdir}/lib%{name}_cpp.so
%{_datadir}/%{name}/cmake/*


%changelog
* Thu Jan 12 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 2.26.11.0-1
- initial build
