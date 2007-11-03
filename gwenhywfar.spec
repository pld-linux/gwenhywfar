%define		beta	beta
#
Summary:	Gwenhywfar - a multi-platform helper library for networking and security
Summary(pl.UTF-8):	Gwenhywfar - wieloplatformowa biblioteka pomocnicza do sieci i bezpieczeństwa
Name:		gwenhywfar
Version:	2.9.7
Release:	0.%{beta}.1
License:	LGPL v2.1+ with OpenSSL linking exception
Group:		Libraries
Source0:	http://dl.sourceforge.net/gwenhywfar/%{name}-%{version}%{beta}.tar.gz
# Source0-md5:	c0f78f063461fde7d155eec042b6fd40
Patch0:		%{name}-visibility.patch
URL:		http://gwenhywfar.sourceforge.net/
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is used by:
 - Libchipcard2 (http://www.libchipcard.de/),
 - OpenHBCI2 (http://www.openhbci.de/),
 - Simthetic, the simulation tool (http://simthetic.sourceforge.net/)
 - AqBanking/AqHBCI (http://www.aquamaniac.de/aqbanking/).

%description -l pl.UTF-8
To jest Gwenhywfar - wieloplatformowa biblioteka pomocnicza do
aplikacji i bibliotek związanych z siecią i bezpieczeństwem. Jest
używana przez:
 - Libchipcard2 (http://www.libchipcard.de/),
 - OpenHBCI2 (http://www.openhbci.de/),
 - narzędzie do symulacji Simthetic (http://simthetic.sourceforge.net/)
 - AqBanking/AqHBCI (http://www.aquamaniac.de/aqbanking/).

%package devel
Summary:	Header files for Gwenhywfar library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Gwenhywfar
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	openssl-devel

%description devel
Header files for Gwenhywfar library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Gwenhywfar.

%package static
Summary:	Static Gwenhywfar library
Summary(pl.UTF-8):	Statyczna biblioteka Gwenhywfar
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Gwenhywfar library.

%description static -l pl.UTF-8
Statyczna biblioteka Gwenhywfar.

%prep
%setup -q -n %{name}-%{version}%{beta}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	--with-openssl-libs=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gwenhywfar/plugins/*/*/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gct-tool
%attr(755,root,root) %{_bindir}/mklistdoc
%attr(755,root,root) %{_bindir}/typemaker
%attr(755,root,root) %{_bindir}/xmlmerge
%attr(755,root,root) %{_libdir}/libgwenhywfar.so.*.*.*
%dir %{_libdir}/gwenhywfar
%dir %{_libdir}/gwenhywfar/plugins
%dir %{_libdir}/gwenhywfar/plugins/*
%dir %{_libdir}/gwenhywfar/plugins/*/ct
%attr(755,root,root) %{_libdir}/gwenhywfar/plugins/*/ct/*.so*
%{_libdir}/gwenhywfar/plugins/*/ct/*.xml
%dir %{_libdir}/gwenhywfar/plugins/*/dbio
%attr(755,root,root) %{_libdir}/gwenhywfar/plugins/*/dbio/*.so*
%{_libdir}/gwenhywfar/plugins/*/dbio/*.xml
%{_datadir}/gwenhywfar/ca-bundle.crt

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gwenhywfar-config
%attr(755,root,root) %{_libdir}/libgwenhywfar.so
%{_libdir}/libgwenhywfar.la
%{_includedir}/gwenhywfar3
%{_aclocaldir}/gwenhywfar.m4
%{_pkgconfigdir}/gwenhywfar.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgwenhywfar.a
