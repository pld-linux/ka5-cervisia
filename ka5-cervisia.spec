#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		cervisia
Summary:	Front-end for CVS
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	1578314c039eb617e9d1415690a23c9a
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kdesu-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kinit-devel >= %{kframever}
BuildRequires:	kf5-kitemviews-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cervisia is a user friendly version control system front-end for CVS.
The aim is to support advanced usage of CVS in an easy to use
interface, featuring conflict resolution, difference and history
viewers and status for the working copy files.

%description -l pl.UTF-8
Cervisia jest przyjaznym użytkownikowi frontendem do systemu kontroli
wersji CVS. Celem jest wspieranie zaawansowanego użycia CVSa w łatwy sposób.
Możliwości Cervisi to między innymi rozwiązywanie konfliktów w kodzie,
pokazwanie różnic oraz historii projektu a także pokazywanie statusu kopii
roboczej plików.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

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
%lang(pt_BR) %{_mandir}/pt_BR/man1/cervisia.1*
%lang(sv) %{_mandir}/sv/man1/cervisia.1*
%lang(uk) %{_mandir}/uk/man1/cervisia.1*
%{_datadir}/metainfo/org.kde.cervisia.appdata.xml
