%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	Screen magnifier for KDE4
Name:		kmag
Version:	 18.08.3
Release:	1
Epoch:		2
License:	GPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/utilities/kmag/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake cmake(ECM) ninja
BuildRequires:	cmake(KF5Config) cmake(KF5ConfigWidgets) cmake(KF5CoreAddons) cmake(KF5I18n) cmake(KF5KIO) cmake(KF5WidgetsAddons) cmake(KF5XmlGui) cmake(Qt5Core) cmake(Qt5Gui) cmake(Qt5PrintSupport) cmake(Qt5Widgets) cmake(QAccessibilityClient)
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
%{_datadir}/kxmlgui5/kmag/kmagui.rc
%{_mandir}/man1/kmag.1*
%{_datadir}/metainfo/org.kde.kmag.appdata.xml

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html --with-man
