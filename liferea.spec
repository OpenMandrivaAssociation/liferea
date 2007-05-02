%define	name	liferea
%define	epoch	1
%define version 1.2.13
%define oversion %version
%define release %mkrel 1

Summary:	A News Aggregator For RSS/RDF Feeds For GTK/GNOME
Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		%{epoch}
License:	GPL
Group:		Networking/News
URL:		http://liferea.sf.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://prdownloads.sourceforge.net/liferea/%{name}-%{version}.tar.bz2
Patch: liferea-1.1.5-prototypes.patch
Patch1:	liferea-1.1.0-firefox-detect.patch
Patch2: liferea-planetmandriva.patch
BuildRequires:	dbus-glib-devel
BuildRequires:	gtkhtml2-devel 
BuildRequires:	gtk+2-devel
BuildRequires:	gnome-vfs2-devel mozilla-firefox-devel ImageMagick
BuildRequires:	libnotify-devel
BuildRequires:	libxslt-devel
BuildRequires:	libgnutls-devel
#BuildRequires:	liblua-devel
BuildRequires:	libsm-devel
BuildRequires:	desktop-file-utils
Requires:	libmozilla-firefox = %(rpm -q --queryformat %{VERSION} mozilla-firefox)

%description
Liferea (abbreviation of Linux Feed Reader) is a news aggregator for
RSS/RDF feeds which also supports CDF channels, Atom/Echo/PIE feeds
and OCS or OPML directories. It is a simple FeedReader clone for Unix.

%prep
%setup -q -n %name-%oversion
%patch -p1 -b .prototypes
%patch2 -p1 -b .planetmandriva
%if %mdkversion <= 200700
%patch1 -p1 -b .firefox-detect
autoconf
%endif
perl -pi -e "s^/usr/lib^%_libdir^" src/liferea.in

%build
%if %mdkversion <= 1000
%define __libtoolize true
%define __cputoolize true
%endif
#gw else it does not build with ff 1.5
export CXX="g++ -DMOZILLA_INTERNAL_API"
%configure2_5x --disable-schemas-install
%make

%install
rm -rf %{buildroot}
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

# menu entry
%__mkdir_p %{buildroot}%{_menudir}
cat > %{buildroot}%{_menudir}/%{name} << _EOF_
?package(%{name}): \
 command="%{_bindir}/liferea" \
 icon="%{name}.png" \
 longtitle="News aggregator simulating FeedReader" \
 needs="x11" \
 section="Internet/News" \
 title="Liferea" \
 startup_notify="true" xdg="true"
_EOF_

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Internet-News" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

# icons
%__mkdir_p %{buildroot}%{_iconsdir} \
	   %{buildroot}%{_liconsdir}
%__install -D -m 644       pixmaps/liferea.png %{buildroot}%{_miconsdir}/%{name}.png
convert -geometry 32x32 pixmaps/liferea.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 48x48 pixmaps/liferea.png %{buildroot}%{_liconsdir}/%{name}.png

%find_lang %{name}

%post
%update_menus
%post_install_gconf_schemas %name
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas %name

%postun
%clean_menus
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(0644,root,root,0755)
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%_datadir/icons/hicolor/48x48/apps/liferea.png
%{_datadir}/%{name}
%{_libdir}/%{name}
%exclude %{_libdir}/%{name}/*.la
%_mandir/man1/*
%lang(pl) %_mandir/pl/man1/liferea.1*

%{_menudir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png


