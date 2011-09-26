Summary:	Nautilus context menu for sending files
Summary(pl.UTF-8):	Menu kontekstowe nautilusa do wysyłania plików
Name:		nautilus-sendto
Version:	3.0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-sendto/3.0/%{name}-%{version}.tar.xz
# Source0-md5:	291b01089bdd02e46c2e47508e75e013
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	evolution-data-server-devel >= 3.0.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	gupnp-devel >= 0.13.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.28.0
Requires:	nautilus >= 3.0.0
Suggests:	file-roller
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nautilus-sendto provides a Nautilus context menu for sending files via
other desktop applications.

%description -l pl.UTF-8
nautilus-sendto dostarcza menu kontekstowe dla Nautilusa do wysyłania
plików poprzez inne aplikacje biurkowe.

%package apidocs
Summary:	nautilus-sendto API documentation
Summary(pl.UTF-8):	Dokumentacja API nautilus-sendto
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
nautilus-sendto API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API nautilus-sendto.

%package cd-burner
Summary:	nautilus-sendto CD/DVD Creator plugin
Summary(pl.UTF-8):	Wtyczka nautilus-sendto dla kreatora CD/DVD
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus-extension-brasero

%description cd-burner
A nautilus-sendto plugin for sending files to CD/DVD Creator.

%description cd-burner -l pl.UTF-8
Wtyczka nautilus-sendto do wysyłania plików do kreatora CD/DVD.

%package devel
Summary:	Header files for nautilus-sendto
Summary(pl.UTF-8):	Pliki nagłówkowe nautilus-sendto
Group:		Development/Libraries
Requires:	glib2-devel >= 1:2.28.0
Requires:	gtk+3-devel >= 3.0.0

%description devel
Header files for nautilus-sendto.

%description devel -l pl.UTF-8
Pliki nagłówkowe nautilus-sendto.

%package evolution
Summary:	nautilus-sendto Evolution plugin
Summary(pl.UTF-8):	Wtyczka nautilus-sendto dla Evolution
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Provides:	nautilus-sendto-icedove
Provides:	nautilus-sendto-sylpheed
Obsoletes:	nautilus-sendto-icedove
Obsoletes:	nautilus-sendto-sylpheed

%description evolution
A nautilus-sendto plugin for sending files via Evolution Mail. It
works with Balsa, Sylpheed and Icedove as well.

%description evolution -l pl.UTF-8
Wtyczka nautilus-sendto do wysyłania plików poprzez Evolution Mail.
Działa również z Balsą, Sylpheedem i Icedove.

%package gajim
Summary:	nautilus-sendto Gajim plugin
Summary(pl.UTF-8):	Wtyczka nautilus-sendto dla Gajima
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	dbus >= 1.0.2
Requires:	gajim >= 0.10.1

%description gajim
A nautilus-sendto plugin for sending files via Gajim.

%description gajim -l pl.UTF-8
Wtyczka nautilus-sentdo do wysyłania plików poprzez Gajima.

%package pidgin
Summary:	nautilus-sendto Pidgin plugin
Summary(pl.UTF-8):	Wtyczka nautilus-sendto dla Pidgina
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	pidgin >= 2.0
Obsoletes:	nautilus-sendto-gaim

%description pidgin
A nautilus-sendto plugin for sending files via Pidgin.

%description pidgin -l pl.UTF-8
Wtyczka nautilus-sentdo do wysyłania plików poprzez Pidgina.

%package upnp
Summary:	nautilus-sendto UPnP media server plugin
Summary(pl.UTF-8):	Wtyczka nautilus-sendto dla serwera multimediów UPnP
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gupnp-tools

%description upnp
A nautilus-sendto plugin for sending files to UPnP media server.

%description upnp -l pl.UTF-8
Wtyczka nautilus-sendto do wysyłania plików do serwera multimediów
UPnP.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/{nautilus/extensions-3.0,nautilus-sendto/plugins}/*.la

# shipped with nautilus
%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/libnautilus-sendto.so

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/nautilus-sendto
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstremovable_devices.so
%{_datadir}/GConf/gsettings/nautilus-sendto-convert
%{_datadir}/glib-2.0/schemas/org.gnome.Nautilus.Sendto.gschema.xml
%{_datadir}/nautilus-sendto
%{_mandir}/man1/%{name}.1*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/nautilus-sendto

%files cd-burner
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstburn.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/nautilus-sendto
%{_pkgconfigdir}/nautilus-sendto.pc

%files evolution
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstevolution.so

%files gajim
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstgajim.so

%files pidgin
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstpidgin.so

%files upnp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstupnp.so
