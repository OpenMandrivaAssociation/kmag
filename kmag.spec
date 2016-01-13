Summary:	Screen magnifier for KDE4
Name:		kmag
Version:	15.12.1
Release:	1
Epoch:		2
License:	GPLv2+ and GFDL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/utilities/kmag/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	qaccessibilityclient-devel
Requires:	kdebase4-runtime

%description
KMag is a small utility for Linux to magnify a part of the screen. KMag is very
useful for people with visual disabilities and for those working in the fields
of image analysis, web development etc.

%files
%doc AUTHORS ChangeLog COPYING COPYING.DOC README TODO                                                 
%doc %{_docdir}/HTML/en/kmag                                                                      
%{_bindir}/kmag                                                                                        
%{_datadir}/apps/kmag                                                                                  
%{_datadir}/applications/kde4/kmag.desktop                                                             
%{_iconsdir}/hicolor/*/*/kmag*                                                                         
%{_mandir}/man1/kmag.1.*  

#----------------------------------------------------------------------------

%prep
%setup -q

%build
export CXX=g++
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build
