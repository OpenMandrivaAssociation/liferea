%define	name	liferea
%define	epoch	1
%define version 1.5.13
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
Source:		http://prdownloads.sourceforge.net/liferea/%{name}-%{version}.tar.gz
Patch0:		liferea-1.4.10-planetmandriva.patch
#Patch1: 	liferea-1.5.8-fix-str-fmt.patch
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	webkitgtk-devel
BuildRequires:  imagemagick
BuildRequires:	libnotify-devel
BuildRequires:	libxslt-devel
BuildRequires:	libgnutls-devel
BuildRequires:	libsm-devel
BuildRequires:	desktop-file-utils
BuildRequires:	sqlite3-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	curl-devel
BuildRequires:	intltool >= 0.35.0

%description
Liferea (abbreviation of Linux Feed Reader) is a news aggregator for
RSS/RDF feeds which also supports CDF channels, Atom/Echo/PIE feeds
and OCS or OPML directories. It is a simple FeedReader clone for Unix.

%prep
%setup -q -n %name-%version
%patch0 -p1 -b .planetmandriva
#%patch1 -p0

%build
%configure2_5x 	--disable-schemas-install --disable-nm
%make

%install
rm -rf %{buildroot}
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

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
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%_datadir/icons/hicolor/*/apps/*
%{_datadir}/%{name}
%{_libdir}/%{name}
%exclude %{_libdir}/%{name}/*.la
%_mandir/man1/*
%lang(pl) %_mandir/pl/man1/liferea.1*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
