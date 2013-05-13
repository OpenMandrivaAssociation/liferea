%define	name	liferea
%define	epoch	1
%define version 1.8.8
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
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libexslt)
BuildRequires:	pkgconfig(sm)
BuildRequires:	desktop-file-utils
BuildRequires:	sqlite3-devel
BuildRequires:	libsoup-devel
BuildRequires:	unique-devel
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	intltool >= 0.35.0


%description
Liferea (abbreviation of Linux Feed Reader) is a news aggregator for
RSS/RDF feeds which also supports CDF channels, Atom/Echo/PIE feeds
and OCS or OPML directories. It is a simple FeedReader clone for Unix.

%prep
%setup -q -n %name-%version
%apply_patches

# Add Planet Mandriva feed
sed -i -e 's@^\(.*http://planet\.gnome\.org.*\)$@\1\n\t\t\t\t<outline text="Planet Mandriva" htmlUrl="http://planetmandriva.zarb.org/" xmlUrl="http://planetmandriva.zarb.org/rss20.xml" />@' opml/*.opml

#autoreconf -fi

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


%changelog
* Sat Sep 01 2012 Götz Waschk <waschk@mandriva.org> 1:1.8.8-1mdv2012.0
+ Revision: 816172
- update to new version 1.8.8
- update build deps again

* Sat Jun 16 2012 Götz Waschk <waschk@mandriva.org> 1:1.8.6-1
+ Revision: 805992
- update build deps
- update to new version 1.8.6

* Sun Apr 15 2012 Götz Waschk <waschk@mandriva.org> 1:1.8.5-1
+ Revision: 791079
- update to new version 1.8.5

* Wed Mar 28 2012 Götz Waschk <waschk@mandriva.org> 1:1.8.4-1
+ Revision: 788011
- new version

* Sat Mar 24 2012 Götz Waschk <waschk@mandriva.org> 1:1.8.3-1
+ Revision: 786540
- new version

* Mon Mar 19 2012 Götz Waschk <waschk@mandriva.org> 1:1.8.2-1
+ Revision: 785492
- new version
- remove extra source tarball
- call libtool (needed for backports)

* Sun Mar 04 2012 Götz Waschk <waschk@mandriva.org> 1:1.8.1-1
+ Revision: 782067
- fix configure
- new version

* Sat Dec 10 2011 Götz Waschk <waschk@mandriva.org> 1:1.8.0-1
+ Revision: 740057
- new version

* Thu Nov 17 2011 Götz Waschk <waschk@mandriva.org> 1:1.8-0.RC2.1
+ Revision: 731250
- new prerelease

* Mon Sep 26 2011 Götz Waschk <waschk@mandriva.org> 1:1.8-0.RC1.1
+ Revision: 701347
- new version
- update build deps
- update file list
- don't apply libnotify patch for backports

* Thu Jun 23 2011 Funda Wang <fwang@mandriva.org> 1:1.6.6b-1
+ Revision: 686757
- new version 1.6.6b
- update url

* Wed Jun 22 2011 Götz Waschk <waschk@mandriva.org> 1:1.6.6-1
+ Revision: 686594
- new version
- add missing source file

* Mon Jun 20 2011 Funda Wang <fwang@mandriva.org> 1:1.6.5-4
+ Revision: 686155
- rebuild for new webkit

* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 1:1.6.5-3
+ Revision: 677119
- rebuild to add gconf2 as req
- build with libnotify 0.7

* Wed Sep 29 2010 Götz Waschk <waschk@mandriva.org> 1:1.6.5-1mdv2011.0
+ Revision: 582058
- update to new version 1.6.5

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 1:1.6.4-1mdv2011.0
+ Revision: 550272
- update to new version 1.6.4

  + Funda Wang <fwang@mandriva.org>
    - support for updates distro
    - update BR to enable old distro

* Tue Feb 23 2010 Funda Wang <fwang@mandriva.org> 1:1.6.3-1mdv2010.1
+ Revision: 509923
- new version 1.6.3

  + Frederik Himpe <fhimpe@mandriva.org>
    - Really enable networkmanager support

* Fri Jan 22 2010 Frederik Himpe <fhimpe@mandriva.org> 1:1.6.2-1mdv2010.1
+ Revision: 495075
- Update to new version 1.6.2
- Fix failing build because of different libtool by running autoreconf
- Build with networkmanager support

* Sat Nov 21 2009 Funda Wang <fwang@mandriva.org> 1:1.6.1-1mdv2010.1
+ Revision: 468072
- new version 1.6.1

* Sat Jul 25 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.6.0-1mdv2010.0
+ Revision: 399606
- Update to new version 1.6.0

* Tue Jul 21 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.6.0-0.rc7.1mdv2010.0
+ Revision: 398419
- Update to new version 1.6.0-rc7

* Tue Jun 23 2009 Funda Wang <fwang@mandriva.org> 1:1.6.0-0.rc6.1mdv2010.0
+ Revision: 388118
- New version 1.6 rc6

* Sat Jun 13 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.6.0-0.rc5.1mdv2010.0
+ Revision: 385751
- Update to new version 1.6.0-rc5

* Sat Jun 06 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.6.0-0.rc4.1mdv2010.0
+ Revision: 383199
- Update to new version 1.6.0-rc4

* Sat May 30 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.6.0-0.rc3.1mdv2010.0
+ Revision: 381194
- Update to new version 1.6.0-rc3

* Sun May 24 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.6.0-0.rc2.1mdv2010.0
+ Revision: 379142
- Update to new version 1.6.0-rc2

* Tue May 05 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.6.0-0.rc1.1mdv2010.0
+ Revision: 372234
- Update to new version 1.6.0-rc1

* Sun Mar 15 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.5.14-1mdv2009.1
+ Revision: 355400
- Update to new version 1.5.14
- Use sed hack to add Planet Mandriva feed so that it's not necessary
  to rediff a patch if the upstream feed changes

* Thu Mar 12 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.5.13-1mdv2009.1
+ Revision: 354374
- update to new version 1.5.13

* Sat Mar 07 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.5.12-1mdv2009.1
+ Revision: 351502
- update to new version 1.5.12

* Sat Feb 28 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.5.11-1mdv2009.1
+ Revision: 345848
- update to new version 1.5.11

* Tue Feb 24 2009 Emmanuel Andry <eandry@mandriva.org> 1:1.5.10-1mdv2009.1
+ Revision: 344429
- New version 1.5.10
- drop P1 (not needed anymore)

* Sat Jan 24 2009 Funda Wang <fwang@mandriva.org> 1:1.5.8-1mdv2009.1
+ Revision: 333189
- 1.5.8

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Tue Nov 11 2008 Funda Wang <fwang@mandriva.org> 1:1.5.6-1mdv2009.1
+ Revision: 302054
- 1.5.6 final

* Sun Nov 09 2008 Funda Wang <fwang@mandriva.org> 1:1.5.6-0.4144.1mdv2009.1
+ Revision: 301266
- svn snapshot 1.5.6
  only webkit is support now

* Sun Aug 03 2008 Frederik Himpe <fhimpe@mandriva.org> 1:1.5.5-3mdv2009.0
+ Revision: 261847
- Xulrunner detection and build is pretty broken, use webkit now
- Re-enable planetmandriva patch
- Remove gtkhtml2 buildrequires, we don't use it

* Wed Jul 30 2008 Funda Wang <fwang@mandriva.org> 1:1.5.5-2mdv2009.0
+ Revision: 255127
- build against xulrunner

* Thu Jul 24 2008 Funda Wang <fwang@mandriva.org> 1:1.5.5-1mdv2009.0
+ Revision: 245283
- New version 1.5.5

* Wed Jul 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.5.4-2mdv2009.0
+ Revision: 236419
- rebuilt for mozilla-firefox-2.0.0.16

* Fri Jul 04 2008 Funda Wang <fwang@mandriva.org> 1:1.5.4-1mdv2009.0
+ Revision: 231502
- BR intltool
- New version 1.5.4

* Thu Jul 03 2008 Tiago Salem <salem@mandriva.com.br> 1:1.5.3-2mdv2009.0
+ Revision: 231251
- Rebuild for firefox 2.0.0.15

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed May 14 2008 Funda Wang <fwang@mandriva.org> 1:1.5.3-1mdv2009.0
+ Revision: 207060
- add missing icons
- fix icons
- BR curl
- New version 1.5.3

* Sat Apr 19 2008 Funda Wang <fwang@mandriva.org> 1:1.4.15-1mdv2009.0
+ Revision: 195762
- New version 1.4.15

* Wed Mar 26 2008 Götz Waschk <waschk@mandriva.org> 1:1.4.14-3mdv2008.1
+ Revision: 190450
- rebuild for firefox 2.0.0.13

  + Tiago Salem <salem@mandriva.com.br>
    - Rebuild for Firefox 2.0.0.13

  + Funda Wang <fwang@mandriva.org>
    - New version 1.4.14

* Fri Mar 07 2008 Funda Wang <fwang@mandriva.org> 1:1.4.13-1mdv2008.1
+ Revision: 181296
- update to new version 1.4.13

* Sat Feb 09 2008 Funda Wang <fwang@mandriva.org> 1:1.4.12-2mdv2008.1
+ Revision: 164626
- rebuild for new FF

* Sat Feb 02 2008 Funda Wang <fwang@mandriva.org> 1:1.4.12-1mdv2008.1
+ Revision: 161321
- New version 1.4.12

* Fri Jan 18 2008 Funda Wang <fwang@mandriva.org> 1:1.4.11-1mdv2008.1
+ Revision: 154536
- update to new version 1.4.11

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Dec 21 2007 Funda Wang <fwang@mandriva.org> 1:1.4.10-1mdv2008.1
+ Revision: 136257
- New version 1.4.9
- Rediff planetmandriva patch

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Götz Waschk <waschk@mandriva.org> 1:1.4.9-2mdv2008.1
+ Revision: 117687
- rebuild for new firefox

* Sun Dec 02 2007 Funda Wang <fwang@mandriva.org> 1:1.4.9-1mdv2008.1
+ Revision: 114400
- New version 1.4.9
- Rediff planetmandriva patch

* Sun Nov 25 2007 Funda Wang <fwang@mandriva.org> 1:1.4.8-1mdv2008.1
+ Revision: 111919
- update to new version 1.4.8

* Wed Nov 14 2007 Funda Wang <fwang@mandriva.org> 1:1.4.7-1mdv2008.1
+ Revision: 108814
- update to new version 1.4.7

* Mon Nov 05 2007 Götz Waschk <waschk@mandriva.org> 1:1.4.6-2mdv2008.1
+ Revision: 106067
- rebuild for new firefox

* Fri Nov 02 2007 Funda Wang <fwang@mandriva.org> 1:1.4.6-1mdv2008.1
+ Revision: 105275
- New version 1.4.6

* Fri Oct 19 2007 Götz Waschk <waschk@mandriva.org> 1:1.4.5b-3mdv2008.1
+ Revision: 100432
- rebuild for new firefox

* Thu Oct 18 2007 Funda Wang <fwang@mandriva.org> 1:1.4.5b-2mdv2008.1
+ Revision: 99856
- Rebuild against FF 2.0.0.7

* Fri Oct 12 2007 Funda Wang <fwang@mandriva.org> 1:1.4.5b-1mdv2008.1
+ Revision: 97581
- New version 1.4.5b

* Mon Oct 01 2007 Funda Wang <fwang@mandriva.org> 1:1.4.4-1mdv2008.0
+ Revision: 94332
- New upstream version 1.4.4

* Sun Sep 23 2007 Funda Wang <fwang@mandriva.org> 1:1.4.2b-1mdv2008.0
+ Revision: 92332
- New version 1.4.2b

* Sat Sep 01 2007 Funda Wang <fwang@mandriva.org> 1:1.4.0-1mdv2008.0
+ Revision: 77397
- New version 1.4.0 final

* Sun Aug 19 2007 Funda Wang <fwang@mandriva.org> 1:1.4-0.RC3.3mdv2008.0
+ Revision: 67160
- add mor exdg category (bug#32684)

* Tue Jul 31 2007 Götz Waschk <waschk@mandriva.org> 1:1.4-0.RC3.2mdv2008.0
+ Revision: 57244
- rebuild

* Thu Jul 26 2007 Funda Wang <fwang@mandriva.org> 1:1.4-0.RC3.1mdv2008.0
+ Revision: 55748
- disable protocol patch now
- BR sqlite3 and glade2
- New unstable version 1.4 RC3

* Thu Jul 12 2007 Funda Wang <fwang@mandriva.org> 1:1.2.20-1mdv2008.0
+ Revision: 51631
- New version

* Sun Jul 08 2007 Funda Wang <fwang@mandriva.org> 1:1.2.19-1mdv2008.0
+ Revision: 49861
- New version

* Sat Jun 30 2007 Funda Wang <fwang@mandriva.org> 1:1.2.18-1mdv2008.0
+ Revision: 46116
- New version

* Tue Jun 19 2007 Funda Wang <fwang@mandriva.org> 1:1.2.17-1mdv2008.0
+ Revision: 41173
- New version

* Fri Jun 15 2007 Götz Waschk <waschk@mandriva.org> 1:1.2.16b-3mdv2008.0
+ Revision: 39893
- rebuild for new ff

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 1:1.2.16b-2mdv2008.0
+ Revision: 36184
- rebuild with correct optflags

  + Funda Wang <fwang@mandriva.org>
    - New version

* Tue Jun 05 2007 Funda Wang <fwang@mandriva.org> 1:1.2.16-1mdv2008.0
+ Revision: 35762
- New version

* Tue May 22 2007 Funda Wang <fwang@mandriva.org> 1:1.2.15-2mdv2008.0
+ Revision: 29678
- Added back patch1 for backports

* Tue May 22 2007 Funda Wang <fwang@mandriva.org> 1:1.2.15-1mdv2008.0
+ Revision: 29656
- patch1 not needed
- Shouuld be 1.2.15 instead
- New upstream version

* Wed May 09 2007 Götz Waschk <waschk@mandriva.org> 1:1.2.14-1mdv2008.0
+ Revision: 25416
- new version

* Wed May 02 2007 Götz Waschk <waschk@mandriva.org> 1:1.2.13-1mdv2008.0
+ Revision: 20422
- new version

* Wed Apr 25 2007 Götz Waschk <waschk@mandriva.org> 1:1.2.12-1mdv2008.0
+ Revision: 18143
- new version


* Thu Apr 05 2007 Götz Waschk <waschk@mandriva.org> 1.2.10c-1mdv2007.1
+ Revision: 150734
- new version
- rediff patch 2
- new version

* Mon Mar 19 2007 Götz Waschk <waschk@mandriva.org> 1:1.2.8-1mdv2007.1
+ Revision: 146400
- new version

* Tue Mar 06 2007 Götz Waschk <waschk@mandriva.org> 1:1.2.7-1mdv2007.1
+ Revision: 134089
- new version

* Tue Feb 27 2007 Götz Waschk <waschk@mandriva.org> 1:1.2.6-2mdv2007.1
+ Revision: 126290
- rebuild for new firefox

* Sat Feb 10 2007 Götz Waschk <waschk@mandriva.org> 1:1.2.6-1mdv2007.1
+ Revision: 118703
- new version

* Mon Jan 22 2007 Götz Waschk <waschk@mandriva.org> 1:1.2.4-1mdv2007.1
+ Revision: 112076
- new version

* Sun Jan 21 2007 Götz Waschk <waschk@mandriva.org> 1:1.2.3-1mdv2007.1
+ Revision: 111610
- new version

* Mon Jan 08 2007 Götz Waschk <waschk@mandriva.org> 1:1.2.0-2mdv2007.1
+ Revision: 106106
- rebuild

* Mon Dec 18 2006 Götz Waschk <waschk@mandriva.org> 1:1.2.0-1mdv2007.1
+ Revision: 98387
- new version

* Sat Dec 09 2006 Götz Waschk <waschk@mandriva.org> 1:1.2-0.RC4.1mdv2007.1
+ Revision: 94162
- new version

* Thu Dec 07 2006 Götz Waschk <waschk@mandriva.org> 1:1.2-0.RC3.2mdv2007.1
+ Revision: 92022
- take out the trash
- disable firefox detection patch on Cooker

* Sun Nov 26 2006 Götz Waschk <waschk@mandriva.org> 1:1.2-0.RC3.1mdv2007.1
+ Revision: 87343
- new version

* Tue Nov 21 2006 Götz Waschk <waschk@mandriva.org> 1:1.2-0.RC2.2mdv2007.1
+ Revision: 85846
- bot rebuild
- new version

* Sat Nov 11 2006 Götz Waschk <waschk@mandriva.org> 1:1.2-0.RC1.2mdv2007.0
+ Revision: 82973
- fix deps (bug #27117)

* Sat Nov 11 2006 Götz Waschk <waschk@mandriva.org> 1:1.2-0.RC1.1mdv2007.1
+ Revision: 81027
- new version
- fix firefox dep

* Thu Nov 09 2006 Götz Waschk <waschk@mandriva.org> 1:1.1.9-2mdv2007.1
+ Revision: 79217
- rebuild for new firefox

* Sat Nov 04 2006 Götz Waschk <waschk@mandriva.org> 1:1.1.9-1mdv2007.1
+ Revision: 76476
- new version
- drop patch 3

* Tue Oct 31 2006 Götz Waschk <waschk@mandriva.org> 1:1.1.8-1mdv2007.1
+ Revision: 74781
- new version
- patch to fix build

* Thu Oct 26 2006 Götz Waschk <waschk@mandriva.org> 1:1.1.7-5mdv2007.1
+ Revision: 72590
- add missing buildrequires

* Wed Oct 25 2006 Götz Waschk <waschk@mandriva.org> 1:1.1.7-4mdv2007.1
+ Revision: 72494
- new version 1.1.7d

* Wed Oct 25 2006 Götz Waschk <waschk@mandriva.org> 1:1.1.7-3mdv2007.1
+ Revision: 72493
- new version

* Tue Oct 24 2006 Götz Waschk <waschk@mandriva.org> 1:1.1.7-2mdv2007.0
+ Revision: 71945
- new version 1.1.7b

* Mon Oct 23 2006 Götz Waschk <waschk@mandriva.org> 1:1.1.7-1mdv2007.0
+ Revision: 71680
- fix previous commit
- new version 1.1.7b
  unpack patches
- Import liferea

* Sun Oct 22 2006 Götz Waschk <waschk@mandriva.org> 1:1.1.7-1mdv2007.1
- New version 1.1.7

* Wed Oct 04 2006 Götz Waschk <waschk@mandriva.org> 1:1.1.6-1mdv2007.0
- New version 1.1.6

* Fri Sep 29 2006 G�tz Waschk <waschk@mandriva.org> 1.1.5-1mdv2007.0
- add planetmandriva to default feeds
- patch to fix build
- New version 1.1.5

* Sat Sep 16 2006 Frederic Crozat <fcrozat@mandriva.com> 1:1.1.4-2mdv2007.0
- Rebuild with latest firefox

* Tue Sep 12 2006 G�tz Waschk <waschk@mandriva.org> 1:1.1.4-1mdv2007.0
- New version 1.1.4

* Thu Aug 31 2006 Götz Waschk <waschk@mandriva.org> 1:1.1.2-1mdv2007.0
- New release 1.1.2

* Tue Aug 22 2006 G�tz Waschk <waschk@mandriva.org> 1.1.1-1mdv2007.0
- New release 1.1.1

* Sat Aug 12 2006 G�tz Waschk <waschk@mandriva.org> 1.1.0-2mdv2007.0
- fix buildrequires

* Sat Aug 12 2006 G�tz Waschk <waschk@mandriva.org> 1.1.0-1mdv2007.0
- update file list
- rediff the patch
- New release 1.1.0

* Fri Aug 11 2006 G�tz Waschk <waschk@mandriva.org> 1.0.21-1mdv2007.0
- rediff the patch
- new version

* Wed Aug 09 2006 G�tz Waschk <waschk@mandriva.org> 1.0.20-1mdv2007.0
- depend on the exact firefox version
- drop patch 0
- New release 1.0.20

* Tue Aug 01 2006 Götz Waschk <waschk@mandriva.org> 1:1.0.19-1mdv2007.0
- New release 1.0.19

* Sun Jul 23 2006 Götz Waschk <waschk@mandriva.org> 1:1.0.18-1
- New release 1.0.18

* Thu Jul 20 2006 G�tz Waschk <waschk@mandriva.org> 1:1.0.17-1mdv2007.0
- new macros
- xdg menu
- New release 1.0.17

* Tue Jun 27 2006 Götz Waschk <waschk@mandriva.org> 1:1.0.16-1
- New release 1.0.16

* Thu Jun 15 2006 G�tz Waschk <waschk@mandriva.org> 1.0.15-1mdv2007.0
- drop patch 2
- New release 1.0.15

* Tue May 30 2006 G�tz Waschk <waschk@mandriva.org> 1.0.14-1mdv2007.0
- patch 2: fix build
- New release 1.0.14

* Thu May 18 2006 Pascal Terjan <pterjan@mandriva.org> 1:1.0.13-1mdk
- New release 1.0.13

* Mon May 08 2006 G�tz Waschk <waschk@mandriva.org> 1.0.12-1mdk
- update patch 1
- New release 1.0.12

* Fri May 05 2006 Götz Waschk <waschk@mandriva.org> 1:1.0.11-1mdk
- New release 1.0.11

* Sun Apr 23 2006 G�tz Waschk <waschk@mandriva.org> 1.0.10-1mdk
- update patch 0
- New release 1.0.10

* Wed Apr 05 2006 Götz Waschk <waschk@mandriva.org> 1.0.9-1mdk
- New release 1.0.9

* Sun Mar 19 2006 G�tz Waschk <waschk@mandriva.org> 1.0.8-1mdk
- update patch 0
- New release 1.0.8

* Mon Mar 06 2006 Tibor Pittich <Tibor.Pittich@mandriva.org> 1.0.7-1mdk
- 1.0.7

* Sat Feb 25 2006 Götz Waschk <waschk@mandriva.org> 1.0.6-1mdk
- New release 1.0.6

* Tue Feb 21 2006 Tibor Pittich <Tibor.Pittich@mandriva.org> 1.0.5-1mdk
- 1.0.5

* Mon Feb 13 2006 Götz Waschk <waschk@mandriva.org> 1.0.4-1mdk
- New release 1.0.4

* Wed Feb 01 2006 Götz Waschk <waschk@mandriva.org> 1.0.3-1mdk
- New release 1.0.3

* Wed Jan 25 2006 Tibor Pittich <Tibor.Pittich@mandriva.org> 1.0.2.1mdk
- 1.0.2

* Tue Jan 17 2006 G�tz Waschk <waschk@mandriva.org> 1.0.1-1mdk
- firefox build fix
- New release 1.0.1

* Fri Dec 23 2005 Tibor Pittich <Tibor.Pittich@mandriva.org> 1:1.0-1mdk
- 1.0
- add Epoch

* Thu Nov 24 2005 G�tz Waschk <waschk@mandriva.org> 1.0-1.RC4.2mdk
- reenable gtkhtml

* Fri Nov 18 2005 Tibor Pittich <Tibor.Pittich@mandriva.org> 1.0-1.RC4.1mdk
- 1.0 RC4
- rediff P0

* Sat Nov 05 2005 G�tz Waschk <waschk@mandriva.org> 1.0-1.RC3.1mdk
- new version

* Thu Oct 27 2005 Götz Waschk <waschk@mandriva.org> 1.0-0.RC2.3mdk
- rebuild for new dbus

* Fri Oct 14 2005 G�tz Waschk <waschk@mandriva.org> 1.0-0.RC2.2mdk
- fix buildrequires

* Wed Oct 12 2005 G�tz Waschk <waschk@mandriva.org> 1.0-0.RC2.1mdk
- fix buildrequires
- disable gtkhtml2 backend, doesn't build
- new version

* Tue Oct 04 2005 G�tz Waschk <waschk@mandriva.org> 1.0-0.RC1.1mdk
- update patch 0
- new version

* Tue Sep 27 2005 G�tz Waschk <waschk@mandriva.org> 0.9.7b-4mdk
- fix mozilla detection again

* Tue Sep 27 2005 G�tz Waschk <waschk@mandriva.org> 0.9.7b-3mdk
- fix mozilla detection

* Fri Sep 23 2005 Frederic Crozat <fcrozat@mandriva.com> 0.9.7b-2mdk
- Fix schema uninstall

* Mon Sep 05 2005 Götz Waschk <waschk@mandriva.org> 0.9.7b-1mdk
- New release 0.9.7b

* Wed Aug 31 2005 Götz Waschk <waschk@mandriva.org> 0.9.7a-1mdk
- New release 0.9.7a

* Wed Aug 31 2005 Götz Waschk <waschk@mandriva.org> 0.9.7-1mdk
- New release 0.9.7

* Wed Aug 17 2005 Götz Waschk <waschk@mandriva.org> 0.9.6-1mdk
- New release 0.9.6

* Mon Aug 01 2005 G�tz Waschk <waschk@mandriva.org> 0.9.5-1mdk
- update patches
- new version

* Wed May 18 2005 Tibor Pittich <Tibor.Pittich@mandriva.org> 0.9.2-1mdk
- 0.9.2
- use mkrel macro

* Sun Mar 13 2005 Tibor Pittich <Tibor.Pittich@mandrake.org> 0.9.1-2mdk
- update P0 to find installation mozilla-firefox as first

* Sun Mar 13 2005 Tibor Pittich <Tibor.Pittich@mandrake.org> 0.9.1-1mdk
- 0.9.1
- adjust requirements for mozilla-firefox
- quick patch for configure which allow detect mozilla-firefox

* Sun Feb 20 2005 Tibor Pittich <Tibor.Pittich@mandrake.org> 0.9.0b-2mdk
- requires glib-2.6

* Wed Jan 19 2005 Jerome Soyer <saispo@mandrake.org> 0.9.0b-1mdk
- New release 0.9.0b

* Sat Jan 15 2005 Goetz Waschk <waschk@linux-mandrake.com> 0.9.0-1mdk
- New release 0.9.0

* Tue Nov 30 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.6.4-1mdk
- 0.6.4

* Fri Nov 26 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.6.3-1mdk
- New release 0.6.3

* Sun Nov 14 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.6.2-1mdk
- fix source URL
- New release 0.6.2

* Mon Nov 01 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.6.1-2mdk
- fix mozilla detection in the startup script

* Mon Nov 01 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.6.1-1mdk
- small spec cleanup
- drop patches
- New release 0.6.1

* Sat Oct 16 2004 Jerome Soyer <saispo@mandrake.org> 0.6.0-3mdk
- Fix program icons

* Tue Sep 21 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 0.6.0-2mdk
- don't package *.la files
- install gconf schemas at install time instead build time

* Thu Sep 16 2004 Jerome Soyer <saispo@mandrake.org> 0.6.0-1mdk
- New release
- Remove patch1

* Thu Sep 02 2004 Jerome Soyer <saispo@mandrake.org> 0.5.3c-2mdk
- remove zero-length file

* Thu Sep 02 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.5.3c-1mdk
- 0.5.3c

* Wed Sep 01 2004 Jerome Soyer <saispo@mandrake.org> 0.5.3c-1mdk
- New release

* Sun Aug 22 2004 Jerome Soyer <saispo@mandrake.org> 0.5.3b-1mdk
- 0.5.3b
- fix some bugs

* Wed Aug 18 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 0.5.3-1mdk
- 0.5.3
- added default xml configs and schemas
- added P10 which fixed missing comma in array of months

* Wed Aug 04 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 0.5.2c-1mdk
- 0.5.2c
- removed P3

* Wed Jul 28 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 0.5.2-3mdk
- fixed slovak translation

* Tue Jul 27 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 0.5.2-2mdk
- added P3 to fix problem with compressed favicon

* Sat Jul 24 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 0.5.2-1mdk
- 0.5.2

* Fri Jul 02 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 0.5.1-1mdk
- 0.5.1
- drop external slovak translation, merged into project

* Mon Jun 21 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 0.5.0-1mdk
- new version
- drop P3
- added slovak translation
- package man page too

* Sun Jun 20 2004 Abel Cheung <deaddog@deaddog.org> 0.4.9-2mdk
- Rebuild with new gcc

* Tue Jun 01 2004 Abel Cheung <deaddog@deaddog.org> 0.4.9-1mdk
- New version
- Drop P0 (upstream)
- Regen P3

* Sun May 09 2004 Abel Cheung <deaddog@deaddog.org> 0.4.8-1mdk
- New version
- Regenerate P0
- Patch3: Fix bad translations

* Mon May 03 2004 Abel Cheung <deaddog@deaddog.org> 0.4.7d-1mdk
- New version
- Update patch1 to autodetect mozilla version
- Patch2: Add missing mozilla header dir to search for (ugly)

* Thu Apr 29 2004 Abel Cheung <deaddog@deaddog.org> 0.4.7c-2mdk
- Fix patch1 to set MOZILLA_FIVE_HOME correctly (thanks to
  Jorge Enrique Gomez G.  jegomez<AT>agofer<DOT>com<DOT>co)

* Fri Apr 23 2004 Abel Cheung <deaddog@deaddog.org> 0.4.7c-1mdk
- New version
- Patch0: build modules without version
- Patch1: set mozilla home correctly

