Summary:	A dynamic resource editor for X Toolkit applications 
Name:		editres
Version:	1.0.6
Release:	11
Group:		Development/X11
License:	MIT
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Patch0:		editres-1.0.3-fix-str-fmt.patch

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xorg-macros)

%description
Editres is a dynamic resource editor for X Toolkit applications.

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/editres
%{_datadir}/X11/app-defaults/Editres
%{_datadir}/X11/app-defaults/Editres-color
%{_mandir}/man1/editres.1*

