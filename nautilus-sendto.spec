Summary:	Nautilus integration with Evolution and Gaim
Summary(pl):	Integracja Nautilusa z Evolution i Gaimem
Name:		nautilus-sendto
Version:	0.4
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/nautilus-sendto/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	2b8bff75d6cda7b1648d59dde6e4e3b2
Patch0:		%{name}-find-evolution-2.2.patch
URL:		http://www.es.gnome.org/~telemaco/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 1.0.0
BuildRequires:	gaim-devel >= 1.0.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool
BuildRequires:	libbonobo-devel >= 2.6.0
BuildRequires:	libglade2-devel >= 2.4.0
BuildRequires:	libgnomeui >= 2.7.0
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.8.0
BuildRequires:	pkgconfig
Requires:	file-roller
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This application provide integration beetween Nautilus, Evolution and
Gaim.

%description -l pl
Ta aplikacja dostarcza integracjê pomiêdzy Nautilusem, Evolution i
Gaimem.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/{gaim,nautilus/extensions-1.0,nautilus-sendto/plugins}/*.la
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/gaim/*.so
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.so
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/glade
