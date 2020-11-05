%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Screen magnifier for KDE Plasma
Name:		kmag
Version:	20.08.3
Release:	1
License:	GPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/utilities/kmag/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kmag-18.11.80-compile.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(QAccessibilityClient)
BuildRequires:	cmake(KF5DocTools)

%description
KMag is a small utility for Linux to magnify a part of the screen. KMag is very
useful for people with visual disabilities and for those working in the fields
of image analysis, web development etc.

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING COPYING.DOC README TODO
%{_bindir}/kmag
%{_iconsdir}/hicolor/*/*/kmag*
%{_datadir}/applications/org.kde.kmag.desktop
%{_datadir}/kmag/icons/*/*/*/*
%{_mandir}/man1/kmag.1*
%{_datadir}/metainfo/org.kde.kmag.appdata.xml

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html --with-man
