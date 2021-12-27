Name:           ns-usbloader
Version:        5.2
Release:        1%{?dist}
Summary:        Awoo Installer and GoldLeaf uploader, RCM injector, split/merge files.

License:        GPLv3
URL:            https://github.com/developersu/ns-usbloader
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        ns-usbloader.desktop
Source2:        99-NS.rules

BuildArch:      noarch

BuildRequires:  maven

Requires:       jre


%description
Awoo Installer and GoldLeaf uploader of the NSPs (and other files), RCM payload
injector, application for split/merge files.


%prep
%setup
cp %{_sourcedir}/ns-usbloader.desktop %{_builddir}/%{name}-%{version}/
cp %{_sourcedir}/99-NS.rules %{_builddir}/%{name}-%{version}/


%build
mvn -B -DskipTests clean package


%install
install -Dm 755 target/ns-usbloader-%{version}-SNAPSHOT-jar-with-dependencies.jar \
    %{buildroot}%{_datadir}/java/ns-usbloader.jar
install -Dm 644 target/classes/res/app_icon32x32.png \
    %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/ns-usbloader.png
install -Dm 644 target/classes/res/app_icon48x48.png \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/ns-usbloader.png
install -Dm 644 target/classes/res/app_icon64x64.png \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/ns-usbloader.png
install -Dm 644 target/classes/res/app_icon128x128.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/ns-usbloader.png
install -Dm 644 ns-usbloader.desktop \
    %{buildroot}%{_datadir}/applications/ns-usbloader.desktop
install -Dm 644 99-NS.rules \
    %{buildroot}%{_sysconfdir}/udev/rules.d/99-NS.rules

%files
%license LICENSE
%{_datadir}/java/ns-usbloader.jar
%{_datadir}/icons/hicolor/32x32/apps/ns-usbloader.png
%{_datadir}/icons/hicolor/48x48/apps/ns-usbloader.png
%{_datadir}/icons/hicolor/64x64/apps/ns-usbloader.png
%{_datadir}/icons/hicolor/128x128/apps/ns-usbloader.png
%{_datadir}/applications/ns-usbloader.desktop
%{_sysconfdir}/udev/rules.d/99-NS.rules

%changelog
* Mon Dec 27 2021 João Capucho <jcapucho7@gmail.com> - 5.2-1
- First ns-usbloader package
