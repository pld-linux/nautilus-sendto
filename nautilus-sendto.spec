Summary:	Nautilus context menu for sending files
Summary(pl.UTF-8):	Menu kontekstowe nautilusa do wysyłania plików
Name:		nautilus-sendto
Version:	0.13.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-sendto/0.13/%{name}-%{version}.tar.bz2
# Source0-md5:	7e8a79e6e51e4bf96318aa8f9a37044b
Patch0:		%{name}-gajim.patch
URL:		http://www.es.gnome.org/~telemaco/
BuildRequires:	GConf2-devel >= 2.21.90
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	evolution-data-server-devel >= 2.21.91
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.12.8
BuildRequires:	intltool >= 0.37.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.21.91
BuildRequires:	pidgin-devel >= 2.0
BuildRequires:	pkgconfig
Requires(post,preun):	GConf2
Requires:	file-roller
Requires:	nautilus >= 2.21.91
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nautilus-sendto provides a Nautilus context menu for sending files via
other desktop applications.

%description -l pl.UTF-8
nautilus-sendto dostarcza menu kontekstowe dla Nautilusa do wysyłania
plików poprzez inne aplikacje biurkowe.

%package evolution
Summary:	nautilus-sendto Evolution plugin
Summary(pl.UTF-8):	Wtyczka nautilus-sendto dla Evolution
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	evolution >= 2.21.91

%description evolution
A nautilus-sendto plugin for sending files via Evolution.

%description evolution -l pl.UTF-8
Wtyczka nautilus-sentdo do wysyłania plików poprzez Evolution.

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

%package gnome-bluetooth
Summary:	nautilus-sendto GNOME Bluetooth plugin
Summary(pl.UTF-8):	Wtyczka nautilus-sendto dla GNOME Bluetooth
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-bluetooth >= 0.7.0

%description gnome-bluetooth
A nautilus-sendto plugin for sending files via GNOME Bluetooth.

%description  gnome-bluetooth -l pl.UTF-8
Wtyczka nautilus-sentdo do wysyłania plików poprzez GNOME Bluetooth.

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

%package sylpheed
Summary:	nautilus-sendto Sylpheed plugin
Summary(pl.UTF-8):	Wtyczka nautilus-sendto dla Sylpheeda
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description sylpheed
A nautilus-sendto plugin for sending files via Sylpheed.

%description sylpheed -l pl.UTF-8
Wtyczka nautilus-sentdo do wysyłania plików poprzez Sylpheeda.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-gajim
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/{pidgin,nautilus/extensions-2.0,nautilus-sendto/plugins}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install nst.schemas

%preun
%gconf_schema_uninstall nst.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/nautilus-sendto
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/libnautilus-sendto.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/glade
%{_sysconfdir}/gconf/schemas/nst.schemas
%{_mandir}/man1/%{name}.1*

%files evolution
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstevolution.so

%files gajim
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstgajim.so

%files gnome-bluetooth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstbluetooth.so

%files pidgin
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pidgin/nautilus.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstpidgin.so

%files sylpheed
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstsylpheed.so
