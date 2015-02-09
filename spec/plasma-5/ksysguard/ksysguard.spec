Name:           ksysguard
Version:        5.2.0
Release:        2%{?dist}
Summary:        KDE Process Management application

License:        GPLv2
URL:            https://projects.kde.org/projects/kde/workspace/ksysguard

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kitemviews-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-ksysguard-devel
BuildRequires:  kf5-kdoctools-devel

BuildRequires:  lm_sensors-devel
BuildRequires:  desktop-file-utils

Requires:       kf5-filesystem

Requires:       ksysguardd = %{version}-%{release}

%description
%{summary}.

%package -n    ksysguardd
Summary: Performance monitor daemon
%description -n ksysguardd
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang ksysguard5 --with-qt --with-kde --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.ksysguard.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f ksysguard5.lang
%doc COPYING COPYING.DOC README
%{_bindir}/ksysguard
%{_kf5_libdir}/libkdeinit5_ksysguard.so
%{_datadir}/ksysguard
%config %{_sysconfdir}/xdg/ksysguard.knsrc
%{_datadir}/applications/org.kde.ksysguard.desktop
%{_docdir}/HTML/en/ksysguard
%{_datadir}/icons/hicolor/*/apps/*.png
%{_kf5_datadir}/knotifications5/ksysguard.notifyrc
%{_kf5_datadir}/kxmlgui5/ksysguard

%files -n ksysguardd
%{_bindir}/ksysguardd
%config %{_sysconfdir}/ksysguarddrc


%changelog
* Mon Feb 09 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-2
- ksysguardd subpackage (originally requested in #426543)

* Mon Jan 26 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-1
- Plasma 5.2.0

* Mon Jan 12 2015 Daniel Vrátil <dvratil@redhat.com> - 5.1.95-1.beta
- Plasma 5.1.95 Beta

* Mon Jan 05 2015 Jan Grulich <jgrulich@redhat.com> - 5.1.1-2
- Fixed license
  Used make install instead of make_install macro
  Removed unnecessary scriptlets and added scriptlets for icon cache
  Added desktop file validation

* Wed Dec 17 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.2-2
- Plasma 5.1.2

* Fri Nov 07 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.1-1
- Plasma 5.1.1

* Tue Oct 14 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0.1-1
- Plasma 5.1.0.1

* Thu Oct 09 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0-1
- Plasma 5.1.0

* Tue Sep 16 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.2-1
- Plasma 5.0.2

* Sun Aug 10 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.1-1
- Plasma 5.0.1

* Wed Jul 16 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-1
- Plasma 5.0.0

* Thu May 15 2014 Daniel Vrátil <dvratil@redhat.com> - 4.90.1-1.20140515gitf7a2bbe
- Intial snapshot
