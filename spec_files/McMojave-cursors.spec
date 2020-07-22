Name:           McMojave-cursors
Version:        2020.07.19
Release:        1%{?dist}
Summary:        This is an x-cursor theme inspired by macOS 
BuildArch:      noarch
License:        GPLv3
URL:            https://github.com/vinceliuice/McMojave-cursors
Source0:        https://github.com/vinceliuice/McMojave-cursors/archive/master.zip
BuildRequires:  inkscape
BuildRequires:  xorg-x11-apps
BuildRequires:  findutils


%description
This is an x-cursor theme inspired by macOS .

%prep
%autosetup -n %{name}-master

%build
./build.sh

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/icons/McMojave-cursors
cp -r ./dist/*  %{buildroot}%{_datadir}/icons/McMojave-cursors


%files
%license  LICENSE 
%doc README.md 
%{_datadir}/icons/McMojave-cursor*



%changelog
* Sun Jul 19 2020 yucefsourani <youssef.m.sourani@gmail.com> - 2020.07.19-1
- Initial
