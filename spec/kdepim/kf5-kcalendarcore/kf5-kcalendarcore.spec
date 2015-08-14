%global framework kcalendarcore
%global git_rev   5542f1

Name:           kf5-%{framework}
Version:        15.08.0
Release:        0.2.git%{git_rev}%{?dist}
Summary:        The KCalendarCore Library

License:        GPLv2+
URL:            https://projects.kde.org/projects/kde/pim/%{framework}

%global versiondir %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
#Source0:        http://download.kde.org/%{stable}/frameworks/%{versiondir}/%{framework}-%{version}.tar.xz
Source0:        kcalcore-%{git_rev}.tar.gz

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  libical-devel

BuildRequires:  kf5-kdelibs4support-devel

Obsoletes:      kdepimlibs%{?_isa} < 15.08.0
Conflicts:      kdepimlibs%{?_isa} < 15.08.0

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kdelibs4support-devel
Requires:       libical-devel
Obsoletes:      kdepimlibs-devel%{?_isa} < 15.08.0
Conflicts:      kdepimlibs-devel%{?_isa} < 15.08.0

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n kcalcore-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_kf5_libdir}/libKF5CalendarCore.so.*

%files devel
%{_kf5_includedir}/kcalcore_version.h
%{_kf5_includedir}/KCalCore
%{_kf5_libdir}/libKF5CalendarCore.so
%{_kf5_libdir}/cmake/KF5CalendarCore
%{_kf5_archdatadir}/mkspecs/modules/qt_KCalCore.pri


%changelog
* Tue Aug 11 2015 Daniel Vrátil <dvratil@redhat.com> - 15.08.0-0.1.git5542f1
- Initial snapshot