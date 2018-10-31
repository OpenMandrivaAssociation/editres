# We intentionally disable -Werror=format-security here.
# It's safe because we're dealing with an array of constant strings.
%define Werror_cflags %{nil}

Summary:	A dynamic resource editor for X Toolkit applications 
Name:		editres
Version:	1.0.7
Release:	2
Group:		Development/X11
License:	MIT
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xorg-macros)

%description
Editres is a dynamic resource editor for X Toolkit applications.

%prep
%autosetup -p1

%build
%configure
%make

%install
%makeinstall_std

%files
%{_bindir}/editres
%{_datadir}/X11/app-defaults/Editres
%{_datadir}/X11/app-defaults/Editres-color
%{_mandir}/man1/editres.1*

