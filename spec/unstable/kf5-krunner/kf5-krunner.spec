%define framework krunner
%define git_commit 50f7522

Name:           kf5-%{framework}
Version:        4.100.0
Release:        100.%{git_commit}git%{?dist}
Summary:        KDE Frameworks 5 Tier 3 module for KRunner

License:        GPLv2+
URL:            http://www.kde.org
# git archive --format=tar --prefix=%{framework}-%{version}/ \
#             --remote=git://anongit.kde.org/%{framework}.git master | \
# bzip2 -c > %{name}-%{version}-%{snapshot}git.tar.bz2
# Source0:        %{name}-%{version}-%{snapshot}git.tar.bz2
#Source0:        http://download.kde.org/unstable/frameworks/%{version}/%{framework}-%{version}.tar.xz
Source0:	%framework-%{git_commit}.tar.xz


BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-solid-devel
BuildRequires:  kf5-threadweaver-devel

Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 3 module for KRunner


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kconfig-devel
Requires:       kf5-kcoreaddons-devel
Requires:       kf5-ki18n-devel
Requires:       kf5-kservice-devel
Requires:       kf5-plasma-devel
Requires:       kf5-solid-devel
Requires:       kf5-threadweaver-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{framework}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%{_kf5_libdir}/libKF5Runner.so.*
%{_kf5_qmldir}/org/kde/runnermodel
%{_kf5_datadir}/kservicetypes5/plasma-runner.desktop

%files devel
%doc
%{_kf5_includedir}/krunner_version.h
%{_kf5_includedir}/KRunner
%{_kf5_libdir}/libKF5Runner.so
%{_kf5_libdir}/cmake/KF5Runner
%{_kf5_archdatadir}/mkspecs/modules/qt_KRunner.pri

%changelog
* Thu Jun 12 2014 Daniel Vrátil <dvratil@redhat.com> - 4.100.0-100.20140612git
- Git snapshot

* Tue Jun 03 2014 Daniel Vrátil <dvratil@redhat.com> - 4.100.0-1
- KDE Frameworks 4.100.0

* Mon May 05 2014 Daniel Vrátil <dvratil@redhat.com> - 4.99.0
- KDE Frameworks 4.99.0

* Mon Mar 31 2014 Jan Grulich <jgrulich@redhat.com> 4.98.0-1
- Update to KDE Frameworks 5 Beta 1 (4.98.0)

* Wed Mar 05 2014 Jan Grulich <jgrulich@redhat.com> 4.97.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.97.0)

* Wed Feb 12 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-0.1.20140213git
- initial version
