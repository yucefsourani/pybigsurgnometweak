Name:           sur-white-Wallpaper
Version:        1.0
Release:        1%{?dist}
Summary:        Sur white Wallpaper
BuildArch:      noarch
License:        Unknown
URL:            https://github.com/yeyushengfan258/Sur-white-kde
Source0:        https://raw.githubusercontent.com/yeyushengfan258/Sur-white-kde/master/wallpaper/Sur-white/contents/images/1920x1080.jpg
  

%description
Sur white Wallpaper.

%prep



%build



%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/wallpapers
install -p -m 755 %{SOURCE0} %{buildroot}%{_datadir}/wallpapers/sur-white-Wallpaper.jpg

%files
%{_datadir}/wallpapers/sur-white-Wallpaper.jpg



%changelog
* Sun Jul 19 2020 yucefsourani <youssef.m.sourani@gmail.com> - 1.0-1
- Initial
