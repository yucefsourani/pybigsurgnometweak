Name:           WhiteSur-gtk-theme
Version:        2020.09.07
Release:        1%{?dist}
Summary:        WhiteSur is a MacOS Big Sur like theme
BuildArch:      noarch
License:        GPLv3
URL:            https://github.com/vinceliuice/WhiteSur-gtk-theme
Source0:        https://github.com/vinceliuice/WhiteSur-gtk-theme/archive/master.zip
Requires:       gtk2-engines
Requires:       gtk-murrine-engine
BuildRequires:  sassc
BuildRequires:  glib2-devel
BuildRequires:  inkscape
BuildRequires:  optipng 




%description
WhiteSur is a MacOS Big Sur like theme for GTK 3, GTK 2 and Gnome-Shell which supports 
GTK 3 and GTK 2 based desktop environments like Gnome, Pantheon, XFCE, Mate, etc.

%prep
%autosetup -n %{name}-master

%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/themes
./install.sh --dest %{buildroot}%{_datadir}/themes --icon fedora 

%files
%license LICENSE 
%doc README.md  AUTHORS 
%{_datadir}/themes/WhiteSur-*



%changelog
* Sun Jul 19 2020 yucefsourani <youssef.m.sourani@gmail.com> - 2020.09.07-1
- Version 2020.09.07

* Sun Jul 19 2020 yucefsourani <youssef.m.sourani@gmail.com> - 2020.07.19-1
- Initial
