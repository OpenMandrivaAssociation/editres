Name:		editres
Version:	1.0.5
Release:	%mkrel 4
Summary:	A dynamic resource editor for X Toolkit applications 
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Patch0:		editres-1.0.3-fix-str-fmt.patch
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	libx11-devel >= 1.0.0
BuildRequires:	libxmu-devel >= 1.0.0
BuildRequires:	libxt-devel >= 1.0.0
BuildRequires:	libxaw-devel >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1

%description
Editres is a dynamic resource editor for X Toolkit applications.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/editres
%{_datadir}/X11/app-defaults/Editres
%{_datadir}/X11/app-defaults/Editres-color
%{_mandir}/man1/editres.1*



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-2mdv2011.0
+ Revision: 664122
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.0.5-1mdv2011.0
+ Revision: 592506
- new release

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdv2010.1
+ Revision: 522570
- rebuilt for 2010.1

* Wed Sep 23 2009 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2010.0
+ Revision: 447713
- new release

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.3-7mdv2010.0
+ Revision: 424378
- rebuild

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 1.0.3-6mdv2009.1
+ Revision: 364905
- fix str fmt

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-5mdv2009.0
+ Revision: 220718
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-4mdv2008.1
+ Revision: 149688
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Choose default Xaw from xaw.m4 unless configure explicitly told otherwise.

* Wed Sep 19 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.3-2mdv2008.0
+ Revision: 90160
- rebuild for 2008
- minor spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages extension


* Mon Feb 05 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.3-1mdv2007.0
+ Revision: 116305
- new upstream version: 1.0.3

* Sat Sep 02 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.1-6mdv2007.0
+ Revision: 59557
- rebuild to fix libXaw.so.8 dependency
- rebuild to fix cooker uploading
- rebuild against new libXaw package
- increment release
- Adding X.org 7.0 to the repository

  + Warly <warly@mandriva.com>
    - rebuild

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix description

