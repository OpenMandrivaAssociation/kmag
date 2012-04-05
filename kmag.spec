Name: kmag
Summary: KMag screen magnifier
Version: 4.8.1
Release: 1
Group: Graphical desktop/KDE
License: LGPLv2
URL: http://utils.kde.org/projects/kmag
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%{name}-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}

Obsoletes: kde4-kmag < 4.0.68
Provides: kde4-kmag = %version

%description
KMagnifier (or kmag, its unix name) is a small utility for Linux 
to magnify a part of the screen.

%files 
%_kde_bindir/kmag
%_kde_iconsdir/*/*/apps/kmag.*
%_kde_iconsdir/*/*/actions/*.png
%_kde_datadir/applications/kde4/kmag.desktop
%_kde_datadir/apps/kmag/kmagui.rc
%_kde_docdir/HTML/*/kmag
%_mandir/man1/*

%prep
%setup -q

%build
%cmake_kde4

%make

%install
%makeinstall_std -C build

