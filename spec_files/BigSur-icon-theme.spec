Name:           BigSur-icon-theme
Version:        2020.09.07
Release:        1%{?dist}
Summary:        BigSur like icon theme 
BuildArch:      noarch
License:        GPLv3
URL:            https://github.com/yeyushengfan258/BigSur-icon-theme
Source0:        https://github.com/yeyushengfan258/BigSur-icon-theme/archive/master.zip
BuildRequires:  gtk-update-icon-cache


%description
BigSur like icon theme  for all linux desktops.

%prep
%autosetup -n %{name}-master

%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/icons
./install.sh --dest %{buildroot}%{_datadir}/icons -a

%files
%license  COPYING 
%doc README.md  AUTHORS 
%{_datadir}/icons/BigSu*



%changelog
* Sun Jul 19 2020 yucefsourani <youssef.m.sourani@gmail.com> - 2020.09.07-1
- Version 2020.09.07

* Sun Jul 19 2020 yucefsourani <youssef.m.sourani@gmail.com> - 2020.07.19-1
- Initial
