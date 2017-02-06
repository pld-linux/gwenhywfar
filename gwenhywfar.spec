#
# TODO: - define _one_, system-wide place for ca-bundle.crt and use one, up-to-date file
#
# Conditional build:
%bcond_without	fox		# FOX 1.6 GUI
%bcond_without	qt		# any Qt GUI (convenience)
%bcond_without	qt4		# Qt 4 GUI
%bcond_without	qt5		# Qt 5 GUI
%bcond_without	static_libs	# static libraries
#
%if %{without qt}
%undefine	with_qt4
%undefine	with_qt5
%endif
Summary:	Gwenhywfar - a multi-platform helper library for networking and security
Summary(pl.UTF-8):	Gwenhywfar - wieloplatformowa biblioteka pomocnicza do sieci i bezpieczeństwa
Name:		gwenhywfar
Version:	4.15.3
Release:	1
License:	LGPL v2.1+ with OpenSSL linking exception
Group:		Libraries
# https://www.aquamaniac.de/sites/download/packages.php
Source0:	https://www.aquamaniac.de/sites/download/download.php?package=01&release=201&file=01&dummy=/%{name}-%{version}.tar.gz
# Source0-md5:	4e96e68482a3cf1cfc00bd3645684c82
Patch0:		gcc.patch
Patch1:		%{name}-qt5.patch
URL:		https://www.aquamaniac.de/sites/aqbanking/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
%{?with_fox:BuildRequires:	fox16-devel >= 1.6}
BuildRequires:	gettext-tools
BuildRequires:	gnutls-devel >= 2.9.8
BuildRequires:	gtk+2-devel >= 2:2.17.5
BuildRequires:	libgcrypt-devel >= 1.2.0
BuildRequires:	libgpg-error-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
%if %{with qt4}
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	qt4-build
%endif
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
%endif
Requires:	gnutls-libs >= 2.9.8
Requires:	libgcrypt >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ver_cmake	%(echo %{version} | cut -d. -f 1-2)

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
Requires:	gnutls-devel >= 2.9.8
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

%package gui-cpp
Summary:	C++ wrapper classes for Gwenhywfar GUI functions
Summary(pl.UTF-8):	Klasy C++ obudowujące funkcje GUI biblioteki Gwenhywfar
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gui-cpp
C++ wrapper classes for Gwenhywfar GUI functions.

%description gui-cpp -l pl.UTF-8
Klasy C++ obudowujące funkcje GUI biblioteki Gwenhywfar.

%package gui-cpp-devel
Summary:	Header files for Gwenhywfar GUI C++ library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Gwenhywfar GUI C++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gui-cpp = %{version}-%{release}
Requires:	libstdc++-devel

%description gui-cpp-devel
Header files for Gwenhywfar GUI C++ library.

%description gui-cpp-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Gwenhywfar GUI C++.

%package gui-cpp-static
Summary:	Static Gwenhywfar GUI C++ library
Summary(pl.UTF-8):	Statyczna biblioteka Gwenhywfar GUI C++
Group:		Development/Libraries
Requires:	%{name}-gui-cpp-devel = %{version}-%{release}

%description gui-cpp-static
Static Gwenhywfar GUI C++ library.

%description gui-cpp-static -l pl.UTF-8
Statyczna biblioteka Gwenhywfar GUI C++.

# TODO: rename to gui-fox[16] when something changes
%package fox
Summary:	FOX 1.6 Gwenhywfar GUI library implementation of the GWEN_DIALOG framework
Summary(pl.UTF-8):	Biblioteka graficznego interfejsu FOX 1.6 do Gwenhywfar
Group:		X11/Libraries
Requires:	%{name}-gui-cpp = %{version}-%{release}

%description fox
FOX 1.6 Gwenhywfar GUI library, containing FOX implementation of the
GWEN_DIALOG framework.

