%define	name	liferea
%define	epoch	1
%define version 1.8.0
%define release %mkrel 1
Summary:	A News Aggregator For RSS/RDF Feeds For GTK/GNOME
Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		%{epoch}
License:	GPLv2+
Group:		Networking/News
URL:		http://liferea.sf.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://downloads.sourceforge.net/liferea/%{name}-%{version}.tar.gz
BuildRequires:	gtk+2-devel >= 2.18
BuildRequires:  glib2-devel >= 2.26
BuildRequires:	libGConf2-devel
BuildRequires:	webkitgtk-devel
BuildRequires:	avahi-client-devel
BuildRequires:  imagemagick
BuildRequires:	libnotify-devel
BuildRequires:	libxslt-devel
BuildRequires:	libsm-devel
BuildRequires:	desktop-file-utils
BuildRequires:	sqlite3-devel
BuildRequires:	libsoup-devel
BuildRequires:	unique-devel
BuildRequires:	libjson-glib-devel
BuildRequires:	intltool >= 0.35.0


%description
Liferea (abbreviation of Linux Feed Reader) is a news aggregator for
RSS/RDF feeds which also supports CDF channels, Atom/Echo/PIE feeds
and OCS or OPML directories. It is a simple FeedReader clone for Unix.

%prep
%setup -q -n %name-%version

# Add Planet Mandriva feed
sed -i -e 's@^\(.*http://planet\.gnome\.org.*\)$@\1\n\t\t\t\t<outline text="Planet Mandriva" htmlUrl="http://planetmandriva.zarb.org/" xmlUrl="http://planetmandriva.zarb.org/rss20.xml" />@' opml/*.opml

%build
%configure2_5x 	--disable-schemas-install
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %buildroot%{_libdir}/%{name}/*.la

desktop-file-install --vendor="" \
  --add-category="GTK;GNOME" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

# icons
%__mkdir_p %{buildroot}%{_iconsdir} \
	   %{buildroot}%{_liconsdir}
install -D -m 644 pixmaps/16x16/liferea.png %{buildroot}%{_miconsdir}/%{name}.png
install -D -m 644 pixmaps/32x32/liferea.png %{buildroot}%{_iconsdir}/%{name}.png
install -D -m 644 pixmaps/48x48/liferea.png %{buildroot}%{_liconsdir}/%{name}.png

%find_lang %{name}

%if %mdkversion < 200900
%post
%update_menus
%post_install_gconf_schemas %name
%update_icon_cache hicolor
%endif

%preun
%preun_uninstall_gconf_schemas %name

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(0644,root,root,0755)
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%defattr(-, root, root)
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%_datadir/icons/hicolor/*/apps/*
%{_datadir}/%{name}
%_mandir/man1/*
%lang(pl) %_mandir/pl/man1/liferea.1*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
