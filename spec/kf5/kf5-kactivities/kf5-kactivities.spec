%global framework kactivities

%if 0%{?fedora} > 21 || "%{?copr_projectname}" == "plasma-5"
%global build_main_package 1
%endif

Name:           kf5-%{framework}
Summary:        A KDE Frameworks 5 Tier 3 to organize user work into separate activities
Version:        5.13.0
Release:        0.1%{?dist}

License:        GPLv2+ and LGPLv2+
URL:            http://www.kde.org

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz

BuildRequires:  boost-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kglobalaccel-devel

BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kcmutils-devel

Requires:       kf5-kactivities-libs%{?_isa} = %{version}-%{release}

Obsoletes:      kactivities < 4.90.0
Provides:       kactivities%{?_isa} = %{version}-%{release}
Provides:       kactivities = %{version}-%{release}

%description
A KDE Frameworks 5 Tier 3 API for using and interacting with Activities as a
consumer, application adding information to them or as an activity manager.

%package libs
Summary:        Libraries for KActivities framework
Requires:       kf5-filesystem
%description    libs
%{summary}.

%package devel
Summary:        Developer files for %{name}-libs
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
%{summary}.


%prep
%setup -q -n %{framework}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang kactivities5_qt --with-qt --all-name

%if !0%{?build_main_package}
rm -f %{buildroot}%{_kf5_bindir}/kactivitymanagerd
rm -f %{buildroot}%{_kf5_datadir}/kservices5/*.desktop
rm -f %{buildroot}%{_kf5_datadir}/kservices5/*.protocol
rm -f %{buildroot}%{_kf5_datadir}/kservicetypes5/kactivitymanagerd-plugin.desktop
rm -rf %{buildroot}%{_kf5_qtplugindir}/kactivitymanagerd/
rm -r %{buildroot}%{_kf5_qtplugindir}/*.so
rm -rf %{buildroot}/%{_kf5_datadir}/kf5/kactivitymanagerd
%endif


%if 0%{?build_main_package}
%files
%doc README README.md README.packagers README.developers MAINTAINER
%{_kf5_bindir}/kactivitymanagerd
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/activities.protocol
%{_kf5_datadir}/kservicetypes5/kactivitymanagerd-plugin.desktop
%{_kf5_qtplugindir}/kactivitymanagerd/
%{_kf5_qtplugindir}/*.so
%{_kf5_datadir}/kf5/kactivitymanagerd/
%endif

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs -f kactivities5_qt.lang
%if !0%{?build_main_package}
%doc README README.md README.packagers README.developers MAINTAINER
%endif
%{_kf5_libdir}/libKF5Activities.so.*
%{_kf5_qmldir}/org/kde/activities/

%files devel
%{_kf5_libdir}/libKF5Activities.so
%{_kf5_libdir}/cmake/KF5Activities/
%{_kf5_includedir}/KActivities/
%{_kf5_includedir}/kactivities_version.h
%{_kf5_libdir}/pkgconfig/libKActivities.pc
%{_kf5_archdatadir}/mkspecs/modules/qt_KActivities.pri


%changelog
* Tue Aug 11 2015 Daniel Vrátil <dvratil@redhat.com> - 5.13.0-0.1
- KDE Frameworks 5.13

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 5.12.0-2
- rebuild for Boost 1.58

* Sun Jul 12 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.12.0-1
- 5.12.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Daniel Vrátil <dvratil@redhat.com> - 5.11.0-1
- KDE Frameworks 5.11.0

* Mon May 11 2015 Daniel Vrátil <dvratil@redhat.com> - 5.10.0-1
- KDE Frameworks 5.10.0

* Fri May 08 2015 Rex Dieter <rdieter@fedoraproject.org> 5.9.0-2
- enable main pkg in plasma-5 copr too

* Tue Apr 07 2015 Daniel Vrátil <dvratil@redhat.com> - 5.9.0-1
- KDE Frameworks 5.9.0

* Mon Mar 16 2015 Daniel Vrátil <dvratil@redhat.com> - 5.8.0-1
- KDE Frameworks 5.8.0

* Fri Feb 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.7.0-2
- Rebuild (GCC 5)

* Mon Feb 16 2015 Daniel Vrátil <dvratil@redhat.com> - 5.7.0-1
- KDE Frameworks 5.7.0

* Mon Feb 09 2015 Daniel Vrátil <dvratil@redhat.com> - 5.7.0-1
- KDE Frameworks 5.7.0

* Thu Jan 08 2015 Daniel Vrátil <dvratil@redhat.com> - 5.6.0-1
- KDE Frameworks 5.6.0

* Mon Dec 08 2014 Daniel Vrátil <dvratil@redhat.com> - 5.5.0-1
- KDE Frameworks 5.5.0

* Mon Nov 03 2014 Daniel Vrátil <dvratil@redhat.com> - 5.4.0-1
- KDE Frameworks 5.4.0

* Tue Oct 07 2014 Daniel Vrátil <dvratil@redhat.com> - 5.3.0-1
- KDE Frameworks 5.3.0

* Mon Sep 15 2014 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-1
- KDE Frameworks 5.2.0

* Fri Aug 22 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 5.1.0-4
- Do not build the main package on F21- (#1132715)

* Fri Aug 22 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0-3
- Obsoletes, rather than Conflicts with kactivities

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 06 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0-1
- KDE Frameworks 5.1.0

* Wed Jul 09 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-1
- KDE Frameworks 5.0.0

* Tue Jun 03 2014 Daniel Vrátil <dvratil@redhat.com> - 4.100.0-1
- KDE Frameworks 4.100.0

* Mon May 19 2014 Daniel Vrátil <dvratil@redhat.com> - 4.99.0-5
- Fix provides: kactivities(4) has an epoch set

* Thu May 15 2014 Daniel Vrátil <dvratil@redhat.com> - 4.99.0-4
- Add Conflicts to -runtime

* Wed May 14 2014 Daniel Vrátil <dvratil@redhat.com> - 4.99.0-3
- Remove Conflicts: kactivities, per change in kactivties(4) package

* Tue May 13 2014 Daniel Vrátil <dvratil@redhat.com> - 4.99.0-2
- Add missing kf5-kactivities package
- Fix Conflicts/Provides versions

* Mon May 05 2014 Daniel Vrátil <dvratil@redhat.com> - 4.99.0
- KDE Frameworks 4.99.0

* Mon Apr 28 2014 Daniel Vrátil <dvratil@redhat.com> - 4.98.0-2.20140425gitd1cbd36f
- kf5-kactivities-runtime provides kactivities

* Mon Mar 31 2014 Jan Grulich <jgrulich@redhat.com> 4.98.0-1
- Update to KDE Frameworks 5 Beta 1 (4.98.0)

* Wed Mar 05 2014 Jan Grulich <jgrulich@redhat.com> 4.97.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.97.0)

* Thu Feb 13 2014 Daniel Vrátil <dvratil@redhat.com> - 4.96.0-1
- upgrade to Tier 3 Framework and rename from kactivities-qt5 to kf5-kactivities

* Thu Jan 09 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-0.1.20140109git
- fork from kactivities and build against Qt5
- omitted changelog
