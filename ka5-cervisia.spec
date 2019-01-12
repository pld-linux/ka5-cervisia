%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		cervisia
Summary:	Front-end for CVS
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	4b134c8d9c752b01a3d5e5e6b6049ad2
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kdesu-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kinit-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kparts-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cervisia is a user friendly version control system front-end for CVS.
The aim is to support advanced usage of CVS in an easy to use
interface, featuring conflict resolution, difference and history
viewers and status for the working copy files.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cervisia
%attr(755,root,root) %{_bindir}/cvsaskpass
%attr(755,root,root) %{_bindir}/cvsservice5
%attr(755,root,root) %{_libdir}/libkdeinit5_cervisia.so
%attr(755,root,root) %{_libdir}/libkdeinit5_cvsaskpass.so
%attr(755,root,root) %{_libdir}/libkdeinit5_cvsservice.so
%attr(755,root,root) %{_libdir}/qt5/plugins/cervisiapart5.so
%{_desktopdir}/org.kde.cervisia.desktop
%{_datadir}/config.kcfg/cervisiapart.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.cervisia5.cvsjob.xml
%{_datadir}/dbus-1/interfaces/org.kde.cervisia5.cvsloginjob.xml
%{_datadir}/dbus-1/interfaces/org.kde.cervisia5.cvsservice.xml
%{_datadir}/dbus-1/interfaces/org.kde.cervisia5.repository.xml
%{_iconsdir}/hicolor/16x16/actions/vcs-add-cvs-cervisia.png
%{_iconsdir}/hicolor/16x16/actions/vcs-commit-cvs-cervisia.png
%{_iconsdir}/hicolor/16x16/actions/vcs-diff-cvs-cervisia.png
%{_iconsdir}/hicolor/16x16/actions/vcs-remove-cvs-cervisia.png
%{_iconsdir}/hicolor/16x16/actions/vcs-status-cvs-cervisia.png
%{_iconsdir}/hicolor/16x16/actions/vcs-update-cvs-cervisia.png
%{_iconsdir}/hicolor/16x16/apps/cervisia.png
%{_iconsdir}/hicolor/22x22/actions/vcs-add-cvs-cervisia.png
%{_iconsdir}/hicolor/22x22/actions/vcs-commit-cvs-cervisia.png
%{_iconsdir}/hicolor/22x22/actions/vcs-diff-cvs-cervisia.png
%{_iconsdir}/hicolor/22x22/actions/vcs-remove-cvs-cervisia.png
%{_iconsdir}/hicolor/22x22/actions/vcs-status-cvs-cervisia.png
%{_iconsdir}/hicolor/22x22/actions/vcs-update-cvs-cervisia.png
%{_iconsdir}/hicolor/22x22/apps/cervisia.png
%{_iconsdir}/hicolor/32x32/actions/vcs-add-cvs-cervisia.png
%{_iconsdir}/hicolor/32x32/actions/vcs-commit-cvs-cervisia.png
%{_iconsdir}/hicolor/32x32/actions/vcs-diff-cvs-cervisia.png
%{_iconsdir}/hicolor/32x32/actions/vcs-remove-cvs-cervisia.png
%{_iconsdir}/hicolor/32x32/actions/vcs-status-cvs-cervisia.png
%{_iconsdir}/hicolor/32x32/actions/vcs-update-cvs-cervisia.png
%{_iconsdir}/hicolor/32x32/apps/cervisia.png
%{_iconsdir}/hicolor/48x48/actions/vcs-add-cvs-cervisia.png
%{_iconsdir}/hicolor/48x48/actions/vcs-commit-cvs-cervisia.png
%{_iconsdir}/hicolor/48x48/actions/vcs-diff-cvs-cervisia.png
%{_iconsdir}/hicolor/48x48/actions/vcs-remove-cvs-cervisia.png
%{_iconsdir}/hicolor/48x48/actions/vcs-status-cvs-cervisia.png
%{_iconsdir}/hicolor/48x48/actions/vcs-update-cvs-cervisia.png
%{_iconsdir}/hicolor/48x48/apps/cervisia.png
%{_iconsdir}/hicolor/scalable/actions/vcs-add-cvs-cervisia.svgz
%{_iconsdir}/hicolor/scalable/actions/vcs-commit-cvs-cervisia.svgz
%{_iconsdir}/hicolor/scalable/actions/vcs-diff-cvs-cervisia.svgz
%{_iconsdir}/hicolor/scalable/actions/vcs-remove-cvs-cervisia.svgz
%{_iconsdir}/hicolor/scalable/actions/vcs-status-cvs-cervisia.svgz
%{_iconsdir}/hicolor/scalable/actions/vcs-update-cvs-cervisia.svgz
%{_datadir}/knotifications5/cervisia.notifyrc
%{_datadir}/kservices5/org.kde.cervisiapart5.desktop
%{_datadir}/kservices5/org.kde.cvsservice5.desktop
%dir %{_datadir}/kxmlgui5/cervisia
%{_datadir}/kxmlgui5/cervisia/cervisiashellui.rc
%dir %{_datadir}/kxmlgui5/cervisiapart
%{_datadir}/kxmlgui5/cervisiapart/cervisiaui.rc
%lang(ca) %{_mandir}/ca/man1/cervisia.1*
%lang(de) %{_mandir}/de/man1/cervisia.1*
%lang(es) %{_mandir}/es/man1/cervisia.1*
%lang(it) %{_mandir}/it/man1/cervisia.1*
%{_mandir}/man1/cervisia.1*
%lang(nl) %{_mandir}/nl/man1/cervisia.1*
%lang(pt) %{_mandir}/pt/man1/cervisia.1*
%lang(sv) %{_mandir}/sv/man1/cervisia.1*
%lang(uk) %{_mandir}/uk/man1/cervisia.1*
%{_datadir}/metainfo/org.kde.cervisia.appdata.xml