Name:           bismuth
Version:        3.1.4
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
BuildRequires:  kf5-kglobalaccel-devel kdecoration-devel 

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
%{_libdir}/qt5/qml/org/kde/bismuth/core/qmldir
%{_libdir}/qt5/qml/org/kde/bismuth/core/libbismuth_core.so
%{_libdir}/qt5/plugins/kcms/kcm_bismuth.so
%{_libdir}/qt5/plugins/org.kde.kdecoration2/bismuth_kdecoration.so
%{_datadir}/config.kcfg/bismuth_config.kcfg
%{_datadir}/kconf_update/bismuth*
%{_datadir}/qlogging-categories5/bismuth.categories
%{_datadir}/kservices5/kcm_bismuth.desktop
%{_datadir}/kpackage/kcms/kcm_bismuth/*
%{_datadir}/icons/hicolor/scalable/apps/bismuth.svg
%{_datadir}/icons/hicolor/22x22/categories/bismuth*
%{_datadir}/icons/hicolor/64x64/categories/bismuth*
%{_datadir}/kwin/scripts/bismuth/*
%{_datadir}/icons/hicolor/16x16/status/bismuth*
%{_datadir}/icons/hicolor/32x32/status/bismuth*

%changelog
* Sun Oct 02 2022 Ta-Lun Yen <es at evsfy.com> - 3.1.4-1
- Update to version 3.1.4
* Wed Jul 13 2022 Ta-Lun Yen <es at evsfy.com> - 3.1.2-1
- Update to version 3.1.2
* Mon Jun 06 2022 Ta-Lun Yen <es at evsfy.com> - 3.1.1-1
- Update to version 3.1.1
* Sun Jan 30 2022 João Capucho <jcapucho7 at gmail.com> - 2.3.0-1
- Update to version 2.3.0
* Tue Dec 07 2021 João Capucho <jcapucho7 at gmail.com> - 2.2.0-1
- First bismuth package
