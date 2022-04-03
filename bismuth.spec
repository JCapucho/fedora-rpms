Name:           bismuth
Version:        3.0.0
Release:        1%{?dist}
Summary:        KDE Plasma extension that lets you tile your windows automatically

License:        MIT
URL:            https://bismuth-forge.github.io/bismuth
Source0:        https://github.com/Bismuth-Forge/bismuth/archive/refs/tags/v%{version}.tar.gz
Patch0:         empty.patch

BuildRequires:  cmake ninja-build extra-cmake-modules npm
BuildRequires:  kf5-kconfigwidgets-devel qt5-qtbase-devel qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel qt5-qtsvg-devel 
BuildRequires:  qt5-qtfeedback-devel kf5-kcmutils-devel kf5-ki18n-devel kf5-kdeclarative-devel
BuildRequires:	kdecoration-devel kf5-kglobalaccel-devel

%description
KDE Plasma extension, that lets you tile your windows automatically and manage
them via keyboard, just like in classical tiling window managers

%prep
%autosetup

%build
%cmake -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo -DUSE_TSC=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSES/MIT.txt
%{_prefix}/lib/debug%{_libdir}/qt5/plugins/org.kde.kdecoration2/bismuth_kdecoration.so-%{version}-%{release}.fc35.x86_64.debug
%{_prefix}/lib/debug%{_libdir}/qt5/qml/org/kde/bismuth/core/libbismuth_core.so-%{version}-%{release}.fc35.x86_64.debug
%{_libdir}/qt5/plugins/kcms/kcm_bismuth.so
%{_libdir}/qt5/plugins/org.kde.kdecoration2/bismuth_kdecoration.so
%{_libdir}/qt5/qml/org/kde/bismuth/core/libbismuth_core.so
%{_libdir}/qt5/qml/org/kde/bismuth/core/qmldir
%{_datadir}/config.kcfg/bismuth_config.kcfg
%{_datadir}/icons/hicolor/32x32/status/bismuth*
%{_datadir}/icons/hicolor/22x22/categories/bismuth-kcm.svg
%{_datadir}/icons/hicolor/64x64/categories/bismuth-kcm.svg
%{_datadir}/icons/hicolor/scalable/apps/bismuth.svg
%{_datadir}/kconf_update/bismuth_new_logger.upd
%{_datadir}/kconf_update/bismuth_old_conf_ui.sh
%{_datadir}/kconf_update/bismuth_old_conf_ui.upd
%{_datadir}/kconf_update/bismuth_shortcuts_category.upd
%{_datadir}/qlogging-categories5/bismuth.categories
%{_datadir}/kpackage/kcms/kcm_bismuth
%{_datadir}/kservices5/kcm_bismuth.desktop
%{_datadir}/kwin/scripts/bismuth

%changelog
* Sun Apr 03 2022 Martín Cigorraga <tincho at tutamail.com> - 3.0.0-1
- Update to version 3.0.0
* Sun Jan 30 2022 João Capucho <jcapucho7 at gmail.com> - 2.3.0-1
- Update to version 2.3.0
* Tue Dec 07 2021 João Capucho <jcapucho7 at gmail.com> - 2.2.0-1
- First bismuth package
