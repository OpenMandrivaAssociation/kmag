Name:		kmag
Version: 4.9.2
Release: 1
Epoch:		2
Group:		Graphical desktop/KDE
Summary:	Screen magnifier for KDE4
URL:		http://www.kde.org/applications/utilities/kmag/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
License:	GPLv2 and GFDL
BuildRequires:	kdelibs4-devel
Requires:	kdebase4-runtime
Obsoletes:	kdeaccessibility4-core < 2:4.5.71
Obsoletes:	kdeaccessibility4 < 2:4.5.71

%description
KMag is a small utility for Linux to magnify a part of the screen. KMag is very
useful for people with visual disabilities and for those working in the fields
of image analysis, web development etc.

%files
%doc AUTHORS ChangeLog COPYING COPYING.DOC README TODO
%doc %{_kde_docdir}/HTML/en/kmag
%{_kde_bindir}/kmag
%{_kde_appsdir}/kmag
%{_kde_applicationsdir}/kmag.desktop
%{_kde_iconsdir}/hicolor/*/*/kmag*
%{_kde_iconsdir}/hicolor/*/actions/followmouse.png
%{_kde_iconsdir}/hicolor/*/actions/hidemouse.png
%{_kde_iconsdir}/hicolor/*/actions/window.png
%{_kde_mandir}/man1/kmag.1.*


%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

