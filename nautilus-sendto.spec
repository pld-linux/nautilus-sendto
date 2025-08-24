Summary:	Nautilus context menu for sending files
Summary(pl.UTF-8):	Menu kontekstowe nautilusa do wysyłania plików
Name:		nautilus-sendto
Version:	3.8.6
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-sendto/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	e4ac5e7b504bbccc5697cce07e373eae
URL:		https://wiki.gnome.org/Apps/Files
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gobject-introspection-devel >= 0.6.7
BuildRequires:	meson >= 0.40.1
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.28.0
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
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/nautilus-sendto
%{_datadir}/appdata/nautilus-sendto.metainfo.xml
%{_mandir}/man1/nautilus-sendto.1*
