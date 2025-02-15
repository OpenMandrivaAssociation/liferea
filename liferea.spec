%define oversion 1.16-RC1

Summary:	A News Aggregator For RSS/RDF Feeds For GTK/GNOME
Name:		liferea
Version:	1.16~RC1
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Networking/News
URL:		https://liferea.sf.net/
Source:		https://github.com/lwindolf/liferea/releases/download/v%{oversion}/liferea-%{oversion}.tar.bz2

BuildRequires:	pkgconfig(gio-2.0) >= 2.26.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:	pkgconfig(gmodule-2.0) >= 2.0.0
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(harfbuzz-gobject)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libnotify) >= 0.7
BuildRequires:	pkgconfig(libpeas-1.0) >= 1.0.0
BuildRequires:	pkgconfig(libpeas-gtk-1.0) >= 1.0.0
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(libxml-2.0) >= 2.6.27
BuildRequires:	pkgconfig(libxslt) >= 1.1.19
BuildRequires:	pkgconfig(pango) >= 1.4.0
BuildRequires:	pkgconfig(sqlite3) >= 3.7.0
BuildRequires:	pkgconfig(webkit2gtk-4.1)
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	intltool >= 0.35.0
BuildRequires:	gettext-devel
# Without dconf, liferea can't save its settings
Requires:	dconf

%description
Liferea (abbreviation of Linux Feed Reader) is a news aggregator for
RSS/RDF feeds which also supports CDF channels, Atom/Echo/PIE feeds
and OCS or OPML directories. It is a simple FeedReader clone for Unix.

%prep
%setup -q -n %{name}-%{oversion}
%autopatch -p1

# utf-8 convert
iconv -f iso8859-1 -t utf-8 man/pl/liferea.1 > man/pl/liferea.1.conv && \
mv -f man/pl/liferea.1.conv man/pl/liferea.1

# Add Planet Mandriva feed
sed -i -e 's@^\(.*http://planet\.gnome\.org.*\)$@\1\n\t\t\t\t<outline text="Planet Mandriva" htmlUrl="http://planetmandriva.zarb.org/" xmlUrl="http://planetmandriva.zarb.org/rss20.xml" />@' opml/*.opml

%build
%configure
%make_build

%install
%make_install
install -p -D -m 644 liferea.convert %{buildroot}%{_datadir}/GConf/gsettings/liferea.convert

# icons
%__mkdir_p %{buildroot}%{_iconsdir} \
	   %{buildroot}%{_liconsdir}
#install -D -m 644 pixmaps/16x16/liferea.png %{buildroot}%{_miconsdir}/%{name}.png
#install -D -m 644 pixmaps/32x32/liferea.png %{buildroot}%{_iconsdir}/%{name}.png
#install -D -m 644 pixmaps/48x48/liferea.png %{buildroot}%{_liconsdir}/%{name}.png

desktop-file-install --vendor="" \
  --add-category="GTK;GNOME" \
  --remove-category="Feed" \
  --set-key="Version" \
  --set-value="1.0" \
 %{buildroot}/%{_datadir}/applications/net.sourceforge.liferea.desktop

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog INSTALL
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/%{name}
%{_libdir}/%{name}/girepository-1.0/Liferea-3.0.typelib
%{_libdir}/%{name}/plugins/*
%{_libdir}/%{name}/web-extension
%{_datadir}/metainfo/net.sourceforge.liferea.appdata.xml
%{_datadir}/glib-2.0/schemas/net.sf.liferea.gschema.xml
%{_datadir}/GConf/gsettings/liferea.convert
%{_datadir}/dbus-1/services/net.sourceforge.liferea.service
%{_mandir}/it/man1/liferea.1.*
%{_mandir}/man1/liferea.1.*
