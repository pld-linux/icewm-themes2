Summary:	Pack of themes for icewm
Summary(pl):	Zestaw tematów dla icewm
Name:		icewm-themes-pack2
Version:	1.0
Release:	2
License:	GPL (?)
Group:		Themes
Group(de):	Themen
Group(pl):	Motywy
Source0:	%{name}.tar.gz
Requires:	icewm
BuildArch:	noarch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	/usr/X11R6/lib/X11/icewm/themes

%description 
This is a set of 25 themes for icewm. Thenmes authors:
- Implants (MJ-4) - RudeSka
- Infadel - Xerithane
- IronGrey - isutt <funghi@linuxbr.com.br>
- Jake14 - Jake
- KDE2 - John Wright
- losttime - RudeSka
- MacOS8 pastiche - MarkJ <h089@mth.uea.ac.uk>
- BigTheme - John Wright
- Mozilla-M12 - <Mathias.Hasselmann@gmx.de>
- MozModern - Rick Silin <winix@crosswinds.net>
- MyHack - Niels Rasmussen <nielsemand@image.dk>
- New Psychic Abilities (MJ-3) - RudeSka
- NeXT - Lyonel Vincent <vincentl@ec-lyon.fr>
- NiceWarp - John Wright
- Notif2 - Marc D. Williams <marcdw@flash.net>
- OpenLook - <Mathias.Hasselmann@gmx.de>
- PHOENIX - Markus "maol" Ackermann <m.acki@gmx.net>
- Poke'mon theme - William Wieboldt <waw@iname.com>
- QN-X11 - Pal Palocz <palocz.pal@mail.deltav.hu>
- Red Centre - Heiko Noordhof <heiky@yahoo.com>
- redice - RudeSka
- Silence - Xerithane <xerithane@nerdfarm.org>
- Yin - MarkJ <h089@mth.uea.ac.uk>
- Slashdot - Daniel W. Lemon <dwl@wolsi.com>
- Spring - Roland Buehlmann <http://www.trash.net/~orlando/>

%description -l pl
Jest to zestaw 25 tematów do uprzyjemnienia wygl±du twojego icewm'a.
Autorzy tematów
- Implants (MJ-4) - RudeSka
- Infadel - Xerithane
- IronGrey - isutt <funghi@linuxbr.com.br>
- Jake14 - Jake
- KDE2 - John Wright
- losttime - RudeSka
- MacOS8 pastiche - MarkJ <h089@mth.uea.ac.uk>
- BigTheme - John Wright
- Mozilla-M12 - <Mathias.Hasselmann@gmx.de>
- MozModern - Rick Silin <winix@crosswinds.net>
- MyHack - Niels Rasmussen <nielsemand@image.dk>
- New Psychic Abilities (MJ-3) - RudeSka
- NeXT - Lyonel Vincent <vincentl@ec-lyon.fr>
- NiceWarp - John Wright
- Notif2 - Marc D. Williams <marcdw@flash.net>
- OpenLook - <Mathias.Hasselmann@gmx.de>
- PHOENIX - Markus "maol" Ackermann <m.acki@gmx.net>
- Poke'mon theme - William Wieboldt <waw@iname.com>
- QN-X11 - Pal Palocz <palocz.pal@mail.deltav.hu>
- Red Centre - Heiko Noordhof <heiky@yahoo.com>
- redice - RudeSka
- Silence - Xerithane <xerithane@nerdfarm.org>
- Yin - MarkJ <h089@mth.uea.ac.uk>
- Slashdot - Daniel W. Lemon <dwl@wolsi.com>
- Spring - Roland Buehlmann <http://www.trash.net/~orlando/>

%prep
%setup -q -n %{name}
%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themesdir}

cp -R * $RPM_BUILD_ROOT%{_themesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_themesdir}
%{_themesdir}/*
