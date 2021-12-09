Name:           wallpaper-engine-kde-plugin
Version:        0.4.3
Release:        1%{?dist}
Summary:        A kde wallpaper plugin integrating wallpaper engine 

License:        GPLv2
URL:            https://github.com/catsout/wallpaper-engine-kde-plugin
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  git cmake extra-cmake-modules
Requires:  gstreamer1-libav kf5-kpackage-devel kf5-plasma-devel lz4-devel
Requires:  mpv-libs-devel python3-websockets qt5-qtx11extras-devel
Requires:  qt5-qtbase-devel qt5-qtbase-private-devel qt5-qtdeclarative-devel 
Requires:  qt5-qtwebchannel-devel qt5-qtwebsockets-devel

%description
A wallpaper plugin integrating wallpaper engine into kde wallpaper setting


%prep
%autosetup


%build
%cmake -DUSE_PLASMAPKG=OFF
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%{_libdir}/qt5/qml/com/github/catsout/wallpaperEngineKde/libWallpaperEngineKde.so
%{_libdir}/qt5/qml/com/github/catsout/wallpaperEngineKde/qmldir
%{_datadir}/kservices5/plasma-wallpaper-com.github.casout.wallpaperEngineKde.desktop
%{_datadir}/plasma/wallpapers/com.github.casout.wallpaperEngineKde


%changelog
* Thu Dec 09 2021 João Capucho <jcapucho7@gmail.com> - 0.4.3-1
- First wallpaper-engine-kde-plugin package