%description fox
Biblioteka graficznego interfejsu FOX 1.6 do Gwenhywfar, zawierająca
implementację FOX szkieletu GWEN_DIALOG.

%package fox-devel
Summary:	Header files for FOX 1.6 Gwenhywfar GUI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki graficznego interfejsu FOX 1.6 do Gwenhywfar
Group:		X11/Development/Libraries
Requires:	%{name}-fox = %{version}-%{release}
Requires:	%{name}-gui-cpp-devel = %{version}-%{release}
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
implementację GTK+ 2 szkieletu GWEN_DIALOG.

# TODO: rename to -gui-gtk2 when something changes (e.g. when introducing gtk3 library)
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

%package gui-qt4
Summary:	Qt 4 Gwenhywfar GUI library implementation of the GWEN_DIALOG framework
Summary(pl.UTF-8):	Biblioteka graficznego interfejsu Qt 4 do Gwenhywfar
Group:		X11/Libraries
Requires:	%{name}-gui-cpp = %{version}-%{release}
Obsoletes:	gwenhywfar-qt < 4.15

%description gui-qt4
Qt 4 Gwenhywfar GUI library, containing Qt 4 implementation of the
GWEN_DIALOG framework.

%description gui-qt4
Biblioteka graficznego interfejsu Qt 4 do Gwenhywfar, zawierająca
implementację Qt 4 szkieletu GWEN_DIALOG.

%package gui-qt4-devel
Summary:	Header files for Qt 4 Gwenhywfar GUI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki graficznego interfejsu Qt 4 do Gwenhywfar
Group:		X11/Development/Libraries
Requires:	%{name}-gui-cpp-devel = %{version}-%{release}
Requires:	%{name}-gui-qt4 = %{version}-%{release}
Requires:	QtCore-devel >= 4
Requires:	QtGui-devel >= 4
Obsoletes:	gwenhywfar-qt-devel < 4.15

%description gui-qt4-devel
Header files for Qt 4 Gwenhywfar GUI library

%description gui-qt4-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki graficznego interfejsu Qt 4 do Gwenhywfar.

%package gui-qt4-static
Summary:	Static Qt 4 Gwenhywfar GUI library
Summary(pl.UTF-8):	Statyczna biblioteka graficznego interfejsu Qt 4 do Gwenhywfar
Group:		X11/Development/Libraries
Requires:	%{name}-gui-qt4-devel = %{version}-%{release}
Obsoletes:	gwenhywfar-qt-static < 4.15

%description gui-qt4-static
Static Qt 4 Gwenhywfar GUI library.

%description gui-qt4-static -l pl.UTF-8
Statyczna biblioteka graficznego interfejsu Qt 4 do Gwenhywfar.

%package gui-qt5
Summary:	Qt 5 Gwenhywfar GUI library implementation of the GWEN_DIALOG framework
Summary(pl.UTF-8):	Biblioteka graficznego interfejsu Qt 5 do Gwenhywfar
Group:		X11/Libraries
Requires:	%{name}-gui-cpp = %{version}-%{release}

%description gui-qt5
Qt 5 Gwenhywfar GUI library, containing Qt 5 implementation of the
GWEN_DIALOG framework.

%description gui-qt5
Biblioteka graficznego interfejsu Qt 5 do Gwenhywfar, zawierająca
implementację Qt 5 szkieletu GWEN_DIALOG.

%package gui-qt5-devel
Summary:	Header files for Qt 5 Gwenhywfar GUI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki graficznego interfejsu Qt 5 do Gwenhywfar
Group:		X11/Development/Libraries
Requires:	%{name}-gui-cpp-devel = %{version}-%{release}
Requires:	%{name}-gui-qt5 = %{version}-%{release}
Requires:	Qt5Core-devel >= 5
Requires:	Qt5Gui-devel >= 5
Requires:	Qt5Widgets-devel >= 5

%description gui-qt5-devel
Header files for Qt 5 Gwenhywfar GUI library

