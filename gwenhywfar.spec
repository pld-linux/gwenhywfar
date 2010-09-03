#
# TODO: - define _one_, system-wide place for ca-bundle.crt and use one, up-to-date file
#	- unpackaged files
#
Summary:	Gwenhywfar - a multi-platform helper library for networking and security
Summary(pl.UTF-8):	Gwenhywfar - wieloplatformowa biblioteka pomocnicza do sieci i bezpieczeństwa
Name:		gwenhywfar
Version:	4.0.1
Release:	1
License:	LGPL v2.1+ with OpenSSL linking exception
Group:		Libraries
# http://www2.aquamaniac.de/sites/download/packages.php
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	513ea7b5b22edf512fa7d825ef544954
Patch0:		%{name}-qt4-includes.patch
URL:		http://gwenhywfar.sourceforge.net/
BuildRequires:	QtGui-devel
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnutls-devel >= 1.6.1
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	qt4-build
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is used by:
 - Libchipcard (http://www.libchipcard.de/),
 - OpenHBCI2 (http://www.openhbci.de/),
 - Simthetic, the simulation tool (http://simthetic.sourceforge.net/)
 - AqBanking/AqHBCI (http://www.aquamaniac.de/aqbanking/).

%description -l pl.UTF-8
To jest Gwenhywfar - wieloplatformowa biblioteka pomocnicza do
aplikacji i bibliotek związanych z siecią i bezpieczeństwem. Jest
używana przez:
 - Libchipcard (http://www.libchipcard.de/),
 - OpenHBCI2 (http://www.openhbci.de/),
 - narzędzie do symulacji Simthetic (http://simthetic.sourceforge.net/)
 - AqBanking/AqHBCI (http://www.aquamaniac.de/aqbanking/).

%package devel
Summary:	Header files for Gwenhywfar library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Gwenhywfar
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnutls-devel >= 1.6.1

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
%setup -q
%patch0 -p1

%build
# gettextize not used (custom support instead of AM_GNU_GETTEXT)
touch config.rpath
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	--with-qt4-libs=%{_libdir} \
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
%attr(755,root,root) %{_bindir}/typemaker2
%attr(755,root,root) %{_bindir}/xmlmerge
%attr(755,root,root) %{_libdir}/libgwenhywfar.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgwenhywfar.so.60
%dir %{_libdir}/gwenhywfar
%dir %{_libdir}/gwenhywfar/plugins
%dir %{_libdir}/gwenhywfar/plugins/*
%dir %{_libdir}/gwenhywfar/plugins/*/ct
%attr(755,root,root) %{_libdir}/gwenhywfar/plugins/*/ct/*.so*
%{_libdir}/gwenhywfar/plugins/*/ct/*.xml
%dir %{_libdir}/gwenhywfar/plugins/*/dbio
%attr(755,root,root) %{_libdir}/gwenhywfar/plugins/*/dbio/*.so*
%{_libdir}/gwenhywfar/plugins/*/dbio/*.xml
%dir %{_libdir}/gwenhywfar/plugins/*/configmgr
%attr(755,root,root) %{_libdir}/gwenhywfar/plugins/*/configmgr/*.so
%{_libdir}/gwenhywfar/plugins/*/configmgr/*.xml
# just ca-bundle.crt
%{_datadir}/gwenhywfar

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gwenhywfar-config
%attr(755,root,root) %{_libdir}/libgwenhywfar.so
%{_libdir}/libgwenhywfar.la
%{_includedir}/gwenhywfar4
%{_aclocaldir}/gwenhywfar.m4
%{_pkgconfigdir}/gwenhywfar.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgwenhywfar.a
