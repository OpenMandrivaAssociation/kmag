Name:		kmag
Version:	4.10.5
Release:	1
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

%changelog
* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.0-1
- New version 4.9.0

* Fri Jul 20 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.97-1
- New version 4.8.97

* Fri Jul 06 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.1-69.1mib2010.2
- New version 4.8.1
- Add Obsoletes for kdeaccessibility4-core and kdeaccessibility4
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.0-69.1mib2010.2
+ Revision: 198333
- Backport from Mageia to Mandriva 2010.2 for MIB users
- Merge handbook back into main package
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 mikala <mikala> 2:4.8.0-1.mga2
+ Revision: 198333
- Updating tarball to KDE 4.8.0

* Thu Jan 05 2012 mikala <mikala> 2:4.7.97-1.mga2
+ Revision: 191007
- Update tarball to kde 4.7.97

* Fri Dec 23 2011 mikala <mikala> 2:4.7.95-1.mga2
+ Revision: 186260
- Update tarball to kde 4.7.95
- fix group

* Wed Dec 14 2011 mikala <mikala> 2:4.7.90-1.mga2
+ Revision: 181445
- imported package kmag

