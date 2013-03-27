Summary:	Nautilus context menu for sending files
Summary(pl.UTF-8):	Menu kontekstowe nautilusa do wysyłania plików
Name:		nautilus-sendto
Version:	3.8.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-sendto/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	d0d2464b5d200ec914e127640c316ecb
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Suggests:	file-roller
Obsoletes:	nautilus-sendto-apidocs
Obsoletes:	nautilus-sendto-cd-burner
Obsoletes:	nautilus-sendto-devel
Obsoletes:	nautilus-sendto-evolution
Obsoletes:	nautilus-sendto-gaim
Obsoletes:	nautilus-sendto-gajim
Obsoletes:	nautilus-sendto-icedove
Obsoletes:	nautilus-sendto-pidgin
Obsoletes:	nautilus-sendto-sylpheed
Obsoletes:	nautilus-sendto-upnp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nautilus-sendto provides a Nautilus context menu for sending files via
e-mail.

%description -l pl.UTF-8
nautilus-sendto dostarcza menu kontekstowe dla Nautilusa do wysyłania
plików poprzez pocztę elektroniczną.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/nautilus-sendto
%{_mandir}/man1/%{name}.1*
