Summary:	Nautilus integration with evolution and gaim
Name:		nautilus-sendto
Version:	0.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/nautilus-sendto/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	946aea5c775308f0472bdf9d1e4048c7
Patch0:		%{name}-find-evolution-2.2.patch
URL:		http://www.es.gnome.org/~telemaco/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 1.0.0
BuildRequires:	gaim-devel >= 1.0.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 2.4.0
BuildRequires:	libbonobo-devel >= 2.6.0
BuildRequires:	libgnomeui >= 2.7.0
BuildRequires:	nautilus-devel >= 2.8.0
BuildRequires:	pkgconfig
Requires:	file-roller
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This application provide integration beetween nautilus, evolution and
gaim.

%prep
%setup -q
%patch0 -p1

%build
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/gaim/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/glade
