#%define snapshot 20140206
%define framework attica


Name:           kf5-attica
Version:        4.98.0
Release:        1.20140418git52d69993%{?dist}
Summary:        KDE Frameworks Tier 1 Addon with implementation of the Open Collaboration Services API

Group:          Development/Libraries
License:        LGPLv2+
URL:            http://www.kde.org

# git archive --format=tar --prefix=%{name}-%{version}/ \
#             --remote=git://anongit.kde.org/attica,git master | \
# bzip2 -c > %{name}-%{version}-%{snapshot}git.tar.bz
#Source0:        %{name}-%{version}-%{snapshot}git.tar.bz2

Source0:        kf5-attica-52d69993.tar

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel

Requires:       kf5-filesystem

Provides:       attica-qt5
Obsoletes:      attica-qt5

%description
Attica is a Qt library that implements the Open Collaboration Services
API version 1.4.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       attica-qt5-devel
Obsoletes:      attica-qt5-devel
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


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING README.md
%doc ChangeLog
%{_kf5_libdir}/libKF5Attica.so.*

%files devel
%{_kf5_libdir}/cmake/KF5Attica/
%{_kf5_includedir}/attica_version.h
%{_kf5_includedir}/Attica/
%{_kf5_libdir}/libKF5Attica.so
%{_kf5_archdatadir}/mkspecs/modules/qt_Attica.pri
%{_kf5_libdir}/pkgconfig/libKF5Attica.pc


%changelog
* Fri Apr 18 2014 dvratil <dvratil@redhat.com> - 4.98.0-20140418git52d69993
- Update to git: 52d69993

* Mon Mar 31 2014 Jan Grulich <jgrulich@redhat.com> 4.98.0-1
- Update to KDE Frameworks 5 Beta 1 (4.98.0)

* Wed Mar 05 2014 Jan Grulich <jgrulich@redhat.com> 4.97.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.97.0)

* Wed Feb 12 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.96.0)

* Thu Feb 06 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-20140206git
- Attica is now a proper Tier 1 framework

* Wed Feb 05 2014 Daniel Vrátil <dvratil@redhat.com> 1.0.0-20140205git
- Update snapshot of Attica to current git

* Thu Jan 09 2014 Daniel Vrátil <dvratil@redhat.com> 1.0.0-1
- Update to KDE Frameworks 5 TP1 (4.9.95)

* Mon Jan 06 2014 Daniel Vrátil <dvratil@redhat.com> 0.4.2-1
- Attica-qt5 4.9.95 - fork attica to attica-qt5