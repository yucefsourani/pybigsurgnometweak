Name:           pybigsurgnometweak
Version:        1.0
Release:        2%{?dist}
Summary:        Python Script To change Gnome Shell look
License:        GPLv3     
URL:            https://github.com/yucefsourani/pybigsurgnometweak
Source0:        https://github.com/yucefsourani/pybigsurgnometweak/archive/master.zip
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       pygobject3
Requires:       python3-gobject
Requires:       gtk3
Requires:       python3-dbus
Requires:       WhiteSur-gtk-theme
Requires:       sur-white-Wallpaper 
Requires:       McMojave-cursors
Requires:       BigSur-icon-theme
   

%description
Python Script To change Gnome Shell look .


%prep
%autosetup -n pybigsurgnometweak-master

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --prefix /usr


%files
%license LICENSE
%doc README.md
%{python3_sitelib}/*
%{_bindir}/pybigsurgnometweak


%changelog
* Sun Jul 19 2020 yucefsourani <youssef.m.sourani@gmail.com> - 1.0-2
- Release 2

* Sun Jul 19 2020 yucefsourani <youssef.m.sourani@gmail.com> - 1.0-1
- Initial
