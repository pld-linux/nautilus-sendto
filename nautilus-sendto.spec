Summary:	Nautilus context menu for sending files
Summary(pl):	Menu kontekstowe nautilusa do wysy³ania plików
Name:		nautilus-sendto
Version:	0.7
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/nautilus-sendto/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	c6988b7b10cf2350ed4db03c57136928
Patch0:		%{name}-gaim20.patch
Patch1:		%{name}-gajim.patch
URL:		http://www.es.gnome.org/~telemaco/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 1.7.3
BuildRequires:	gaim-devel >= 2.0
BuildRequires:	gnome-bluetooth-devel >= 0.7.0
BuildRequires:	gtk+2-devel >= 2:2.9.4
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui >= 2.15.1
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.15.2
BuildRequires:	pkgconfig
Requires:	file-roller
Requires:	nautilus >= 2.15.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nautilus-sendto provides a Nautilus context menu for sending
files via other desktop applications.

%description -l pl
nautilus-sendto dostarcza menu kontekstowe dla Nautilusa do
wysy³ania plików poprzez inne aplikacje biurkowe.

%package evolution
Summary:	nautilus-sendto Evolution plugin
Summary(pl):	Wtyczka nautilus-sendto dla Evolution
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	evolution >= 2.7.3

%description evolution
A nautilus-sendto plugin for sending files via Evolution.

%description evolution -l pl
Wtyczka nautilus-sentdo do wysy³ania plików poprzez Evolution.

%package gaim
Summary:	nautilus-sendto Gaim plugin
Summary(pl):	Wtyczka nautilus-sendto dla Gaima
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gaim >= 2.0

%description gaim
A nautilus-sendto plugin for sending files via Gaim.

%description gaim -l pl
Wtyczka nautilus-sentdo do wysy³ania plików poprzez Gaima.

%package gajim
Summary:	nautilus-sendto Gajim plugin
Summary(pl):	Wtyczka nautilus-sendto dla Gajima
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	dbus >= 0.62
Requires:	gajim >= 0.10.1

%description gajim
A nautilus-sendto plugin for sending files via Gajim.

%description gajim -l pl
Wtyczka nautilus-sentdo do wysy³ania plików poprzez Gajima.

%package gnome-bluetooth
Summary:	nautilus-sendto GNOME Bluetooth plugin
Summary(pl):	Wtyczka nautilus-sendto dla GNOME Bluetooth
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-bluetooth >= 0.7.0

%description gnome-bluetooth
A nautilus-sendto plugin for sending files via GNOME Bluetooth.

%description  gnome-bluetooth -l pl
Wtyczka nautilus-sentdo do wysy³ania plików poprzez GNOME Bluetooth.

%package sylpheed
Summary:	nautilus-sendto Sylpheed plugin
Summary(pl):	Wtyczka nautilus-sendto dla Sylpheeda
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description sylpheed
A nautilus-sendto plugin for sending files via Sylpheed.

%description sylpheed -l pl
Wtyczka nautilus-sentdo do wysy³ania plików poprzez Sylpheeda.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-gajim
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/{gaim,nautilus/extensions-1.0,nautilus-sendto/plugins}/*.la
#rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/libnautilus-sendto.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/glade

%files evolution
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstevolution.so

%files gaim
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gaim/*.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstgaim.so

%files gajim
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstgajim.so

%files gnome-bluetooth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstbluetooth.so

%files sylpheed
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/libnstsylpheed.so
