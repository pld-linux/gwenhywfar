Summary:	Gwenhywfar - a multi-platform helper library for networking and security
Summary(pl):	Gwenhywfar - wieloplatformowa biblioteka pomocnicza do sieci i bezpieczeñstwa
Name:		gwenhywfar
Version:	2.4.0
Release:	1
License:	LGPL v2.1+ with OpenSSL linking exception
Group:		Libraries
Source0:	http://dl.sourceforge.net/gwenhywfar/%{name}-%{version}.tar.gz
# Source0-md5:	a1e75c18ea7289f51f88a6fddca59193
URL:		http://gwenhywfar.sourceforge.net/
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is used by:
 - Libchipcard2 (http://www.libchipcard.de/),
 - OpenHBCI2 (http://www.openhbci.de/),
 - Simthetic, the simulation tool (http://simthetic.sourceforge.net/)
 - AqBanking/AqHBCI (http://www.aquamaniac.de/aqbanking/).

%description -l pl
To jest Gwenhywfar - wieloplatformowa biblioteka pomocnicza do
aplikacji i bibliotek zwi±zanych z sieci± i bezpieczeñstwem. Jest
u¿ywana przez:
 - Libchipcard2 (http://www.libchipcard.de/),
 - OpenHBCI2 (http://www.openhbci.de/),
 - narzêdzie do symulacji Simthetic (http://simthetic.sourceforge.net/)
 - AqBanking/AqHBCI (http://www.aquamaniac.de/aqbanking/).

%package devel
Summary:	Header files for Gwenhywfar library
Summary(pl):	Pliki nag³ówkowe biblioteki Gwenhywfar
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	openssl-devel

%description devel
Header files for Gwenhywfar library.

%description devel -l pl
Pliki nag³ówkowe biblioteki Gwenhywfar.

%package static
Summary:	Static Gwenhywfar library
Summary(pl):	Statyczna biblioteka Gwenhywfar
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Gwenhywfar library.

%description static -l pl
Statyczna biblioteka Gwenhywfar.

%prep
%setup -q

%build
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
%dir %{_libdir}/gwenhywfar/plugins/*/crypttoken
%attr(755,root,root) %{_libdir}/gwenhywfar/plugins/*/crypttoken/*.so*
%{_libdir}/gwenhywfar/plugins/*/crypttoken/*.xml
%dir %{_libdir}/gwenhywfar/plugins/*/dbio
%attr(755,root,root) %{_libdir}/gwenhywfar/plugins/*/dbio/*.so*
%{_libdir}/gwenhywfar/plugins/*/dbio/*.xml
%dir %{_libdir}/gwenhywfar/plugins/*/storage
%attr(755,root,root) %{_libdir}/gwenhywfar/plugins/*/storage/*.so*
%{_libdir}/gwenhywfar/plugins/*/storage/*.xml
%{_sysconfdir}/gwen-public-ca.crt

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gwenhywfar-config
%attr(755,root,root) %{_libdir}/libgwenhywfar.so
%{_libdir}/libgwenhywfar.la
%{_includedir}/gwenhywfar
%{_aclocaldir}/gwenhywfar.m4
%{_pkgconfigdir}/gwenhywfar.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgwenhywfar.a
