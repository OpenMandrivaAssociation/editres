Name:		editres
Version:	1.0.5
Release:	%mkrel 2
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

