#
# TODO: - define _one_, system-wide place for ca-bundle.crt and use one, up-to-date file
#
# Conditional build:
%bcond_without	fox	# FOX 1.6 GUI
#
Summary:	Gwenhywfar - a multi-platform helper library for networking and security
Summary(pl.UTF-8):	Gwenhywfar - wieloplatformowa biblioteka pomocnicza do sieci i bezpieczeństwa
Name:		gwenhywfar
Version:	4.2.1
Release:	2
License:	LGPL v2.1+ with OpenSSL linking exception
Group:		Libraries
# http://www2.aquamaniac.de/sites/download/packages.php
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	b1673f601af5f07d591f6716d822275b
URL:		http://www.aquamaniac.de/aqbanking/
BuildRequires:	QtGui-devel >= 4
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
%{?with_fox:BuildRequires:	fox16-devel >= 1.6}
BuildRequires:	gettext-devel
BuildRequires:	gnutls-devel >= 1.6.1
BuildRequires:	gtk+2-devel >= 2:2.17.5
BuildRequires:	libgcrypt-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build
Requires:	libgcrypt >= 1.2.0
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
Requires:	libgcrypt-devel >= 1.2.0

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

%package fox
Summary:	GTK+ 2 Gwenhywfar GUI library implementation of the GWEN_DIALOG framework
Summary(pl.UTF-8):	Biblioteka graficznego interfejsu GTK+ 2 do Gwenhywfar
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description fox
GTK+ 2 Gwenhywfar GUI library, containing GTK+ 2 implementation of the
GWEN_DIALOG framework.

%description fox
Biblioteka graficznego interfejsu GTK+ 2 do Gwenhywfar, zawierająca
implementację GTK+2 szkieletu GWEN_DIALOG.

%package fox-devel
Summary:	Header files for FOX 1.6 Gwenhywfar GUI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki graficznego interfejsu FOX 1.6 do Gwenhywfar
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-fox = %{version}-%{release}
Requires:	fox16-devel >= 1.6

%description fox-devel
Header files for FOX 1.6 Gwenhywfar GUI library

%description fox-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki graficznego interfejsu FOX 1.6 do
Gwenhywfar.

%package fox-static
Summary:	Static FOX 1.6 Gwenhywfar GUI library
Summary(pl.UTF-8):	Statyczna biblioteka graficznego interfejsu FOX 1.6 do Gwenhywfar
Group:		X11/Development/Libraries
Requires:	%{name}-fox-devel = %{version}-%{release}

%description fox-static
Static FOX 1.6 Gwenhywfar GUI library.

%description fox-static -l pl.UTF-8
Statyczna biblioteka graficznego interfejsu FOX 1.6 do Gwenhywfar.

%package gtk
Summary:	GTK+ 2 Gwenhywfar GUI library implementation of the GWEN_DIALOG framework
Summary(pl.UTF-8):	Biblioteka graficznego interfejsu GTK+ 2 do Gwenhywfar
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.17.5

%description gtk
GTK+ 2 Gwenhywfar GUI library, containing GTK+ 2 implementation of the
GWEN_DIALOG framework.

%description gtk
Biblioteka graficznego interfejsu GTK+ 2 do Gwenhywfar, zawierająca
implementację GTK+2 szkieletu GWEN_DIALOG.

%package gtk-devel
Summary:	Header files for GTK+ 2 Gwenhywfar GUI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki graficznego interfejsu GTK+ 2 do Gwenhywfar
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.17.5

%description gtk-devel
Header files for GTK+ 2 Gwenhywfar GUI library

%description gtk-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki graficznego interfejsu GTK+ 2 do
Gwenhywfar.

%package gtk-static
Summary:	Static GTK+ 2 Gwenhywfar GUI library
Summary(pl.UTF-8):	Statyczna biblioteka graficznego interfejsu GTK+ 2 do Gwenhywfar
Group:		X11/Development/Libraries
Requires:	%{name}-gtk-devel = %{version}-%{release}

%description gtk-static
Static GTK+ 2 Gwenhywfar GUI library.

%description gtk-static -l pl.UTF-8
Statyczna biblioteka graficznego interfejsu GTK+ 2 do Gwenhywfar.

%package qt
Summary:	Qt 4 Gwenhywfar GUI library implementation of the GWEN_DIALOG framework
Summary(pl.UTF-8):	Biblioteka graficznego interfejsu Qt 4 do Gwenhywfar
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description qt
Qt 4 Gwenhywfar GUI library, containing Qt 4 implementation of the
GWEN_DIALOG framework.

%description qt
Biblioteka graficznego interfejsu Qt 4 do Gwenhywfar, zawierająca
implementację GTK+2 szkieletu GWEN_DIALOG.

%package qt-devel
Summary:	Header files for Qt 4 Gwenhywfar GUI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki graficznego interfejsu Qt 4 do Gwenhywfar
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt = %{version}-%{release}
Requires:	QtGui-devel >= 4

%description qt-devel
Header files for Qt 4 Gwenhywfar GUI library

%description qt-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki graficznego interfejsu Qt 4 do Gwenhywfar.

%package qt-static
Summary:	Static Qt 4 Gwenhywfar GUI library
Summary(pl.UTF-8):	Statyczna biblioteka graficznego interfejsu Qt 4 do Gwenhywfar
Group:		X11/Development/Libraries
Requires:	%{name}-qt-devel = %{version}-%{release}

%description qt-static
Static Qt 4 Gwenhywfar GUI library.

%description qt-static -l pl.UTF-8
Statyczna biblioteka graficznego interfejsu Qt 4 do Gwenhywfar.

%prep
%setup -q

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
	--with-guis="%{?with_fox:fox16 }gtk2 qt4" \
	--with-openssl-libs=%{_libdir} \
	--with-qt4-libs=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gwenhywfar/plugins/*/*/*.{la,a}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	fox -p /sbin/ldconfig
%postun	fox -p /sbin/ldconfig

%post	gtk -p /sbin/ldconfig
%postun	gtk -p /sbin/ldconfig

%post	qt -p /sbin/ldconfig
%postun	qt -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gct-tool
%attr(755,root,root) %{_bindir}/gsa
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
%dir %{_includedir}/gwenhywfar4
%{_includedir}/gwenhywfar4/gwen-gui-cpp
%{_includedir}/gwenhywfar4/gwenhywfar
%{_aclocaldir}/gwenhywfar.m4
%{_pkgconfigdir}/gwenhywfar.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgwenhywfar.a

%if %{with fox}
%files fox
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgwengui-fox16.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgwengui-fox16.so.0

%files fox-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgwengui-fox16.so
%{_includedir}/gwenhywfar4/gwen-gui-fox16
%{_pkgconfigdir}/gwengui-fox16.pc

%files fox-static
%defattr(644,root,root,755)
%{_libdir}/libgwengui-fox16.a
%endif

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgwengui-gtk2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgwengui-gtk2.so.0

%files gtk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgwengui-gtk2.so
%{_includedir}/gwenhywfar4/gwen-gui-gtk2
%{_pkgconfigdir}/gwengui-gtk2.pc

%files gtk-static
%defattr(644,root,root,755)
%{_libdir}/libgwengui-gtk2.a

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgwengui-qt4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgwengui-qt4.so.0

%files qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgwengui-qt4.so
%{_includedir}/gwenhywfar4/gwen-gui-qt4
%{_pkgconfigdir}/gwengui-qt4.pc

%files qt-static
%defattr(644,root,root,755)
%{_libdir}/libgwengui-qt4.a
