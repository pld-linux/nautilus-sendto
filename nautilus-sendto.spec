Summary:	Nautilus context menu for sending files
Summary(pl.UTF-8):	Menu kontekstowe nautilusa do wysyłania plików
Name:		nautilus-sendto
Version:	1.1.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-sendto/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	1a3a983b72cbb63170ccb989440a40c0
Patch0:		%{name}-gajim.patch
URL:		http://www.es.gnome.org/~telemaco/
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	empathy-devel >= 2.26.0
BuildRequires:	evolution-devel >= 2.22.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	gupnp-av-devel >= 0.2.1
BuildRequires:	intltool >= 0.37.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.26.0
BuildRequires:	pidgin-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	telepathy-glib-devel
Requires(post,preun):	GConf2
Requires:	nautilus >= 2.26.0
Suggests:	file-roller
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nautilus-sendto provides a Nautilus context menu for sending files via
other desktop applications.

%description -l pl.UTF-8
nautilus-sendto dostarcza menu kontekstowe dla Nautilusa do wysyłania
plików poprzez inne aplikacje biurkowe.

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

%package empathy
Summary:	nautilus-sendto Empathy plugin
Summary(pl.UTF-8):	Wtyczka nautilus-sendto dla Empathy
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	empathy >= 2.26.0

%description empathy
A nautilus-sendto plugin for sending files via Empathy.

%description empathy -l pl.UTF-8
Wtyczka nautilus-sendto do wysyłania plików poprzez Empathy.

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

%package gnome-bluetooth
Summary:	nautilus-sendto GNOME Bluetooth plugin
Summary(pl.UTF-8):	Wtyczka nautilus-sendto dla GNOME Bluetooth
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	bluez-gnome >= 0.25

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
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/{evolution/*/plugins,pidgin,nautilus/extensions-2.0,nautilus-sendto/plugins}/*.la

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
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstremovable_devices.so
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/libnautilus-sendto.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/glade
%{_sysconfdir}/gconf/schemas/nst.schemas
%{_mandir}/man1/%{name}.1*

%files cd-burner
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstburn.so

%files empathy
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstempathy.so

%files evolution
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstevolution.so
%attr(755,root,root) %{_libdir}/evolution/*/plugins/liborg-gnome-evolution-send-attachments-to.so
%{_libdir}/evolution/*/plugins/org-gnome-evolution-send-attachments-to.eplug

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

%files upnp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstupnp.so