%description gui-qt5-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki graficznego interfejsu Qt 5 do Gwenhywfar.

%package gui-qt5-static
Summary:	Static Qt 5 Gwenhywfar GUI library
Summary(pl.UTF-8):	Statyczna biblioteka graficznego interfejsu Qt 5 do Gwenhywfar
Group:		X11/Development/Libraries
Requires:	%{name}-gui-qt5-devel = %{version}-%{release}

%description gui-qt5-static
Static Qt 5 Gwenhywfar GUI library.

%description gui-qt5-static -l pl.UTF-8
Statyczna biblioteka graficznego interfejsu Qt 5 do Gwenhywfar.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
# gettextize not used (custom support instead of AM_GNU_GETTEXT)
touch config.rpath
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-network-checks \
	%{?with_static_libs:--enable-static} \
	--with-guis="%{?with_fox:fox16 }gtk2%{?with_qt4: qt4}%{?with_qt5: qt5}" \
	--with-openssl-libs=%{_libdir} \
	--with-qt4-libs=%{_libdir} \
	--with-qt5-moc=%{_bindir}/moc-qt5 \
	--with-qt5-qmake=%{_bindir}/qmake-qt5 \
	--with-qt5-uic=%{_bindir}/uic-qt5

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

%post	gui-cpp -p /sbin/ldconfig
%postun	gui-cpp -p /sbin/ldconfig

%post	fox -p /sbin/ldconfig
%postun	fox -p /sbin/ldconfig

%post	gtk -p /sbin/ldconfig
%postun	gtk -p /sbin/ldconfig

%post	gui-qt4 -p /sbin/ldconfig
%postun	gui-qt4 -p /sbin/ldconfig

%post	gui-qt5 -p /sbin/ldconfig
%postun	gui-qt5 -p /sbin/ldconfig

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
%{_includedir}/gwenhywfar4/gwenhywfar
%{_aclocaldir}/gwenhywfar.m4
%{_pkgconfigdir}/gwenhywfar.pc
%{_libdir}/cmake/gwenhywfar-%{ver_cmake}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgwenhywfar.a
%endif

%files gui-cpp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgwengui-cpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgwengui-cpp.so.0

%files gui-cpp-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgwengui-cpp.so
%{_includedir}/gwenhywfar4/gwen-gui-cpp
%{_libdir}/cmake/gwengui-cpp-%{ver_cmake}

%if %{with static_libs}
%files gui-cpp-static
%defattr(644,root,root,755)
%{_libdir}/libgwengui-cpp.a
%endif

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

%if %{with static_libs}
%files fox-static
%defattr(644,root,root,755)
%{_libdir}/libgwengui-fox16.a
%endif
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

%if %{with static_libs}
%files gtk-static
%defattr(644,root,root,755)
%{_libdir}/libgwengui-gtk2.a
%endif

%if %{with qt4}
%files gui-qt4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgwengui-qt4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgwengui-qt4.so.0

%files gui-qt4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgwengui-qt4.so
%{_includedir}/gwenhywfar4/gwen-gui-qt4
%{_pkgconfigdir}/gwengui-qt4.pc
%{_libdir}/cmake/gwengui-qt4-%{ver_cmake}

%if %{with static_libs}
%files gui-qt4-static
%defattr(644,root,root,755)
%{_libdir}/libgwengui-qt4.a
%endif
%endif

%if %{with qt5}
%files gui-qt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgwengui-qt5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgwengui-qt5.so.0

%files gui-qt5-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgwengui-qt5.so
%{_includedir}/gwenhywfar4/gwen-gui-qt5
%{_pkgconfigdir}/gwengui-qt5.pc
%{_libdir}/cmake/gwengui-qt5-%{ver_cmake}

%if %{with static_libs}
%files gui-qt5-static
%defattr(644,root,root,755)
%{_libdir}/libgwengui-qt5.a
%endif
%endif
